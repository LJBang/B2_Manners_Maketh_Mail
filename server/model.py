def recommand(sent):
    res = [sent+str(x+1) for x in range(3)]
    return res