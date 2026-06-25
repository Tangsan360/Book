import math
# constant = math.pi
# number_of_digits = (int("6")-1)
# print(f"we have {constant:.{number_of_digits}f} as the answer")

# constant_1 = math.e
# digits = int("8")-1
# print(f"euler's number has been evaluated to {constant_1 :.{digits}f}")

fibonacci_sequence = []
numbers = [x for x in range(10)]

def fibonacci() :
    for i in numbers:
        if numbers[i] < numbers[2] :
            # numbers[0] = 0
            fibonacci_sequence.append(numbers[i])
            # print(fibonacci_sequence)
            # numbers[1] = 1
            # fibonacci_sequence.append(numbers[1])         
        elif numbers[i] >= numbers[2] :
            numbers[i] = numbers[i-1] + numbers[i-2]
            fibonacci_sequence.append(numbers[i])
print(fibonacci())
for i in fibonacci_sequence:
    print(i, end= ",")

    


    
         
        

