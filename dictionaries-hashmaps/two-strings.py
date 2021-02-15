# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1 = set(list(s1))
    s2 = set(list(s2))
    share = s1 & s2
    if len(share) > 0:
        return "YES"
    else:
        return "NO"
