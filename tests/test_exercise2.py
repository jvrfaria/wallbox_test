import pathlib
import pytest
import subprocess
from src.exercise2 import second_exercise

FILES_PROPERTIES_1 = [
    {
        'name': '1.py',
        'size': str(14 * 2 ** 20),
        'chmod': '777',
        'user': 'admin',
    },
    {
        'name': '2.py',
        'size': '10',
        'chmod': '777',
        'user': 'root',
    },
    {
        'name': '3.py',
        'size': '16',
        'chmod': '666',
        'user': 'admin'
    },
    {
        'name': '4.py',
        'size': str(14 * 2 ** 20 - 1),
        'chmod': '777',
        'user': 'admin'
    },
    {
        'name': '5.py',
        'size': '1',
        'chmod': '766',
        'user': 'admin'
    }
]

FILES_PROPERTIES_2 = [
    {
        'name': '1.py',
        'size': '1',
        'chmod': '777',
        'user': 'root',
    },
    {
        'name': '2.py',
        'size': '10',
        'chmod': '766',
        'user': 'admin',
    },
    {
        'name': '3.py',
        'size': '10',
        'chmod': '766',
        'user': 'admin'
    }
]

FILES_PROPERTIES_3 = [
    {
        'name': '1.py',
        'size': '1',
        'chmod': '744',
        'user': 'admin',
    },
    {
        'name': '2.py',
        'size': '10',
        'chmod': '766',
        'user': 'admin',
    },
    {
        'name': '3.py',
        'size': '10',
        'chmod': '666',
        'user': 'admin'
    }
]

FILES_PROPERTIES_4 = [
    {
        'name': '1.py',
        'size': str(14 * 2 ** 20),
        'chmod': '777',
        'user': 'admin',
    },
    {
        'name': '2.py',
        'size': '10',
        'chmod': '777',
        'user': 'root',
    },
    {
        'name': '3.py',
        'size': '10',
        'chmod': '666',
        'user': 'admin'
    }
]


def _fill_tmpdir(tmp_path: pathlib.Path, files_properties: list[dict]):
    for file_property in files_properties:
        file_path = tmp_path / file_property['name']
        file_path.touch()
        subprocess.run(['fallocate', '-l', file_property['size'], file_path])
        subprocess.run(['chmod', file_property['chmod'], file_path])
        subprocess.run(['chown', file_property['user'], file_path])


@pytest.fixture(scope='session', autouse=True)
def create_admin_user():
    subprocess.run(['useradd', '-p', 'admin', 'admin'])  # create 'admin' user
    yield
    subprocess.run(['userdel', 'admin'])  # remove 'admin' user


@pytest.fixture(params=
[
    # TEST CASE 1: size = 14MB, non-executable and root files before expected file
    (FILES_PROPERTIES_1, '4.py'),
    # TEST CASE 2: one non-executable file with size 14MB and root owner before expected file
    (FILES_PROPERTIES_2, '2.py'),
    # TEST CASE 3: first file meets the requirements
    (FILES_PROPERTIES_3, '1.py'),
    # TEST CASE 4: no file meets the requirements
    (FILES_PROPERTIES_4, None),
    # TEST CASE 5: empty directory
    ([], None)
])
def initial_setup(tmp_path, request):
    # SETUṔ
    file_properties, expected = request.param  # retrive files parameters and name of first test file that meets requirements
    _fill_tmpdir(tmp_path, file_properties)  # creates test files
    yield str(tmp_path.absolute()), expected  # yields test directory path and name of first test file that meets requirements
    # TEARDOWN
    for file in tmp_path.iterdir():  #  deletes test files
        file.unlink()
    tmp_path.rmdir()  # deletes test directory


def test_second_exercise(initial_setup):
    filled_path, expected = initial_setup
    assert second_exercise(filled_path) == expected
