
def count_sort(arr):

    max_v = int(max(arr))
    min_v = int(min(arr))

    elem_range = max_v-min_v + 1

    count_arr = [ 0 for _ in range(elem_range)]
    output_arr = [0 for _ in range(len(arr))]

    # store count of each char
    for i in range(len(arr)):
        count_arr[arr[i]-min_v] += 1
    
    # store actual position in output arr
    for i in range(len(count_arr)-1):
        count_arr[i+1] += count_arr[i]
    # build output arr
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i]-min_v]-1] = arr[i]
        count_arr[arr[i]-min_v] -= 1

    return output_arr

new = [-5, -10, 0, -3, 8, 5, -1, 10]
print(count_sort(new))

# implementation of count array?
