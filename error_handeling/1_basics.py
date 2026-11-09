# # Handeling errors in python gracefully without stopping the execution of a programs


# # try:
# #     a = 10
# #     a = b
# # except:
# #     print("The variable has not been assigned")


# try:
#     a = 10
#     a = b
# except NameError as ex:
#     print(ex)


try:
    num1 = int(input("Plese give me a number for divident\n"))
    num2 = int(input("please give me a number as a divisor\n"))

    result = num1 / num2


except ZeroDivisionError as ex:
    print(ex)
except ValueError as ex:
    print("Please provide only integer values")
else:
    # This block will run  after the execution of try block
    print(f"The result of {num1} divided by {num2} is {result}")
finally:
    # Runs ALWAYS (cleanup phase)
    print("This block will always run no matter what ")
