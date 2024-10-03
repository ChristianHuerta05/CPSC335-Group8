from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quicksort
from radix_sort import RadixSort
import time


def run(function_options, input_list):
    data = [3,2,1,4,5,2,1,5,3,2]
    # Cast the input list to a list of integers
    try:
        data = [int(x) for x in input_list.split(', ')]
    except ValueError:
        # Handle invalid input
        print("Invalid input")
        pass
    times = {"Merge_Sort":0,"Bubble_Sort":0,"Quick_Sort":0, "Radix_Sort": 0}
    print(function_options)
    if(function_options["Merge_Sort"] == True ):
        start = time.perf_counter()
        merge_sort(data)
        end = time.perf_counter()
        times["Merge_Sort"] = end-start
    if(function_options["Bubble_Sort"] == True):
        start = time.perf_counter()
        bubble_sort(data)
        end = time.perf_counter()
        times["Bubble_Sort"] = end-start
    if(function_options["Quick_Sort"] == True):
        start = time.perf_counter()
        quicksort(data)
        end = time.perf_counter()
        times["Quick_Sort"] = end-start
    if(function_options["Radix_Sort"] == True):
        start = time.perf_counter()
        RadixSort(data)
        end = time.perf_counter()
        times["Radix_Sort"] = end-start
        
    return times