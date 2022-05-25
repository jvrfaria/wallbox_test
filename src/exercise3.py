def third_exercise(coinset: str | list | tuple):
    """
    :param coinset: sequence of '0's and '1's (tails and heads) as string, list[strings] or tuple[strings]
    :return: returns the mininum of permutations to intersperse the 'coinset' sequence. Returns None if
    the sequence can't be inserpersed or if the sequence has an element different of '0' and '1'
    """
    result = None
    number_of_coins = len(coinset)
    number_of_tails, number_of_heads = 0, 0
    for coin in coinset:
        if coin == '0':
            number_of_tails += 1
        elif coin == '1':
            number_of_heads += 1
        else:
            return result  # there is a character different of '0' and '1' at input
    # returns None if the coinset can't be interspersed or the coinset length is 0 or 1
    if abs(number_of_heads - number_of_tails) > 1 or number_of_coins < 2:
        return result
    elif number_of_coins % 2:  # number of coins is odd
        even_positions = (number_of_coins + 1)/2
        if number_of_tails > number_of_heads:
            tails_at_even_positions = 0
            for index in range(number_of_coins):
                if index % 2 == 0 and coinset[index] == '0': tails_at_even_positions += 1
            return even_positions - tails_at_even_positions
        else:
            heads_at_even_positions = 0
            for index in range(number_of_coins):
                if index % 2 == 0 and coinset[index] == '1': heads_at_even_positions += 1
            return even_positions - heads_at_even_positions
    else:  # number of coins is even
        tails_at_even_positions = 0
        tails_at_odd_positions = 0
        for index in range(number_of_coins):
            if coinset[index] == '0':
                if index % 2 == 0:
                    tails_at_even_positions += 1
                else:
                    tails_at_odd_positions += 1
        return min(number_of_coins // 2 - tails_at_even_positions, number_of_coins // 2 - tails_at_odd_positions)



