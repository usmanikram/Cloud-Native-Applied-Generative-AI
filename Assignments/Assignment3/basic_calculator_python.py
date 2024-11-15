#Python Basic Calculator

first_number = input("Enter First Number:")

second_number = input("Enter Second Number:")

operation = input("Enter operation (+ , - , * , / ):")

first_number = int(first_number)

second_number = int(second_number)


match operation:
    case "+":
        result = first_number + second_number

    case "-":
        result = first_number - second_number

    case "*":
        result = first_number * second_number

    case "/":
        result = first_number / second_number
    

print("The result is: {}" . format(result))