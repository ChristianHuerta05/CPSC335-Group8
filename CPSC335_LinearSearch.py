def linear_search(L, T):
    for index, element in enumerate(L):
        if element == T:
            return index
    return -1

# Input Data
L = [101, 1, 4, 5, 2, 4, 100, 76]
T = 123
print(linear_search(L,T))
