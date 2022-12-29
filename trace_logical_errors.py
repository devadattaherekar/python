def foo():
    print("foo called")
    list1 = [10,20,30,40,50]
    for item in range(5):
        print(item)
        print(list1[item])
        list1[item]=99
    print(list1)
    print("foo ends")


def bar():
    print("Bar called")
    foo()
    print("bar ends")


def newbar():
    print("new bar called")
    bar()
    print("new bar ends")


bar()