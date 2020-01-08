# -*- coding: utf-8 -*-
from .baseapi import BaseAPI, PUT, DELETE, POST, GET
from .baseapi import BaseAPI
from .utils import list_to_dataframe

class RoboatEnviro(BaseAPI):
    def __init__(self, *args, **kwargs):
        super(RoboatEnviro, self).__init__(*args, **kwargs)
    
    def get_accounts(self, return_type="json"):
        """Return a list of accounts.

        Examples
        --------
        >>> api = roboatenviro.legacy.RoboatEnviro()
        >>> api.get_accounts()

        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"
        
        data = self.fetch_data("users")
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        return data

    def get_sensors(self, return_type="json", **kwargs):
        """Return a list of sensors.

        Parameters
        ----------
        return_type: string, required
            Return a list of json objects if set to 'json', or a dataframe if set to 'dataframe'
        params: dict, optional
            Query based on any column or parameter - see utils for further discussion.

        Returns
        -------
        list or dataframe

        Examples
        --------
        Get a list of all sensors:

        >>> api = quantaq.legacy.QuantAQ()
        >>> api.get_sensors()

        Get a list of all sensors as a dataframe:

        >>> api.get_sensors(return_type='dataframe')

        Get a list of all sensors, but limit to just 2 sensors:

        >>> api.get_sensors(params=dict(limit=2))
        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"

        data = self.fetch_data("sensors", **kwargs)
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        return data

    def get_sensor(self, sn, return_type="json"):
        """Return a single sensor.

        Examples
        --------

        >>> api = quantaq.legacy.QuantAQ()
        >>> api.get_sensor(sn="SN001")
        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"
        
        data = self.fetch_data("sensors/{}".format(sn))
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        return data
    
    def update_sensor(self, sn, **kwargs):
        """Update a sensor.

        Parameters
        ----------
        sn: string, required
            The sensor SN
        params: dict, required
            A dictionary containing the information to update.

        Returns
        -------
        sensor: dict
            A dictionary containing the sensor data
        
        Examples
        --------
        >>> api = quantaq.legacy.QuantAQ()
        >>> api.update_sensor(sn="SN001", params=dict(city="cambridge"))
        """
        return self.fetch_data("sensors/{}".format(sn), type=PUT, **kwargs)
    
    def delete_sensor(self, sn):
        """Delete a sensor.

        Parameters
        ----------
        sn: string, required
            The sensor SN
        
        Examples
        --------
        >>> api = quantaq.legacy.QuantAQ()
        >>> api.delete_sensor(sn="SN001")
        """
        return self.fetch_data("sensors/{}".format(sn), type=DELETE)

    def add_sensor(self, **kwargs):
        """Add a new sensor.

        Parameters
        ----------
        params: dict, required
            A dictionary containing all relevant information including the `sn` and `model`.

        Returns
        -------
        sensor: dict
            A dictionary containing the sensor data

        Examples
        --------
        >>> api = quantaq.legacy.QuantAQ()
        >>> api.add_sensor(params=dict(sn="SN001", ... ,blah="blah"))
        """
        return self._make_request("sensors/", type=POST, **kwargs)

    def add_trf_scan_set(self, **kwargs):
        """Add new trf scan set.

        Parameters
        ----------

        Returns
        -------

        Examples
        --------
        >>> api = quantaq.legacy.QuantAQ()
        >>> api.add_trf_scan_set(params=dict(sn="SN001", ... ,blah="blah"))
        """
        return self._make_request("trf-scan-sets/", type=POST, **kwargs)

    def get_trf_scan_set(self, sn, return_type="json", id=None, **kwargs):
        """Return a list of trf scan sets for a given sensor.

        Parameters
        ----------
        sn: string, required
            The sensor SN you would like data for
        return_type: string, required
            Return a list of json objects if set to 'json', or a dataframe if set to 'dataframe'
        id: int
            You can retrieve an individual scan sets by its ID.
        params: dict, optional
            Query based on any column or parameter - see utils for further discussion.

        Returns
        -------
        list or dataframe

        Examples
        --------
        >>> api.get_trf_scan_set(sn='<sn>', params=dict(limit=25))
        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"
        endpoint = "trf-scan-sets/"
        
        if id is not None:
            return self.fetch_data(endpoint + str(id), **kwargs)

        data = self.fetch_data(endpoint, **kwargs)
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        return data

    def add_trf_data(self, **kwargs):
        """Add new trf data.

        Parameters
        ----------

        Returns
        -------

        Examples
        --------
        >>> api = quantaq.legacy.QuantAQ()
        >>> api.add_trf_data(params=dict(sn="SN001", ... ,blah="blah"))
        """
        return self._make_request("raw-trf-data/", type=POST, **kwargs)

    def delete_trf_data(self, sn, id, **kwargs):
        """Delete a trf data point.

        Parameters
        ----------
        sn: string, required
            The sensor SN
        id: int, required
            The id of the individual data point.

        Returns
        -------
        success: dict
            A dictionary containing the success or failure of the request.

        Examples
        --------
        """
        return self.fetch_data("sensors/{}/data/raw/{}".format(sn, id), type=DELETE)

    def get_trf_data(self, sn, return_type="json", id=None, **kwargs):
        """Return a list of trf data for a given sensor.

        Parameters
        ----------
        sn: string, required
            The sensor SN you would like data for
        return_type: string, required
            Return a list of json objects if set to 'json', or a dataframe if set to 'dataframe'
        id: int
            You can retrieve an individual data point by its ID.
        params: dict, optional
            Query based on any column or parameter - see utils for further discussion.

        Returns
        -------
        list or dataframe

        Examples
        --------
        >>> api.get_trf_data(sn='<sn>', params=dict(limit=25))
        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"
        endpoint = "raw-trf-data/"
        
        if id is not None:
            return self.fetch_data(endpoint + str(id), **kwargs)

        data = self.fetch_data(endpoint, **kwargs)
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        return data

    def add_ssf_data(self, **kwargs):
        """Add new ssf data.

        Parameters
        ----------

        Returns
        -------

        Examples
        --------
        >>> api = quantaq.legacy.QuantAQ()
        >>> api.add_ssf_data(params=dict(sn="SN001", ... ,blah="blah"))
        """
        return self._make_request("raw-ssf-data", type=POST, **kwargs)

    def delete_ssf_data(self, sn, id, **kwargs):
        """Delete an ssf data point.

        Parameters
        ----------
        sn: string, required
            The sensor SN
        id: int, required
            The id of the individual data point.

        Returns
        -------
        success: dict
            A dictionary containing the success or failure of the request.

        Examples
        --------
        """
        return self.fetch_data("sensors/{}/data/raw/{}".format(sn, id), type=DELETE)

    def get_ssf_data(self, sn, return_type="json", id=None, **kwargs):
        """Return a list of ssf data for a given sensor.

        Parameters
        ----------
        sn: string, required
            The sensor SN you would like data for
        return_type: string, required
            Return a list of json objects if set to 'json', or a dataframe if set to 'dataframe'
        id: int
            You can retrieve an individual data point by its ID.
        params: dict, optional
            Query based on any column or parameter - see utils for further discussion.

        Returns
        -------
        list or dataframe

        Examples
        --------
        >>> api.get_ssf_data(sn='<sn>', params=dict(limit=25))
        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"
        endpoint = "raw-ssf-data/"
        
        if id is not None:
            return self.fetch_data(endpoint + str(id), **kwargs)

        data = self.fetch_data(endpoint, **kwargs)
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        return data

    def get_sensor_logs(self, return_type="json", **kwargs):
        """Return a list of sensor logs.

        Parameters
        ----------
        return_type: string, required
            Return a list of json objects if set to 'json', or a dataframe if set to 'dataframe'
        params: dict, optional
            Query based on any column or parameter - see utils for further discussion.

        Returns
        -------
        list or dataframe

        Examples
        --------
        Get a list of all deployments:

        >>> api = quantaq.legacy.QuantAQ()
        >>> api.get_sensor_logs()
        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"
        data = self.fetch_data("sensor-logs")
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        return data

    def add_deployment(self, sn, return_type="json", **kwargs):
        """Add new deployment.

        Parameters
        ----------

        Returns
        -------

        Examples
        --------
        >>> api = quantaq.legacy.QuantAQ()
        >>> api.add_deployment(params=dict(sn="SN001", ... ,blah="blah"))
        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"
        endpoint = "deployments/"
        
        if id is not None:
            return self.fetch_data(endpoint + str(id), **kwargs)
        
        data = self.fetch_data(endpoint, **kwargs)
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        return data
    
    '''
    def update_deployment(self, sn, **kwargs):
        """Update a deployment.

        Parameters
        ----------
        sn: string, required
            The sensor SN
        params: dict, required
            A dictionary containing the information to update.

        Returns
        -------
        sensor: dict
            A dictionary containing the deployment data
        
        Examples
        --------

        >>> api = quantaq.legacy.QuantAQ()
        >>> api.update_deployment(sn="SN001", params=dict(city="cambridge"))
        """
        return self.fetch_data("deployments/{}".format(sn), type=PUT, **kwargs)
    '''

    def get_deployments(self, return_type="json", **kwargs):
        """Return a list of deployments.

        Parameters
        ----------
        return_type: string, required
            Return a list of json objects if set to 'json', or a dataframe if set to 'dataframe'
        params: dict, optional
            Query based on any column or parameter - see utils for further discussion.

        Returns
        -------
        list or dataframe

        Examples
        --------
        Get a list of all deployments:

        >>> api = quantaq.legacy.QuantAQ()
        >>> api.get_deployments()
        """
        assert(return_type in ("json", "dataframe")), "Bad return_type"
        data = self.fetch_data("deployments")
        if return_type == "dataframe":
            data = list_to_dataframe(data)
        return data