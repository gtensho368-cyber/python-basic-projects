
def score_rank(score):
    """Returns a rank string based on the interger"""
    if score <= 10:
        return "novince"
    elif score <= 20:
        return "amateur"
    elif score <= 30:
        return "experienced"
    elif score <= 40:
        return "advanced"
    else:
        return "master"

users_score = [10, 20, 30, 40, 50]

for scores in users_score:
    print(score_rank(scores))









