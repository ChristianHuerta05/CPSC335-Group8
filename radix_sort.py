# Radix Sort 
def RadixSort(array):
    
    def CountSort(array, digit):
        size = len(array)
        NewArray = [0] * size
        count = [0] * 10
        
        for i in range(0 , size):
            index = array[i] // digit
            count[index % 10] += 1
            
        for i in range(1 , 10):
            count[i] += count[i-1]
        
        #sort the element    
        i = size-1
        while i >= 0:
            index = array[i] // digit
            NewArray[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1
            
        for i in range(0 , size):
            array[i] = NewArray[i]
    
            
    # Find maximum element in the array
    maxNum = max(array)

    # Call the function CountSort to sort the elements in the array
    digit = 1
    while maxNum // digit > 0:
        CountSort(array , digit)
        digit *= 10