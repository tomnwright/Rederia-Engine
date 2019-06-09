class PolyOBJ(Object3D):
    #restructure to include mesh
    def __init__(self, vertices, faces, position = Vector3.zero, rotation = Vector3.zero, size = Vector3.unit):
        super().__init__(position,rotation,size)
        self.vertices = vertices
        self.faces = faces
    def global_space(self):
        gVs = []
        for vertex in self.vertices:
            n = vertex.vector_scale(self.size)
            n += self.position
            gVs.append(n)
        return gVs