# Calculate sum of sub arrays

array = [1,2,3,4,5,6]

subLen = 2

first_sub_array_sum = sum(array[:subLen])

result = [first_sub_array_sum]

currentSum = first_sub_array_sum


for i in range(1,len(array)-subLen+1):
    currentSum = currentSum - array[i-1] + array[i+subLen-1]
    result.append(currentSum)
    print(result)