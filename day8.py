# st = "upflairs"
# ls = [85,96,74,85,963,31,52]


# for i in ls:
#     print(i)


# ls = [87,96,74,85,963,31,52]

# if 85 in ls:
#     print('yes present')
# else:
#     print('not present')


# ls = [85,96,74,85,963,31,52]
# print(len(ls))

# for item in ls:
#     if item == 85:
#         print('present')

# count = 0 
# for item in ls:
#     count = count + 1

# print(count)  

# initialization 
# while (condition):
#     block of code 
#     incrementing 


# i = 0 
# while i <=50:

    # if i == 25:
    #     break
#     if i == 25:
#         continue

#     print("hello world " , i )
#     i = i + 1

# print('Hii from outside the loop !')


# for i in range(20):
#     if i ==10:
#         continue  
#     print(i)
    
# break execution end 
# continue only current iteration stop  


# ls = [41,52,63,96,74,45,69,85,75,42,62,5]
# count = 0  
# for item in ls:
#     if item == 85:
#         print(count)
#         break 
#     count +=1


# num1 = 44
# if num1 % 2 == 0:     # 0 != 0
#     print("even")
# else:
#     print('odd')




ls = [41,52,63,96,74,45,69,85,75,42,62,5,896,456,74]
even  = []
odd = []
even_no = 0 
odd_no = 0
for item in ls:
    if item % 2 == 0:
        even_no += 1
        even.append(item)
    else:
        odd_no += 1
        odd.append(item)

print("Total even no. : ",even_no)
print("Total odd no : ",odd_no)
print()
print("Even no. : ",even)
print("odd no. : ",odd)

