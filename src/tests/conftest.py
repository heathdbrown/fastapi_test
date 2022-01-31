"""conftest.py
Test configuration to setup defaults for pytest

"""

import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def test_app():
    """test_app
    Utility function that setups the starlette TestClient

    Returns:
    --------
    client: TestClient

    """
    client = TestClient(app)
    yield client  # testing happens here
