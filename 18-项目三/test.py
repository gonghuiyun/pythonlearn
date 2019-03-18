def twoSum(numbers, target):
    i = 0
    j = len(numbers)-1-i
    while not i == j:
        if numbers[i] + numbers[j] <target:
            i = i+1
        elif numbers[i] + numbers[j] >target:
            j = j-1
        else:
            return [i + 1, j + 1]

print(twoSum([2,7,11,15],9))

