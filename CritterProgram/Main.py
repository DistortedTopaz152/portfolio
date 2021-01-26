import random

class Critter(object):
    days = 0
    hours = 0

    def __int__(self):
        self.age = 0
        self.health = 100
        self.hunger = 0
        self.height = 0
        self.weight = 0
        self.name = ""
        self.happy = 100
        self.isAlive = True

    # setters
    def set_name(self,name):
        if len(name) > 4 or len(name) < 4:
            if "uck" not in name:
                if "sh" not in name:
                    if "unt" not in name:
                        self.name = name

    def die(self):
        print("Your pet has died you are an awful horibal person")
        self.isAlive = False

    # getters
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def get_health(self):
        return self.health
    def get_hunger(self):
        return self.hunger
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_happy(self):
        return self.happy
    def get_isAlive(self):
        return self.isAlive

    def intro(self):
        print("Hello my name is "+self.get_name())

    def feed(self,food):
        if food == "pizza":
            self.hunger -= 12
        elif food == "cheese burger":
            self.hunger -= 18
        elif food == "steak":
            self.hunger -= 25
        elif food == "taco":
            self.hunger -= 5
        elif food == "cheesecake":
            self.hunger -= 100
        elif food == "left arm":
            self.hunger -= 7002
            self.die()
        else:
            self.hunger -= 10

    def pass_time(self,hours):
        for i in range(hours):
            self.hunger += 5
            if self.hunger > 50:
                self.weight -= .5
                self.happy -= 15
                self.health -= 5
            if self.hunger < 0:
                self.weight += .5
                self.happy += 15
                self.health -= 2
        self.happy -= 5
        self.height += .01
        hours+=1
        if hours == 5:
            Critter.days+=1
            Critter.hours = 0
        if Critter.days > 0 and Critter.days % 10 == 0:
            self.age+=1
        if self.age >= 99:
            chance = random.randint(5)
            if chance == 0:
                self.isAlive = False

    def play(self,time):
        self.pass_time(self,time)
        self.happy += 10*time
        self.health += 2*time
        if self.happy > 100:
            self.happy = 100
        if self.health == 100:
            self.health = 100

    def hud(self):
        print("Pet name "+self.get_name())
        print("Pet Height: "+str(self.get_height))
        print("Pet Weight: "+str(self.get_weight))
        print("Pet Age: "+str(self.get_age()))
        health = self.get_health()
        if health > 80:
            print("Health: Great")
        elif health > 60:
            print("Health: Good")
        elif health > 50:
            print("Health: Fair")
        elif health == 0:
            self.die()
        else:
            print("Health: Poor")

        hunger = self.get_hunger()
        if hunger > 40:
            print("Hunger: Starving")
        elif hunger > 20:
            print("Hunger: Vary Hungry")
        elif hunger > 10:
            print("Hunger: Full")

        happy = self.get_happy()
        if happy > 50:
            print("Happy: Happy")
        if happy > 35:
            print("Happy: Grumpy")
        else:
            print("Happy: Pissed")
def main():
    pet = Critter()
    pet.set_name(input("What is your pets name?"))
    pet.hud()
    while pet.get_isAlive():
        pet.pass_time(1)
        answer = input("what would you like to do with your pet (feed, play or ignore)").lower()
        if answer == "feed":
            food = input("What do you want to feed your pet").lower()
            pet.feed(food)
        if answer == "play":
            time = int(input("How long will you play with your pet"))
            pet.play(time)
        else:
            pet.pass_time(1)
main()