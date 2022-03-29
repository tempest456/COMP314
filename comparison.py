"""Insertion Sort vs Merge Sort"""
from insertion_sort import insertion_sort
from merge_sort import merge_sort
import random
import time
import matplotlib.pyplot as plt

# (x1, y1) for Insertion Sort and (x2, y2) for Merge Sort
x1axis = []
y1axis = []
x2axis = []
y2axis = []
for size in range(1000, 11000, 2000):
    x1axis.append(size)
    x2axis.append(size)
    start1 = time.time_ns()
    insertion_sort(random.sample(range(1, 10000), size))
    end1 = time.time_ns()
    time_taken1 = end1-start1
    y1axis.append(time_taken1)
    start2 = time.time_ns()
    merge_sort(random.sample(range(1, 10000), size))
    end2 = time.time_ns()
    time_taken2 = end2-start2
    y2axis.append(time_taken2)


plt.plot(x1axis, y1axis, label = "Insertion Sort")
plt.plot(x2axis, y2axis, label = "Merge Sort")
plt.xlabel('Input Size(n)')
plt.ylabel('Time(ns)')
plt.title("Insertion Sort vs Merge Sort Time Complexity")
plt.legend()
plt.show()

