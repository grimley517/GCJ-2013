def surprising(scores):
    if scores.max - scores.min == 2:
        return True
    else:
        return False
