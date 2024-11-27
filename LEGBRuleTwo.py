x = "global"
def outer():
    x = "outer local"
    def inner():
        x = "inner local"
        def func():
            print(x)

        func()

    inner()

outer()

