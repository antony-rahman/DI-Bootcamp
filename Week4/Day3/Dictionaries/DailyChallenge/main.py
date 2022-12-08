# challenge 1:

from itertools import product


string = input("give me a word:")

user_dictionary = {}

for i in range(len(string)):
    if string[i] not in user_dictionary:
        user_dictionary[string[i]] = [i]
    else:
        user_dictionary[string[i]].append(i)

print(user_dictionary)



# challenge 2:

items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"

print(int(wallet.strip('$')))

basket = []

for product, value in items_purchase.items:

    value_format = value.strip('$')
    value_format = value_format.replace(',','')

    if int(value_format) < wallet.format:
        basket.append(product)

print(basket)