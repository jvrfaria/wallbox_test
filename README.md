# Wallbox technical test: part 1

The functions are in `src` directory.
Tests are in `tests` directory.

Developed and tested with python 3.10.4. Maybe it won't work with < 3.10 python versions because the codes uses `|` notation to represents Union types.
Developed and tested with Ubuntu. It won't work in Windows systems and (maybe) other Linux distributions because the 2nd exercise deals with creation/deletion of users and
the command syntax used considers an Ubuntu system.

The tests need to be executed using a root user because the 2nd exercise creates and deletes an user called 'admin'.

To execute:

`pip install -r requirements.txt`

`pytest`
