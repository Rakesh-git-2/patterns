# to calculate shortest sub array where its sum is greater than k 

k = 0
array = [1,2,3,4,5,6]

min_length = float('inf')

initial_sum = [array[0]]
current_sum = 0 
start = 0 
end = 0 

while end < len(array):
    current_sum = current_sum + array[end]
    end = end + 1

    while start<end and current_sum >= k : # start<end is to handle k = 0 case
        current_sum = current_sum - array[start]
        start = start + 1

        min_length = min(min_length,end-start+1)

print(min_length)

        