import ria, misctools

def cube():
    Vs = [
        ria.Vector3(-1.0, -1.0, 1.0),
        ria.Vector3(-1.0, 1.0, 1.0),
        ria.Vector3(-1.0, -1.0, -1.0),
        ria.Vector3(-1.0, 1.0, -1.0),
        ria.Vector3(1.0, -1.0, 1.0),
        ria.Vector3(1.0, 1.0, 1.0),
        ria.Vector3(1.0, -1.0, -1.0),
        ria.Vector3(1.0, 1.0, -1.0)
        ]
    Fs = [
        [0, 1, 3, 2],
        [2, 3, 7, 6],
        [6, 7, 5, 4],
        [4, 5, 1, 0],
        [2, 6, 4, 0],
        [7, 3, 1, 5]
        ]
    return ria.Mesh(Vs,Fs)

def plane():
    Vs = [
        ria.Vector3(-1.0, 0.0, 1.0),
        ria.Vector3(1.0, 0.0, 1.0),
        ria.Vector3(-1.0, 0.0, -1.0),
        ria.Vector3(1.0, 0.0, -1.0) 
        ]
    Fs = [
        [0, 1, 3, 2],
        ]
    return ria.Mesh(Vs,Fs)

def from_obj (file):
    fV, fF = misctools.parse_obj(file)
    return ria.Mesh (fV, fF)