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
                face = [int(rfv.split("/")[0]) for rfv in fv_list[1:]]
                Fs.append(face)
    return Vs, Fs
if __name__ == '__main__':
    v,f = parse_obj('tests/unit_plane.obj')
    print([str(i) for i in v], f)