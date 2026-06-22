# # Question 1
# age = input(f"what is your age ?")
# n_age = int(age)
# if n_age <= 10 :
#     print("child")
# elif 10 < n_age <= 19 :
#     print("teen")
# else :
#     print("adult")

# # Question 3
# enter_password = input(f"what is your password")
# password = "apple360"
# if enter_password == password :
#     print(f"access granted")
# else :
#     print(f"wrong password")

# Question 4 
# multiples = [x for x in range(1,13)]
# n = input(f"any number")
# number = int(n)
# for multiple in multiples :
#     answer = multiple * number
#     print(answer)

# # Question 5
# secret_number = 11
# user_answer = input("guess the number")
# guessed_number = int(user_answer)

# if guessed_number != secret_number :
#     print(f"keep on guessing")
# else :
#     print("correct")

# Question 6
# numbers = [x for x in range(1,101)]
# addition = sum(numbers)
# print(addition)
# when "n"
# ending_number = "n"
# integer = int(ending_number)
# numbers = [x for x in range(1,integer + 1)]
# addition = sum(numbers)
# print(addition)

# Question 7
# sentence = f"I am going to school"
# vowels = {1:"A",2:"E",3:"I",4:"O",5:"U",6:"a",7:"e",8:"i",9:"o",10:"u"}
# empty_result = []
# for i in sentence :
#     if i in vowels.values() :
#         print(i)   
#         empty_result.append(i)

# print(empty_result)

# number_of_vowels = len(empty_result)
# print(number_of_vowels)

# Question 8
# array = [1,2,7,5,8,9,2]
# # order = sorted(array)
# # array.sort()
# # print(array)
# largest_number = max(array)
# print(largest_number)

# cars = {"Economy":10,"SUV":20,"Luxury":30}
# request = input("SUV")
# cost_per_day_in_dollars = 200
# number_of_days = 14

# def car_rental_system(request) :
#     if request in cars.keys() :        
#         total_cost = number_of_days * cost_per_day_in_dollars
#         print(total_cost)
#         print(f"you have {number_of_days} days to hand over the car")
#         final_decision = input("yes")
#         if final_decision == "yes" :
#             # number_of_cars = cars.get(request)
#             # number_of_cars -= 1
#             cars[request] -= 1
#         else :
#             print(f"Thank you")
#     else :
#         print(f"car not found")
     


# result = car_rental_system("SUV")
# print(result)

# print(cars["SUV"])
# a = [1,2]
# b = [1,2]
# print(a==b) true bcoz python checks for equality
# print(a is b) false bcoz pyhton checks for memory location


    




         
    
