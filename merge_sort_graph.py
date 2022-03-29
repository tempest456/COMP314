from merge_sort import merge_sort
import random
import time
import matplotlib.pyplot as plt

xaxis = []
yaxis = []

for size in range(1000, 11000, 2000):
    xaxis.append(size)
    start = time.time_ns()
    merge_sort(random.sample(range(1, 10000), size))
    end = time.time_ns()
    time_taken = (end-start)
    yaxis.append(time_taken)
    
plt.plot(xaxis, yaxis, label = "Merge Sort")
plt.xlabel('Input Size(n)')
plt.ylabel('Time(ns)')
plt.title('Merge Sort Time Complexity')
plt.show()

