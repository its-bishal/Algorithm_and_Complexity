
import math

def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
        
            return i
        print(values)
        
    return -1


def binary_search(values,start, end, target):
    if(end >= start):
        mid = math.floor((start+end)/2)
        if values[mid] == target:
            return mid
        elif values[mid] > target:
            return binary_search(values, start, mid-1, target)
        else:
            return binary_search(values, mid+1, end, target)
    return -1
    

li_values = [4,7,2,9,3,8,4,0]
print(f"9 is at index {linear_search(li_values, 9)}")

bi_values = [6,7,9,11,13,17,19,23,29]
print(f"13 is at index {binary_search(bi_values, 0, 8, 13)}")