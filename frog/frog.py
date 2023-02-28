class Frog:
    def __init__(self):
        self.is_hungry = True
        self.is_asleep = False
        self.grass_length = 10

    def live(self):
        if self.is_asleep:
            print("The frog is sleeping.")
        elif self.is_hungry:
            self.eat()
        else:
            self.walk_and_eat()

    def eat(self):
        if self.grass_length > 0:
            self.grass_length -= 1
            self.is_hungry = False
            print("The frog ate some grass.")
        else:
            print("There is no grass left for the frog to eat.")

    def walk_and_eat(self):
        if self.grass_length > 0:
            self.grass_length -= 1
            print("The frog walked and ate some grass.")
        else:
            print("There is no grass left for the frog to eat.")

    def sleep(self):
        self.is_asleep = True
        print("The frog is sleeping.")

    def wake_up(self):
        self.is_asleep = False
        print("The frog woke up.")

    def rain(self):
        self.grass_length += 5
        print("It rained and the grass grew longer.")