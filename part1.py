def check_array_of_integers(array):
    if not isinstance(array, list) and not isinstance(array, tuple):
        print(f"{array} is not list or tuple or int")
        raise TypeError(array)


def first_exercise(array1: list[int] | tuple[int], array2: list[int] | tuple[int]) -> int | None:
    """
    :param array1: list or tuple of int
    :param array2: list or tuple of int
    :return: Returns the first repeated integer between array1 and array2.
    Returns None if it doesn't find a repeated integer.
    """
    check_array_of_integers(array1)
    check_array_of_integers(array2)
    result = None
    number_map = dict()
    len_array1 = len(array1)
    len_array2 = len(array2)
    max_length = max(len_array1, len_array2)
    for index in range(max_length):
        if index < len_array1:
            number1 = array1[index]
            number_state1 = number_map.get(number1, 0)
            if number_state1 == 0:
                number_map[number1] = 1
            elif number_state1 == 2:
                result = number1
                break
        if index < len_array2:
            number2 = array2[index]
            number_state2 = number_map.get(number2, 0)
            if number_state2 == 0:
                number_map[number2] = 2
            elif number_state2 == 1:
                result = number2
                return result
    return result

