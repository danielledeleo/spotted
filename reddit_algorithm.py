from datetime import datetime, timedelta

def hot(ups, downs, date):
    """The hot formula."""
    s = score(ups, downs)
    order = log10(max(abs(s), 1))
    if s > 0:
        sign = 1
    elif s < 0:
        sign = -1
    else:
        sign = 0
    seconds = date - 1134028003
    return round(order + sign * seconds / 45000, 7)