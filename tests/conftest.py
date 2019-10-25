import time
import uuid

import pytest


@pytest.fixture(scope="session")
def session_uuid():
    yield uuid.uuid4()


@pytest.fixture(scope="module")
def module_uuid():
    yield uuid.uuid4()


@pytest.fixture(scope="class")
def class_uuid():
    yield uuid.uuid4()


@pytest.fixture(scope="function")
def function_uuid():
    yield uuid.uuid4()


def pytest_addoption(parser):
    parser.addoption(
        "--port", action="store", default="/dev/ttyUSB0", help="grbl serial port"
    )
    parser.addoption(
        "--baudrate", action="store", default="115200", help="grbl serial baudrate"
    )


import gcode


@pytest.fixture(scope="function")
def gcode_program():
    yield gcode.GCode()
