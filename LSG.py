"""Generating input-size vs execution Graph for Linear Search Algorithm. """
from LinearSearch import LinearSearch
import time
import matplotlib.pyplot as plt

# (x1, y1) for Best Case and (x2, y2) for Worst Case
x1axis = []
y1axis = []
x2axis = []
y2axis = []
for size in range(10000, 110000, 10000):
    x1axis.append(size)
    x2axis.append(size)
    start1 = time.time()
    LinearSearch(list(range(size)), 0) # 0 is the first element in the list.
    end1 = time.time()
    time_taken1 = "%.2f" % (end1-start1)
    y1axis.append(time_taken1)
    start2 = time.time()
    LinearSearch(list(range(size)), -100) # -100 is not in the list.
    end2 = time.time()
    time_taken2 = "%.3f" % (end2-start2)
    y2axis.append(time_taken2)


plt.plot(x1axis, y1axis, label = "Best Case")
plt.plot(x2axis, y2axis, label = "Worst Case")
plt.xlabel('Input Size(n)')
plt.ylabel('Time(s)')
plt.title("Linear Search: Best vs Worst Case Time Complexity")
plt.legend()
plt.show()
    


