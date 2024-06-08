name = input("Plz enter your name : ")
print("Hello ", name )

message = """
How may i help you sir ?
Type 1 ---> Check balance
Type 2 ---> Deposit balance
Type 3 ---> withdrawl
"""
print(message)
current_available_amount = 5000 
task = int(input("Plz enter your task : "))

if task >=1 and task <=3:
    # operation perform
    print("your welcome in upflairs bank !") 

    # check balance  1
    if task == 1:
        print("Your available balance is INR : ",current_available_amount) 

    # deposit balance 2 
    elif task == 2:
        deposit_amount = int(input("Plz enter deposit amount : "))
        if deposit_amount >= 500 : 
            current_available_amount += deposit_amount 
            print("you have successfully deposite your amount : ",deposit_amount)
            print("Your available balance is INR : ",current_available_amount) 
            


        else:
            print('Plz enter above 500 rupess amount !')    


    # withdrawl balance 3
    else:
        withdrawl_amount = int(input("Plz enter withdrawl amount : "))
        if withdrawl_amount >=0 and  withdrawl_amount <= current_available_amount:
            current_available_amount -= withdrawl_amount
            print("You have successfully withdrawl your amount : ",withdrawl_amount)
            print("Your available balance is INR : ",current_available_amount) 


        else:
            print("Plz enter suffiecient amount !")



else:
    print('Plz enter in between 1 to 3 !')