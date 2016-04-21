#!/usr/bin/env python
import os
import sys

import pytest
from subprocess import call


def run_django():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.testapp.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(['manage.py', 'migrate'])
    execute_from_command_line(['manage.py', 'loaddata', 'tests/testapp/fixtures/test_data.json'])
    execute_from_command_line(['manage.py', 'runserver'])


if __name__ == "__main__":
    run_django()

