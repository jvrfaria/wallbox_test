import pathlib


def owner_is_admin(path: pathlib.Path):
    return path.owner() == 'admin'  # file owner


def file_is_executable(path: pathlib.Path):
    mode = bin(path.stat().st_mode)[-7::3]  # file execution permissions for creator, group and others
    return '1' in mode


def file_size_lower(path: pathlib.Path):
    return path.stat().st_size < 14*2**20  # size smaller than 14*2²⁰ bytes (14 MB)


def second_exercise(path: str) -> str | None:
    """
    :param path: a system path as string
    :return: Returns as string the name of the first file that meets these requirements:
        size < 14*2²⁰ bytes (14 MB),
        file owner: 'admin' user,
        file is executable.
        Returns None if no file inside 'path' meets these requirements
    """
    path_obj = pathlib.Path(path)
    result = None
    for child in sorted(path_obj.iterdir()):
        if child.is_file() and owner_is_admin(child) and file_is_executable(child) and file_size_lower(child):
            result = child.name
            break
    return result
