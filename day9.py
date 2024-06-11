## <<< FUNCTIONS >>>>>>  

# def add():
#     num1 = 10
#     num2 = 20 
#     output = num1 + num2 
#     return output 


# call function 
# print(add())
# output = add()
# print(output)



# def add(num1 , num2):   # parameters
#     output = num1 + num2 
#     return output 



# output = add(25,30)  # positional arguments 
# print(output)

# output = add(num1=25,num2=25)
# print(output)
#modularity 

# print(add(num1=25,num2=25))
# print(add(num1=50,num2=50))
# print(add(num1=500,num2=500))
# print(add(num1=5000,num2=5000))
# print(add(num1=250,num2=250))
# print(add(num1=258,num2=258))





# output = square(num=2)  
# print(output)



# ls = [52,41,63,96,85,74,85,2,41,42,62,35,25,15,42]
# print(len(ls))
# count = 0
# for item in ls:
#     count += 1
# print(count)







### create function
# def apna_len(ls):
#     count = 0
#     for item in ls:
#         count += 1
#     print(count)


# calling 
# lst = [52,41,63,96,25,74]
# apna_len(ls=lst)  # apna_len


# print()
# print(len(lst))

# lst = [85,96,45,12,63,45,85,96,25,41,63,85,74,95,15,25]
# print(len(lst))

# def apna_len(ls):
#     count = 0
#     for item in ls:
#         count = count + 1
#     return count

# calling function "apna_len"
# output = apna_len(lst)
# print(output)

# total even no. 




def count_even(ls):
    count = 0
    for item in ls:
        if item % 2 == 0:
            #even
            print(item)
            count = count + 1
    return count 

lst = [74,96,85,42,51,86,95,45]
output = count_even(ls=lst)
print("Total no. of even : ",output)



# lst = [74,96,85,42,51,86,95,45,85,96,3,42,61,45,35,42,75,65,55,85]
# 1. wap to create a function called "number_filter" ,to filter out the
#     number in between 50 to 80.

# 2. "number_filter" program should be able to return no. of item that are present
#     in between 50 to  100. 


# lst = [25,41,25.25,63.2,12,42,85,'upflairs','ibm',True , 25,14,"celebel"]
# 1. create a function to count only the integer data item in a given list.
# 2. create a function to count only the string data item in a given list.









        
         
