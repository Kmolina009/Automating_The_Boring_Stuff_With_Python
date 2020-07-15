def a():
    print('a() starts')
    b()
    d()
    print('a() returns')
    
def b():
    print('b() starts')
    c()
    print('b() return')
    
def c():
    print('c() starts')
    print('c() returns')
    
def d():
    print('c() starts')
    print('c() returns')
    
a()