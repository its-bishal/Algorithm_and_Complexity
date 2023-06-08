import numpy as np
import matplotlib.pyplot as plt
import time


from search_algo import linear_search, binary_search

def curve(algorithm, data_size, exec_time):
    plt.figure(figsize=(7,7))
    plt.title(f'search complexity for {algorithm}')
    plt.xlabel('size of the data')
    plt.ylabel('execution time')
    plt.plot(data_size, exec_time)
    plt.show()


def performance(algorithm, target, obs_no, size=11):

    assert algorithm in ['linear-search', 'binary-search']
    data_size=[]
    exec_time=[]

    for i in range(1, obs_no):
        data = int(3.14*i)
        data_size.append(data)

        if algorithm == 'linear-search':
            values = np.random.randint(1, size, data)
            
            start_time = time.time()
            linear_search(values=values, target=target)
            end_time = time.time()

        elif algorithm == 'binary-search':
            values = list(range(1,data+1))
        
            start_time = time.time()
            binary_search(values=values, start=0, end=data, target=target)
            end_time = time.time()

        exex_time = end_time-start_time
        exec_time.append(exex_time)

    curve(algorithm=algorithm, data_size=data_size, exec_time=exec_time)


obs_no=20
performance(algorithm='linear-search', target = -1, obs_no=obs_no, size=100)
performance(algorithm='binary-search', target = -1, obs_no=obs_no)

