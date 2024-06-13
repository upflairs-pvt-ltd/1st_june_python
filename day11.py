# try:
#     name = input("Plz enter your name : ")
#     age = int(input("plz enter your age : "))
#     print("Hii i am ",name," and i am ",age,"year old")
    
# except:
#     print("Error is occured but plz dont stop the program execution")

# else:
#     print("error is not occured !")

# finally:
#     print("Hiii i am from finally!")
# print("plz execute me, i am very impotant")







# 1. wrong input by data types  --> ValueError:
# 2. num2 passed as zero   --> ZeroDivisionError:


# try:
#     num1 = int(input("enter first number : "))
#     num2 = int(input("enter second number : ")) 

#     output = num1 / num2
#     print(output)
# except ValueError:
#     print("Plz enter valid input in the program!")

# except ZeroDivisionError:
#     print("Plz dont enter zero in the second number!")

# finally:
#     print("plz execute me, i am very impotant")





# num1 = int(input("enter first number : "))
# num2 = int(input("enter second number : ")) 

# output = num1 / num2
# print(output)


# SyntaxError
# TypeError
# NameError
# IndexError
# KeyError
# ValueError
# ZeroDivisionError
# Indentation Error




ls = [7466,55,44,77,88,9,6,75,95,45,22,11,333,52,63,96,3]

try:
    num = int(input("Input your target number : "))
    position = 0 
    for item in ls:
        if item == num:
            print('position : ',position)
        position += 1
except ValueError:
    print("plz enter valid input!")

finally:
    print('hey i am finding your target element position!')

