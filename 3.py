def solve(arr, result):
    from itertools import chain, permutations
    from string import digits

    letters = ''.join(set(chain(result, *arr)))
    initial_letters = ''.join(set(chain(result[0], (a[0] for a in arr))))
    solutions_found = False
    for perm in permutations(digits, len(letters)):
        decipher_table = str.maketrans(letters, ''.join(perm))
        def decipher(s):
            return s.translate(decipher_table)
        deciphered_sum = sum(int(decipher(code)) for code in arr)
        if deciphered_sum == int(decipher(result)):
            print("---------------------------------------------------------")
            print(str(arr[0]) + "  " + str(decipher(arr[0])))
            print(str(arr[1]) + "  " + str(decipher(arr[1])))
            print(str(result) + "  " + str(decipher(result)))
            print("---------------------------------------------------------")
            solutions_found = True
    if not solutions_found:
        print(" + ".join(arr), "=", result, " : no solution")

array_size = int(input("Enter the number of elements in the array: "))
array = []
for i in range(array_size):
    element = input("Enter element " + str(i+1) + ": ")
    array.append(element)
result = input("Enter the result: ")

solve(array, result)


# solve (array, result)
