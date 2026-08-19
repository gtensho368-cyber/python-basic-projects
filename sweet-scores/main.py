

def get_score(num_mangoes, num_apples, num_bananas, num_cherries, has_poison_apple):
    mangoes = mangoes_score(num_mangoes)
    apples = apple_score(num_apples, has_poison_apple)
    bananas = bananas_score(num_bananas)
    cherries = cherries_score(num_cherries)
    return sum([mangoes, apples, bananas, cherries])


def mangoes_score(mangoes):
    if mangoes % 2 == 0:
        return mangoes * 3
    else:
        return 0

def apple_score(apples, has_poison_apple):
    if has_poison_apple:
        for _ in range(apples):
            apples -= 2

    return apples * 2

def bananas_score(bananas):
    # Bananas have more value in bunches
    if bananas == 1:
        return 1
    elif bananas == 2:
        return 4 
    elif bananas == 3:
        return 8
    elif bananas >= 4:
        return bananas * 2

def cherries_score(cherries):
    pair = cherries//2 
    return pair * 5


print(get_score(6, 5, 4, 6, True))









