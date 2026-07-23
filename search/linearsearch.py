import time
l=[i for i in range(10000)]


def search(x):
    start=time.perf_counter()
    for i in l:
        if i==x:
            print(i)
            break
    end=time.perf_counter()
    print("Time taken=",end-start)
search(10)