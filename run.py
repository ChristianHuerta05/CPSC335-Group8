from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quicksort
from radix_sort import RadixSort
from linear_search import linear_search
import tracemalloc
import time

def run(function_options, input_list):
    data = []
    # Cast the input list to a list of integers
    try:
        data = [int(x) for x in input_list.split(', ')]
    except ValueError:
        # Handle invalid input
        print("Invalid input")
        pass
    
    times = {"Merge_Sort": 0, "Bubble_Sort": 0, "Quick_Sort": 0, "Radix_Sort": 0, "Linear_Search": 0}

    if function_options.get("Merge_Sort"):
        # start tracking time and memory
        tracemalloc.clear_traces() 
        tracemalloc.start()
        start = time.perf_counter()
        merge_sort(data.copy()) 
        
        # stop tracking time 
        end = time.perf_counter()
        
        # from the tracemalloc get back the top memory usage and current usage which is not needed
        curr, top = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Convert bytes to KB for memory usage
        times["Merge_Sort"] = [end - start, top / 1024]  

    if function_options.get("Bubble_Sort"):
        # start tracking time and memory
        tracemalloc.clear_traces() 
        tracemalloc.start()
        start = time.perf_counter()
        bubble_sort(data.copy())
        
        # stop tracking time 
        end = time.perf_counter()
        
        # from the tracemalloc get back the top memory usage and current usage which is not needed
        curr, top = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        times["Bubble_Sort"] = [end - start, top / 1024]

    if function_options.get("Quick_Sort"):
        # start tracking time and memory
        tracemalloc.clear_traces() 
        tracemalloc.start()
        start = time.perf_counter()
        
        try:
            quicksort(data.copy())
        except RecursionError:
            # stop tracking due to recursion being too deep on large amounts of data
            end = time.perf_counter()
            curr, top = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            times["Quick_Sort"] = ["RecursionError", top / 1024]
            return times  
        
        # stop tracking time 
        end = time.perf_counter()
        curr, top = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        times["Quick_Sort"] = [end - start, top / 1024]

    if function_options.get("Radix_Sort"):
        # start tracking time and memory
        tracemalloc.clear_traces() 
        tracemalloc.start()
        start = time.perf_counter()
        
        RadixSort(data.copy())
        
        # stop tracking time and memory
        end = time.perf_counter()
        curr, top = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        times["Radix_Sort"] = [end - start, top / 1024]
        
    if function_options.get("Linear_Search"):
        # start tracking time and memory
        tracemalloc.clear_traces() 
        tracemalloc.start()
        start = time.perf_counter()
        linear_search(data.copy(), 101)
        
        # stop tracking time and memory
        end = time.perf_counter()
        curr, top = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        times["Linear_Search"] = [end - start, top / 1024]

    return times