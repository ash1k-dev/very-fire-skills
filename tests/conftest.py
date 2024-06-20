"""
This module is used to provide configuration, fixtures, and plugins for pytest.

It may be also used for extending doctest's context:
1. https://docs.python.org/3/library/doctest.html
2. https://docs.pytest.org/en/latest/doctest.html
"""
import pytest
from model_bakery import baker
from rest_framework.test import APIClient

pytest_plugins = [
    # Should be the first custom one:
    'plugins.django_settings',

    # TODO: add your own plugins here!
    'plugins.main.main_templates',
]

@pytest.fixture
def admin_api_client():
    admin = baker.make('auth.User', is_staff=True, is_superuser=True)
    client = APIClient()
    client.force_authenticate(user=admin)
    return client


@pytest.fixture
def authenticated_api_client():
    authenticated_user = baker.make('auth.User')
    client = APIClient()
    client.force_authenticate(user=authenticated_user)
    return client


@pytest.fixture
def unauthenticated_api_client():
    client = APIClient()
    return client
