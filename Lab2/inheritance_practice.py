"""
Author: Prof. Alyssa
Description: Practicing inheritance and 
    other OOP paradigms
"""


# Class defining a generic animal
class Animal:
    def __init__(self, name, hungry=False, pred=True):
        self.name = name
        self.hungry = hungry
        self.pred = pred

        #36 
        #self._healthy = True
        #41
        self.__healthy = True

    # Print what the animal "says"
    def speak(self):
        print("Speaking! What do I say??")

    def sleep(self) -> None: # Prints that the animal slept and makes it hungry
        print(f"{self.name} slept")
        self.hungry = True

    def eat(self, food) -> bool: # returns if the animal ate and prints the food it ate
        if self.hungry == True:
            print(f"{self.name} ate {food}!")
            self.hungry == False
            return True
        return False
    
    def isPreditor(self) -> bool:
        return self.pred
    
    #45.c
    def get_healthy(self):
        return self.__healthy
    

#7 Class defining a bird
class Bird(Animal):

    #25
    def __init__(self, name):
        self.nest_location = None

        # 31 call the parent class constructor
        super().__init__(name) 


    def fly(self) -> None:
        print("I can fly!")

    #19 Overriding the speak method to make the bird chirp
    def speak(self):
        print("chirp chirp chirp")

    #45.d
    def get_healthy(self):
        return self.__healthy
    

#49
class fish(Animal):
    def __init__(self, name):

        super().__init__(name+"fish")

    def swim(self) -> None:
        print("Just keep swimming")

    def fly(self) -> None:
        print("I can't fly")
        
    




def run():

    #49
    a_fish = fish("Nemo")
    print(a_fish.name)
    a_fish.swim()
    a_fish.fly()
    a_fish.speak()

    #37
    a_bird = Bird("Big Bird")
    #print(a_bird._healthy)

    #41 
    #print(a_bird.__healthy)

    '''
    #45
    print(a_bird.__healthy)
    print(Animal("Bunny").__healthy)
    print(a_bird.get_healthy())
    print(Animal("Bunny").get_healthy())
    '''

    """
    # Initialize an animal
    an_animal = Animal("Bunny")
    # Make the animal speak
    an_animal.speak()
    '''
    #6a
    # Make the animal sleep 
    an_animal.sleep()
    # Make the animal eat a carrot
    an_animal.eat("carrot")
    '''
    #6c
    # Make the animal eat a carrot
    an_animal.eat("carrot")
    # Make the animal sleep 
    an_animal.sleep()

    #8
    # Initialize a bird
    a_bird = Bird("Big Bird")
    # Make the bird speak
    a_bird.fly()

    #11
    # Make the bird sleep
    a_bird.sleep()

    #15 attempt to make an animal fly
    #an_animal.fly() # This will throw an error because the animal class does not have a fly method
    
    #20
    # Make the bird speak
    a_bird.speak()

    #26
    # print the nest location of the bird
    print(a_bird.nest_location)
    """



if __name__ == "__main__":
    run()