def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


# @make_pretty
def ordinary():
    print("I am ordinary")


pretty = make_pretty(ordinary)
pretty()
# ordinary()
