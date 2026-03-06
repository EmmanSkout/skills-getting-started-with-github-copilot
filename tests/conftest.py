"""Shared pytest fixtures for FastAPI backend tests."""

from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client() -> TestClient:
    """Provide a test client for the FastAPI app."""
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities() -> None:
    """Reset in-memory activity data before each test to avoid state leaks."""
    original_state = deepcopy(app_module.activities)

    yield

    app_module.activities.clear()
    app_module.activities.update(deepcopy(original_state))