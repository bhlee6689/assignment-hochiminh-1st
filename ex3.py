def calculator():
    while True:
        operation = int(input(
            "Please select operation ₩n 1.Add ₩n 2. Subtract ₩n 3. Multiply ₩n 4. Divide ₩n₩n Select Operations from 1,2,3,4:"))
        if operation == 1:
            print("You chose add cal")
            firstNum = int(input('Enter the first num: '))
            secondNum = int(input('Enter the second num: '))
            result = firstNum + secondNum
            print('The result is %f' % result)

        elif operation == 2:
            print("You chose subtraction cal")
            firstNum = int(input('Enter the first num: '))
            secondNum = int(input('Enter the second num: '))
            result = firstNum - secondNum
            print('The result is %f' % result)

        elif operation == 3:
            print("You chose multiplication cal")
            firstNum = int(input('Enter the first num: '))
            secondNum = int(input('Enter the second num: '))
            result = firstNum * secondNum
            print('The result is %f' % result)

        elif operation == 4:
            print("You chose division cal")
            firstNum = int(input('Enter the first num: '))
            secondNum = int(input('Enter the second num: '))
            result = firstNum / secondNum
            print('The result is %f' % result)

        else:
            print("You typed wrong number! Please choose the number from 1 to 4.")


calculator()
