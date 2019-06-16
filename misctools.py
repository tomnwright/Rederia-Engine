import re,ria

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
def retag(tag, *args):
    '''Add the given tag as the first bindtag for every widget passed in'''
    for widget in args:
        widget.bindtags((tag,) + widget.bindtags())
def select(selected,obj):
    if obj not in selected:
        selected.append(obj)
def get_intDisplay(value, figures):
    value, figures = list(str(float(value))), int(figures)

    point_pos = value.index('.')
    del value[point_pos]
    
    new = []

    for e,i in enumerate(value):
        if e<figures:
            new.append(i)
        elif e == figures:
            new.append(i)
            new_round = round(int(''.join(new)),-1)
            new = list(str(new_round))[:-1]
        elif e<=point_pos:
            new.append('0')

    add_0 = '0'*(figures-len(new))
    if add_0:
        new.append(add_0)
    
    if point_pos < len(new):
        new.insert(point_pos, '.')
    return ''.join(new)
def contains_except(iterable, target_ls):
    for i in iterable:
        if i not in target_ls:
            return True
    
    return False



def parse_obj(f_path):
    Vs = []
    Fs = []
    with open(f_path, "r") as file:
        for line in file.read().splitlines():
            if line.startswith('v '):
                v_list = line.split(" ")
                p = ria.Vector3(
                    float(v_list[1]),
                    float(v_list[2]),
                    float(v_list[3]))
                Vs.append(p)
            if line.startswith('f '):
                fv_list = line.split(" ")
                #split vertices, remove 'f' header
                face = [int(rfv.split("/")[0])-1 for rfv in fv_list[1:]]
                Fs.append(face)
    return Vs, Fs
if __name__ == '__main__':
    v,f = parse_obj('tests/unit_plane.obj')
    print(',\n'.join([str(i) for i in f]))
    '''for i in range(10):
        print(get_intDisplay(1969123.723097,i))'''