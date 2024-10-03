# linear search
#Input: List of numbers to be sorted (L) and target number (T)
def linear_search(L, T):
    for index, element in enumerate(L):
        if element == T:
            return index
    return -1