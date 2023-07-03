int_array = [1,2,3,56,7]

target = 9


def two_sum_bruteforce(int_array):
    for i in range(len(int_array)):
        for j in range(len(int_array)):
            if int_array[i]+ int_array[j] == target:
                return [i,j]
    return "no sum found"

print(two_sum_bruteforce(int_array=int_array))

def twoSum(int_array):
    hash_map = {}
    for i in range(len(int_array)):
        if int_array[i] in hash_map: # checking if difference value in hashmap is the number
            return [i,hash_map[int_array[i]]]
        else:
            hash_map[target - int_array[i]] = i # storing the difference in a hashmap
print(twoSum(int_array))

