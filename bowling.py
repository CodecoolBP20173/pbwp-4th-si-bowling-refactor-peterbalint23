def get_value(char):
    if char in "123456789":
        return int(char)
    elif char.lower() == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def score(game):
    result = 0
    frame = 1
    in_first_half = True

    for rolls in range(len(game)):
        if game[rolls] == '/':
            result += 10 - last
        else:
            result += get_value(game[rolls])

        if frame < 10 and get_value(game[rolls]) == 10:
            if game[rolls] == '/':
                result += get_value(game[rolls + 1])
            elif game[rolls].lower() == 'x':
                result += get_value(game[rolls + 1])
                if game[rolls + 2] == '/':
                    result += 10 - get_value(game[rolls + 1])
                else:
                    result += get_value(game[rolls + 2])

        last = get_value(game[rolls])
        if not in_first_half or game[rolls].lower() == 'x':
            frame += 1

        in_first_half = not in_first_half

    return result
