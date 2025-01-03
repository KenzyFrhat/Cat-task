# initialization
num = 0
# inputs
operations = input("Enter the increment and decrement operations (separated with spaces) : ").strip().split(' ')
# validation
operations = [operation.strip() for operation in operations]
is_valid_inputs = all([operation =='++' or operation == '--' for operation  in operations])
if not is_valid_inputs :
    print("invalid inputs! ")
#     process
else:
    for operation in operations:
        if operation == "++":
            num += 1
        else:
            num -= 1
    print(f"The result is {num}")
