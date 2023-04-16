
class User:
    def __init__(self, age) -> None:
        self.age = age


def test_user_age_is_42():
    user = User(42)

    assert user.age == 42 



class Auto:
    x = "Testcase"

p1 = Auto()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John" , 36)

print(p1.name)
print(p1.age)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name, + self.age)

p1 = Person("John", 36)
p1.myfunc()




class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def baik(self):
        print("Woof!")

    def fetch(self):
        print("I can fetch!")

my_dog = Dog("Buddy", "Labrador")


print("Name: ", my_dog.name)
print("Breed: ", my_dog.breed)


def foo():
    pass

    