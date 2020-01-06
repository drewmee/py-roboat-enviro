# -*- coding: utf-8 -*-
from .baseapi import BaseAPI, PUT, DELETE, POST, GET
from .baseapi import BaseAPI
from .utils import list_to_dataframe

class RoboatEnviro(BaseAPI):
    def __init__(self, *args, **kwargs):
        super(RoboatEnviro, self).__init__(*args, **kwargs)
    
    def get_account(self):
        """Return the account information associated with the API key being used.

        Examples
        --------

        >>> api = roboatenviro.legacy.RoboatEnviro()
        >>> api.get_account()

        """
        return self.fetch_data("users")