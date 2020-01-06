import unittest
import os
import sys
import pandas as pd
from dotenv import load_dotenv
import roboatenviro

class SetupTestCase(unittest.TestCase):
    def setUp(self):
        # source the local dev token
        load_dotenv()
        self.token = os.getenv('ROBOAT-ENVIRO_APIKEY_DEV')
        self.api = roboatenviro.legacy.RoboatEnviro(token=self.token)
        self.api.endpoint = "http://localhost:5000/api/"
    
    def tearDown(self):
        pass

    def test_account(self):
        mngr = self.api
        self.assertEqual(mngr.endpoint, "http://localhost:5000/api/")

        # return the account as json
        account = mngr.get_account()
        print(account)
        #self.assertIsNotNone(account["confirmed"])
        #self.assertIsNotNone(account["name"])
        #self.assertIsNotNone(account["email"])
