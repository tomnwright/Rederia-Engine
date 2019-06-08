import ria

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

v,f = parse_obj('tests/unit_cube.obj')
print([str(i) for i in v], f)