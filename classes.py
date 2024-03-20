class Person:
    def set_details(self):
        self.name = "John"
        self.age = 20

    def display(self):
        print("i am a person",self)

    def greet(self):
        print("hello how are you doing", self)




    p1 = Person()
    p1.set_details()
    p1.display()
    p1.greet()
