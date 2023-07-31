"""This file is used to configure pytest"""
import pytest
from blazar_proxy import create_app

@pytest.fixture()
def app():
    """
    Create and configure a new app instance for each test.
    """
    app = create_app('TestingConfig')  # disable=redefined-outer-name

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):  # disable=redefined-outer-name
    """
    Create a test client for the app.
    """
    return app.test_client()


@pytest.fixture()
def runner(app):  # disable=redefined-outer-name
    """
    Create a test runner for the app's Click commands.
    """
    return app.test_cli_runner()
