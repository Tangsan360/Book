# def total(*args):
#     result=0
#     for arg in args:
#         result+=arg
#     return result

# print(total(1,2,3,4,5))

# def students(**kwargs):
#     for key,value in kwargs.items():
#         print(f"the items are {key}:{value}")

# students(name="Kelvin",age=11,hobby="eating")


# def add_contact(l,name,number):

# l={"Alic_e":"0241234567",
# "Bobrsiky":"0559876543",
# "Charlie0chap" :  "201112233"}
# def add_contact(l,name,number):
#     new_phonebook={name:number}
#     if name in phonebook.keys():
#         print("Contact already exists")
#     else:
#         phonebook.update(new_phonebook)
#         print(phonebook)
    

    

# completed=add_contact(phonebook,"Frank","0208700745")
# print("for default ->", completed)
# completedu=add_contact(l,"Frank","0208700745")
# print("test with l ->", completedu)
# done=add_contact(phonebook,"Bob","0559876543")
# print(done)

# def greet(name):
#     print(f"Hello {name}")

# morning=greet("Bob")
# print(morning)

# day="Monday"
# position=day.find("r")
# print(position)

# Ama="You are so beautiful"
# print(Ama.replace("so","very"))
# name="Henry AppiaH"
# # print(name.rstrip("H"))
# print(name.split("H"))
# def greet():
#     language=""
#     def presence():
#         nonlocal language
#         language="Englsih"
#     presence()
#     print(language)
#     return language

# greeting=greet()
# # print(greet())
# user_answers=["Yes","","No","","Maybe","","Yes"]

    

# print(list(filter(lambda answers:answers!="",user_answers
# class Mathematics :
#     def __init__(self,total_students,vision):
#         self.total_students=total_students
#         self.vision=vision
#     def performance(self):
#         print("Excellent")    
# program = Mathematics(2300,"Discipline")
# print(program.vision)
# print(program.performance())
# print(bool(""))
# class CBAS(Mathematics):
#     def grade(self):
#         print("not bad")

# college=CBAS(2300,"Discipline")
# print(college.total_students)
# print(college.grade())
# print(college.performance())
# name= "Kyrie asare Bediako"
# print(name)
# print(name.split("a",2))


# items=[2,3,4,5,6,7]
# for index,item in enumerate(items):
#     print(f'{item}:{index}')

# class animal:
#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed
#     def sound(self):
#         print(f'The sound made by animal')

# class Dog(animal):
#     def __init__(self,name,breed,color):
#         super().__init__(name,breed)
       
#         self._color = color
#     def sound(self):
#         super().sound()
#         print("Wooof!")

# my_dog = Dog("Bruno","German Sheperd","Black")
# print(my_dog._color)
# print(my_dog.sound())


# sentence = "it\'s a good day to sleep right?"
# print(sentence)
# def shop_items(**kwargs):
#     for key,value in kwargs.items() :
#         print(key,value)
#     return kwargs

# print(shop_items(name="Kofi",age=15,occupation= "Python Programmer"))
class student :
    def __init__(self,college,course):
        self.college = college
        self.course = course
        def method():
            print(f"you can only offer {course}")
    
class individual(student):
    def __init__(self,name,age,college,course):
        super.__init__(college,course)
        self.name = name
        self.age = age

        







    




    


    