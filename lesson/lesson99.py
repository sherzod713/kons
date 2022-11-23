# class Mammal:
#     def move(self):
#         print ('двигайся')


# class Hare(Mammal):
#     def move(self):
#         print('прыгает')

# animal = Mammal()
# animal.move()
# Hare = Hare()
# Hare.move()












class car:
    def __init__(Self,brand,model,color):
     Self.brand = brand    
     Self.model=model
     Self.color = color

Mersedes = car ("Mersedes","Gla_amg", "black")

print (f'бренд машины: {Mersedes.brand} модель: {Mersedes.model} цвет: {Mersedes.color}')




# class Employee:
#     def __init__(Self,name,surname,gender, date_birth):
#      Self.name = name   
#      Self.surname = surname
#      Self.gender = gender
#      Self.date_birth = date_birth

#     def __str__(self): 
#         return f'имя: {self.name} , фамилия:{self.surname}, пол: {self.gender}, др: {self.date_birth}'

# empl = Employee("sherzod", 'muratov',"male",'27 april')
# empl2 = Employee('shshs', 'shhsdisa', 'frml', '27 april') 

# print(empl)
# print(empl2)


# class Human:
#      def__init__(self,name,age):
#      self.name =  name
#      self.age = age

# Teacher = Human 




 














class Cat:
    def __init__(self,name,preferences):
        self.name= name
        self.preferences = preferences
    def info(self):
        print(f"я кот. Меня зовут {self.name}. Мне {self.preferences} года.")
        def make_sound(self):
            print("Мяу!")
class Dog:
    def __init__(self,name,preferences):
        self.name = name
        self.preferences = preferences
    def info(self):
        print(f"Я собака. Меня зовут {self.name}. Мне {self.preferences} года.")
    def make_sound(self):
        print("гав!")
catNumber1 = Cat('Васька', 2)
dogNumber1 = Dog('Мухтар', 3)
for animal in (catNumber1, dogNumber1):
    animal.info()
    print(catNumber1)

