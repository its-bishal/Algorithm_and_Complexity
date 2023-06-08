
import math

# insertion sort
def insertion_sort(custom_list):
    for i in range(1, len(custom_list)):

        key = custom_list[i]
        j = i-1
        while j >= 0 and key < custom_list[j]:
            custom_list[j+1] = custom_list[j]
            j-=1
        custom_list[j+1] = key
    return custom_list


#merge sort
def merge(custom_list, left, right, mid):
    n1 = mid - left + 1
    n2 = right - mid

    Left = [0] * n1
    Right = [0] * n2

    for i in range(0, n1):
        Left[i] = custom_list[left+i]
    
    for j in range(0, n2):
        Right[j] = custom_list[mid+1+j]

    i = j = 0
    k = left

    while i<n1 and j<n2:
        if Left[i] <= Right[j]:
            custom_list[k] = Left[i]
            i+=1

        else:
            custom_list[k] = Right[j]
            j+=1

        k+=1

    while i < n1:
        custom_list[k] = Left[i]
        i+=1
        k+=1

    while j < n2:
        custom_list[k] = Right[j]
        j+=1
        k+=1


def merge_sort(custom_list, left, right):
    if left < right:
        mid = math.floor((left + right)/2)
        merge_sort(custom_list, left, mid)
        merge_sort(custom_list, mid+1, right)
        merge(custom_list, left, right, mid)
        return custom_list
    else:
        return custom_list


# cus_list = [3,2,5,6,12,9,14,13,19,21,11]
# print(merge_sort(cus_list, 0, 10))

