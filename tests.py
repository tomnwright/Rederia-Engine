class MatrixError(Exception):
    def __init__(self, text, *args, **kwargs):
        super().__init__(text, *args, **kwargs)

class Test:
    def __init__(self, data):
        self.data = Test.TestData(data)

    class TestData(list):
        pass

x = Test([1,2,3])

y = Test.TestData()
print([int()] * 10)