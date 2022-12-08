# part 1
first_value = int(input("pick value:"))
first_length = int(input("pick length:"))
def multiples(value, length):
    return [value * i for i in range(1, length + 1)]
print(multiples(first_value, first_length))


# part 2
user_word = set(input("enter:"))
print(user_word).replace(',', '')