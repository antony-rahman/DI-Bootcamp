matrix = """    7i3
    Tsi
    h%x
    i #
    sM
    $a
    #t%
    ^r!"""

result = []

matrix_arr = [list(item[4:8]) for item in matrix.split("\n")]

for col in range(len(matrix_arr[0])):
    for row in range(len(matrix_arr)):
        symbol = matrix_arr[row][col]
        if symbol.isalpha():
            result.append(symbol)
            continue
        matrix_arr[row][col] = " "
result = "".join(result)

print(matrix_arr)
print(result)