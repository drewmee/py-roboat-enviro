import os

import pytest
from dotenv import load_dotenv
from py_roboat_enviro import RoboatEnviroData
from uplink.auth import ApiTokenHeader


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def api_client(load_env):
    # token_auth = ApiTokenHeader("api-key", os.environ["PROD_API_KEY"])
    # url = "https://roboat-enviro.herokuapp.com/api/"
    token_auth = ApiTokenHeader("api-key", os.environ["DEV_API_KEY"])
    url = "http://localhost:5000/api/"
    api = RoboatEnviroData(url, auth=token_auth)
    return api
