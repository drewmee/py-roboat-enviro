import json
import random
import string

import pytest
from roboat_enviro_backend import db
from roboat_enviro_backend.schemas import SensorSchema, UserSchema

sensor_sn = "0CR9CPZW1GJ3"


def generate_sample_set_UUID(length=36):
    return "".join(
        random.SystemRandom().choice(string.ascii_uppercase + string.digits)
        for _ in range(length)
    )


class TestUsers:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

    def test_get_users(self):
        response = self.api_client.get_users()
        assert response.ok
        assert response.json()
        users = UserSchema().load(
            response.json(), many=True, partial=True, transient=True
        )
        assert users

    def test_get_user_by_id(self):
        user_id = 1
        response = self.api_client.get_user_by_id(user_id)
        assert response.ok
        assert response.json()
        user = UserSchema().load(response.json(), partial=True, transient=True)
        assert user.id == user_id

    def test_search_users(self):
        filters = [{"field": "id", "op": "<", "value": 24}]
        filters = json.dumps(filters)
        response = self.api_client.search_users(filters)
        assert response.ok
        assert response.json()
        users = UserSchema().load(
            response.json(), many=True, partial=True, transient=True
        )
        assert users


class TestSensors:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

    def test_add_sensor(self):
        nickname = "test-sensor1"
        response = self.api_client.add_sensor(nickname)
        assert response.ok
        assert response.json()

    def test_get_sensors(self):
        response = self.api_client.get_sensors()
        assert response.ok
        assert response.json()
        sensors = SensorSchema().load(
            response.json(), many=True, partial=True, transient=True
        )
        print(sensors)
        assert sensors

    def test_get_sensor_by_id(self):
        sensor_id = 1
        response = self.api_client.get_sensor_by_id(sensor_id)
        assert response.ok
        assert response.json()
        sensor = SensorSchema().load(response.json(), partial=True, transient=True)
        assert sensor.id == sensor_id

    def test_search_sensors(self):
        filters = [{"field": "id", "op": "<", "value": 100}]
        filters = json.dumps(filters)
        response = self.api_client.search_sensors(filters)
        assert response.ok
        assert response.json()
        sensors = SensorSchema().load(
            response.json(), many=True, partial=True, transient=True
        )
        assert sensors


class TestSensorDiagnostics:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

    def test_add_sensor_diagnostics(self):
        data = [
            {
                "datetime_utc": "2021-03-27T18:01:45.398Z",
                "sensor_sn": sensor_sn,
                "cpu_temp": 0,
                "gps_usb_conn": True,
                "spec_usb_conn": True,
                "monochrom_usb_conn": True,
                "mem_avail_percent": 0,
                "cellular_usb_conn": True,
                "load_avg": 0,
                "relay_i2c_conn": True,
                "net_conn": True,
                "external_usb_conn": True,
                "uptime": 0,
                "mem_avail_gb": 0,
                "disk_usage": 0,
            }
        ]
        response = self.api_client.add_sensor_diagnostics(data)
        assert response.ok

    def test_search_sensor_diagnostics(self):
        filters = [{"field": "sensor_sn", "op": "=", "value": sensor_sn}]
        filters = json.dumps(filters)
        response = self.api_client.search_sensor_diagnostics(filters)
        assert response.ok
        assert response.json()

        filters = [
            {"field": "datetime_utc", "op": ">", "value": "2021-03-26"},
            {"field": "datetime_utc", "op": "<", "value": "2021-03-28"},
        ]
        filters = json.dumps(filters)
        response = self.api_client.search_sensor_diagnostics(filters)
        assert response.ok
        assert response.json()

        """
        sensor_diagnostics = SensorDiagnosticsSchema().load(
            response.json(), many=True, partial=True, transient=True
        )
        assert sensor_diagnostics
        """


class TestSensorLogs:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

    def test_add_sensor_logs(self):
        data = [
            {
                "message": "string",
                "sensor_sn": sensor_sn,
                "func_name": "string",
                "filename": "string",
                "priority": "string",
                "line_num": 0,
                "user": "string",
                "datetime_utc": "2021-03-28T22:55:05.074Z",
            }
        ]
        response = self.api_client.add_sensor_logs(data)
        assert response.ok

    def test_search_sensor_logs(self):
        filters = [{"field": "sensor_sn", "op": "=", "value": sensor_sn}]
        filters = json.dumps(filters)
        response = self.api_client.search_sensor_logs(filters)
        assert response.ok
        assert response.json()

        filters = [
            {"field": "datetime_utc", "op": ">", "value": "2021-03-26"},
            {"field": "datetime_utc", "op": "<", "value": "2021-03-29"},
        ]
        filters = json.dumps(filters)
        response = self.api_client.search_sensor_logs(filters)
        assert response.ok
        assert response.json()


class TestGPSMeasurements:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

    def test_add_gps_measurements(self):
        data = [
            {
                "datetime_utc": "2021-03-28T16:50:07.105Z",
                "sensor_sn": sensor_sn,
                "latitude": 42.360001,
                "longitude": -71.092003,
            }
        ]
        response = self.api_client.add_gps_measurements(data)
        assert response.ok

    def test_search_gps_measurements(self):
        filters = [{"field": "sensor_sn", "op": "=", "value": sensor_sn}]
        filters = json.dumps(filters)
        response = self.api_client.search_gps_measurements(filters)
        assert response.ok
        assert response.json()
        print(response.json())

        filters = [
            {"field": "datetime_utc", "op": ">", "value": "2021-03-26"},
            {"field": "datetime_utc", "op": "<", "value": "2021-03-29"},
        ]
        filters = json.dumps(filters)
        response = self.api_client.search_gps_measurements(filters)
        assert response.ok
        assert response.json()


class TestSpectroscopyMeasurementMetadata:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

    # def test_delete__spectroscopy_measurement_metadata(self):

    def test_add_spectroscopy_measurement_metadata(self):
        scan_file = open("tests/test.txt", "r")
        scan_data = scan_file.read()
        scan_file.close()

        sample_set_UUID = generate_sample_set_UUID()
        scan_type = "water_raman"
        scan_index = 1
        s3_filepath = "%s_%s%d.csv" % (sample_set_UUID, scan_type, scan_index)
        data = {
            "datetime_utc": "2021-03-28T16:50:51.201Z",
            "sensor_sn": sensor_sn,
            "sample_set": sample_set_UUID,
            "scan_type": scan_type,
            "scan_index": scan_index,
            "s3_filepath": s3_filepath,
            "dilution_factor": 1,
            "collected_by": "string",
            "description": "string",
            "comments": "string",
        }
        response = self.api_client.add_spectroscopy_measurement_metadata(
            scan_data, json.dumps(data)
        )
        # print(response.json())
        assert response.ok

    def test_search_spectroscopy_measurement_metadata(self):
        filters = [{"field": "sensor_sn", "op": "=", "value": sensor_sn}]
        filters = json.dumps(filters)
        response = self.api_client.search_spectroscopy_measurement_metadata(filters)
        assert response.ok
        assert response.json()

        filters = [
            {"field": "datetime_utc", "op": ">", "value": "1969-03-26"},
            {"field": "datetime_utc", "op": "<", "value": "2022-04-21"},
        ]
        filters = json.dumps(filters)
        response = self.api_client.search_spectroscopy_measurement_metadata(filters)
        print(response.json())
        assert response.ok
        assert response.json()


class TestSpectroscopyMeasurements:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        self.api_client = api_client

    def test_get_spec_measurement_filenames(self):
        response = self.api_client.get_spec_measurement_filenames()
        assert response.ok
        print(response.json())

    def test_get_spec_measurements_by_filename(self):
        filename = "P3IK19EOB5AUF2UE3X4824OEJMATEZ56BCWY_water_raman1.csv"
        response = self.api_client.get_spec_measurements_by_filename(filename)
        assert response.ok
        print(response.json())
