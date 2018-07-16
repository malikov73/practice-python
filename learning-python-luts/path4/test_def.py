def f(x):
    x += 1

    def f1(x=x):
        print(x)
    return f1


#y = f(1)
#y()
#y(4)
l = []
for i in range(9):
    l.append(lambda x, i=i: x**i)
#print("list def: ", l)

#for i in l:
#     print(i(2))


def func():
    x = 10
    print(x+1)

    def func1(y):
        nonlocal x
        x += y
        print(x)
    print(x+2)
    return func1


#test = func()
#test(5)


def func_nesting_3():
    x = 10
    print("1 - ", x)

    def func1(y):
        nonlocal x
        print("2 - ", x)

        def func2(z):
            print(x)
            nonlocal x
            print("3 - ", x)
            x += z
            print("4 - ", x)
        print("5 - ", x)
        x += y
        print("6 - ", x)
        return func2
    print("7 - ", x)
    return func1


test = func_nesting_3()
test1 = test(10)
test2 = test1(7)
