import os

import pytest
from dotenv import load_dotenv
from py_roboat_enviro import RoboatEnviroData
from uplink.auth import ApiTokenHeader

from .utils import generate_random_name


def cleanup(api_client):
    # Delete all sensors
    response = api_client.get_sensors()
    for sensor in response.json():
        sn = sensor["sn"]
        response = api_client.delete_sensor_by_sn(sn)

    # Delete all spec measurements
    response = api_client.get_all_spec_measurement_filenames()
    for f in response.json():
        filename = f["filename"]
        response = api_client.delete_spec_spec_measurements_by_filename(filename)


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def api_client(load_env):
    """Instantiate the API client as a fixture to provide to all tests.

    Args:
        load_env ([type]): [description]

    Returns:
        [type]: [description]
    """

    # token_auth = ApiTokenHeader("api-key", os.environ["DEV_API_KEY"])
    # url = "http://localhost:5000/api/"
    token_auth = ApiTokenHeader("api-key", os.environ["STAGING_API_KEY"])
    url = "https://roboat-enviro-staging.herokuapp.com/api/"

    api = RoboatEnviroData(url, auth=token_auth)
    cleanup(api)
    yield api
    cleanup(api)


@pytest.fixture(scope="session", autouse=True)
def user_id(api_client):
    """Get the first user in the DB and provide the user's ID to tests.
    Eventually, it would be good to have the ability to create a new
    user through the REST API. At the moment, new users can only be
    created through the web-interface.

    Args:
        api_client ([type]): [description]

    Returns:
        [type]: [description]
    """
    response = api_client.get_users()
    uid = response.json()[0]["id"]
    return uid


@pytest.fixture(scope="session", autouse=True)
def sensor_sn(api_client):
    """Handles creation of a new sensor to provide a sensor SN
    to tests. Deletes the sensor from the DB following the completion of the tests.

    Args:
        api_client ([type]): [description]

    Yields:
        [type]: [description]
    """
    nickname = generate_random_name(24)
    response = api_client.add_sensor(nickname)
    sn = response.json()["sn"]
    return sn
