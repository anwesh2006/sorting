import time
import random

def performance_test(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())
    end_time = time.time()
    return end_time - start_time

# Generate a large random array
arr = [random.randint(1, 1000) for _ in range(10000)]

# Test each sorting algorithm
bubble_time = performance_test(bubble_sort, arr)
quick_time = performance_test(quick_sort, arr)
merge_time = performance_test(merge_sort, arr)

print(f"Bubble Sort: {bubble_time:.4f} seconds")
print(f"Quick Sort: {quick_time:.4f} seconds")
print(f"Merge Sort: {merge_time:.4f} seconds")
