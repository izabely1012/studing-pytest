import pytest
import requests
from unittest.mock import MagicMixin

@pytest.fixture
def mock_response():
    mock = 