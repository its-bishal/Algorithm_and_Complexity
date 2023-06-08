# bubble sort

def bubble(unsorted):
    for i in range(len(unsorted)-1):
        for j in range(len(unsorted)-i-1):
            if unsorted[j]>unsorted[j+1]:
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
    print(unsorted)


check = [1,5,2,45,8,9,5,4,90]

# selection sort
def selection(unsorted):
    for i in range(len(unsorted)):
        min_index=i
        for j in range(i+1, len(unsorted)):
            if unsorted[min_index]>unsorted[j]:
                min_index=j
            
        unsorted[min_index], unsorted[i] = unsorted[i], unsorted[min_index]

    print(unsorted)


# insertion sort


# bucket sort

# merge sort

# quick sort

# heap sort