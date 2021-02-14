def jumpingOnClouds(c):

    num_jumps = 0
    i = 0
    while i < len(c)-1:
        if (i+2 == len(c)) or (c[i+2] == 1):
            i += 1
            num_jumps += 1
        else:
            i += 2
            num_jumps += 1
            
    return num_jumps
