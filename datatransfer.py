import pickle, ria

class RenderRequest:
    def __init__(self, objs, cam, res, shading):
        self.objs = objs
        self.cam = cam
        self.res = res
        self.shading = shading
    
    def dump(self, filepath):
        dump(self, filepath)

def dump(data, filepath):
    with open(filepath, "wb") as file:
        return pickle.dump(data, file)

def load(filepath):
    with open(filepath, "rb") as file:
        out = pickle.load(file)
    return out

if __name__ == "__main__":
    path = "C:/Users/Tom/Desktop/request00"

    data = load(path)
    print(data)
    