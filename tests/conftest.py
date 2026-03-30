"""Shared pytest fixtures for backend API tests.

AAA guideline:
- Arrange: prepare inputs and expected state.
- Act: send one API request.
- Assert: verify status code, response payload, and state changes.
"""

from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset the in-memory activities store between tests."""
    original_state = deepcopy(app_module.activities)
    yield
    app_module.activities.clear()
    app_module.activities.update(original_state)


@pytest.fixture
def client():
    """Provide a test client bound to the FastAPI app."""
    return TestClient(app_module.app)
