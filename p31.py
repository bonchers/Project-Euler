value = [200, 100, 50, 20, 10, 5, 2, 1]

def fitcombis(ind, fit):
    if fit == 0 or ind == 7: # no more to fit OR reached last index i.e. '1', only 1 possibility left
        return 1

    combis = occupy = 0
    while occupy <= fit: # all possible amounts value[ind] can occupy in fit amount
        combis += fitcombis(ind + 1, fit - occupy)
        occupy += value[ind]
    
    return combis

print(fitcombis(0, 200))