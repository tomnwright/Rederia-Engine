import ria
def add_object(obj):
    ria.objects.append(obj)
while True:
    task = str(input(">>>"))
    print(eval(task))