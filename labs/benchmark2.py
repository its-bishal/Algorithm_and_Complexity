
import time
import matplotlib.pyplot as plt

from sort_algo import insertion_sort, merge_sort


def plot_curve():

    data_size = []
    insertion_exec_time = []
    merge_exec_time = []

    for i in range(1000, 10001, 250):

        input_val = list(range(1, i+1))
        # input_val = list(reversed(range(1, i+1)))
        data_size.append(i)

        start_time = time.time_ns()
        insertion_sort(input_val)
        end_time = time.time_ns()
        each_time1 = end_time - start_time
        insertion_exec_time.append(each_time1)
        
        start_time = time.time_ns()
        merge_sort(input_val, 0, len(input_val)-1)
        end_time = time.time_ns()
        each_time2 = end_time - start_time
        merge_exec_time.append(each_time2)


    plt.figure(figsize=(6,6))
    plt.title(f'time complexity')
    plt.xlabel('size of data')
    plt.ylabel('time complexity')
    plt.plot(data_size, insertion_exec_time, label='InsertionSort')
    plt.plot(data_size, merge_exec_time, label='MergeSort')
    plt.legend()
    plt.show()


if __name__=="__main__":
    plot_curve()
