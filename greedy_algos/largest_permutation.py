def permutation_swaps(array, swaps):
    # find the largest permutation possible.
    # swapping two numbers in an array to get a large number
    
    # going through left half of the array and if a number on the right side is larger, then swap it
    
    # keep highest elements in descending order on the left
    
    # have numbers in descending order for the number of swaps
    
    # https://www.interviewbit.com/problems/largest-permutation/
    
    i = 0
    
    _max = len(array) #
    d = {x: i for i, x in enumerate(array)} 
        # dictionary of the value and the position x in the array
    
    
    while swaps and i < len(array):
        j = d[_max] # index of the highest value in the array, hgihest element in len 5 is 5, len 3 is 3
        
        if i == j: # is the largest value in the right position (as far to left as possible)
            pass
        else:
            swaps -= 1 # using a swap
            array[i], array[j] = array[j], array[i] # swapping the values
            d[array[i]], d[array[j]] = d[array[j]], d[array[i]] # swapping spots in the dictionary for the position:value
            
        i += 1 # increasing index
        _max -= 1 # keeping track of max element left in the array
        
    return array