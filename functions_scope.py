a = 45.4
b = 32


def addition(a, b):
    return a + b


print(addition(a, b))
print(type(addition(a, b)))


# scope: global and local
# scope determines the point of accessing a variable


# LEGB rule: Local, Enclosing, Global, Built-in

# 1. local scope
def local_scp():
    var1 = 10
    print(var1)


local_scp()
# print(var1): this will show a name error since it is outside the local variable defined


# 2. enclosing scope: function can access variable inside the fn it is nested in
def greeting():
    message = "Hello There"

    def greeting2():
        print(message)

    greeting2()


greeting()

# EXAMPLE 2:
# var3 = "example"
# upper_var = var3.upper()
# print(upper_var)


def outer_s():
    mess = "Hi Wilma"
    print(mess)

    def inner_s():
        mess2 = "Hi Justin, how you?"
    print(mess)
    inner_s()


outer_s()
# on enclosing scope only the enclosed (inner) scope can access the outer scope variable


# 3.Global variable: declared outside
# way 1: define outside all fns:
g_var = 10
g_var2 = 34


def add(g_var, g_var2):
    return g_var + g_var2


result = add(g_var, g_var2)
print(result)


# way 2: using 'global' keyword to define the variable (inside local scope makes it global):
g_var3 = 23


def powerr(g_var3):
    global g_var4
    g_var4 = 34
    print(g_var3)
    print(g_var4)


def powerr2():
    global g_var3
    g_var3 = 35


# call 1st fn
powerr(g_var3)
print(g_var4)

# call 2nd fn
powerr2()
print(g_var3)
