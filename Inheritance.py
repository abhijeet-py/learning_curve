# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# child class
class Penguin(Bird):
    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        Bird.swim(self)
        print("Penguin")

    def run(self):
        print("Run faster")


def glob_whois(species):
    species.whoisThis()


peggy = Penguin()
# birdy = Bird()
peggy.whoisThis()
# birdy.whoisThis()
# peggy.swim()
# peggy.run()
# glob_whois(peggy)
# glob_whois(birdy)
