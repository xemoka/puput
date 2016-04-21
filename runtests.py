#!/usr/bin/env python
import os
import sys

import pytest


def run_django():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.testapp.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line('migrate')
    execute_from_command_line('loaddata blog/fixtures/test_data.json')
    execute_from_command_line('runserver &')


def run_tests():
    pytest.main()


if __name__ == "__main__":
    run_django()
    run_tests()

