# Function is block of code that is run when its called()

# def is for define
# IndentationError
# formatFile in vscode

def sayHello(name='daniel'):
    print('Hello ' + name)


# don't forget to call the function
sayHello()
sayHello('Beth')

# return value


def getSum(num1, num2):
    total = num1 + num2
    return total

# print(total)


numSum = getSum(4, 3)
print(numSum)


def addOneToNum(num):
    num = num + 1
    num += 1
    return num


num = 5
new_num = addOneToNum(num)

print('new_num')  # 6


# lambda function is a small anonymous function.
def getSum(num1, num2): return num1 + num2


print(getSum(9, 2))


def getAdd1(num): return num + 1


print(getAdd1(2))
