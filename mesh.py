import ria

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
        [1, 2, 4, 3],
        [3, 4, 8, 7],
        [7, 8, 6, 5],
        [5, 6, 2, 1],
        [3, 7, 5, 1],
        [8, 4, 2, 6]
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
        [1, 2, 4, 3],
        ]
    return ria.Mesh(Vs,Fs)

