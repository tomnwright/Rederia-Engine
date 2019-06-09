import re
def increment(name):
    #search for '.xyz' ending
    if re.search('\.[0-9][0-9][0-9]$',name):
        i = int(name[-1]) + 1
        if i>9:
            i = 0
            j = int(name[-2]) + 1
            if j > 9:
                j = 0
                k = int(name[-3]) + 1
                if k > 9:
                    return 'x' + name[:-3] + '000'
                else:
                    return name[:-3] + str(k) + str(j) + str(i)
            else:
                return name[:-2]+str(j)+str(i)
        else:
            return name[:-1] + str(i)
    else:
        return name + '.000'