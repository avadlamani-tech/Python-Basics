x = 1
def global_func():
    global x
    print(x)
    x = x + 1
    

global_func()
global_func()
global_func()
global_func()