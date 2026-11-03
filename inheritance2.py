class Animal:
     def speak(self):
        print("Animal speaks")

class Dog(Animal):
     def speak(self):
         print("Dog berks")

dog=Dog()
dog.speak()

animal=Animal()
animal.speak()