a = 123

def func():
    global a
    a = 12
    print(a)

func()
print(a)