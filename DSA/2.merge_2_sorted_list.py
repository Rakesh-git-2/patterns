a = [1,2,3,4,7,90,100,177]
b = [1,3,44,66,99]


def merge_sorted_list(l1,l2):
    result = []
    pointer1 = 0
    pointer2 = 0
    for i in range(len(l1)+len(l2)):
        if pointer1 >= len(a):
            result.extend(l2[pointer2:len(b)])
            return result
        if pointer2 >= len(b):
            result.extend(l1[pointer1:len(a)])
            return result
        if l1[pointer1] <= l2[pointer2]:
            result.append(l1[pointer1])
            pointer1 += 1
        else :
            result.append(l2[pointer2])
            pointer2 += 1
    return result


print(merge_sorted_list(a,b))