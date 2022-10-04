# quick_sort.py

"""
my current understanding:

this sorting method isn't quite as intuitive as mergesort. quick sort relies on optimalish partition points. The quick_sort function is easy to understand, it just calls itself using the partition point for both the left - 1 and right + 1 sides, the partition point itself is already in the correct position. I don't really understand that.

The partition sorts elements in the range if they are less than the pivot. A pivot is chosen, ie the last number and elements less than it are sent to the left recursive call and elements greater are sent to the right recursive call. When aprtitioning


The two pointer method is hard to understand, quick sort uses less memory than mergesort because it does the sorting in place and not in each call to the call stack

The pivot/partition point is key to having this algorithm working in a O(nlogn) time rather than a O(n^2) time. If the array is already sortedish, a median partition point will be important. 

if the values are in a random order, then any partition point should be good.
"""

# explained it the best as a tree structure
# https://www.youtube.com/watch?v=XE4VP_8Y0BU

# pivot needs to rest in same place
def partition(l, low, high):
    
    # take right most element as pivot
    pivot = l[high] # right most of sub array
    # this is where heuristics come in
    
    i = low - 1 # starting index to start at
    
    # traverse through all elements in list
    # compare each element with the pivot
    
    for j in range(low, high): # iterate through elements in sub array, inclusive, exclusive
        # doesn't iterate last element because it swaps the last element there
        
        # can do high -> low to swap on opposite ends, but low -> high works because they move at different rates and keep swapping elements that are greater than the pivot
        # low -> high is less intuitive because  it has two pointers at different speeds, 
        # high -> low is intuitive because they swap and once they meet the iteration ends.
        if l[j] <= pivot: 
            # if it is less, then move it left of the pivot
            # swap it with the greater element pointed to by i
            
            i += 1 # moving over element to swap, 
            
            (l[i], l[j]) = (l[j],l[i]) # swapping the greater element to the end
            
            # because some elements are greater than the pivot the j will always iterate and i won't this leads the i to lag, the j will end up on the right and lements that are less than the pivot at j will swap with elements at index i, this leads elements to swap to the left of the pivot
            
    
    # swap pivot with greater element specified by i,
    # i was incrimented when an element was lower than the pivot, not we can insert just to the right of all elements less than the pivot
    (l[i + 1], l[high]) = (l[high], l[i + 1])
    
    return i + 1 # next partition point
    
    
def high_low_partition(l, low, high):
    i = low
    j = high
    pivot = l[high]
    
    while i < j: # so they dont cross over
        while i < high and l[i] <= pivot: # while points to the left are valid
            i += 1
            
        while j > low and l[j] > pivot: # while points to the right are valid
            j += 1
        
        # the two while statements will keep iterating until they find elements that are on the wrong side of the pivot, once found they swap them
        
        # if still validly iterating
        if i < j:
            l[i], l[j] = l[j], l[i]
            
    if l[i] > pivot:
        l[i], l[high] = l[high], l[i]
        
    return i 
    

def quick_sort(l, low, high):
    if low < high: # if still valid to switch
        
        # find pivot element so elemnt smaller than pivot are on the left
        # items greater than the pivot are on the right
        # items smaller than the pivot are on the left
        part = partition(l, low, high) # to find partition position and swap elements
        # puts partition in right spot

        # recursive call on left
        quick_sort(l,low, part - 1) 
            # dont need to include pivot because its already in the right position
        
        # recursive call on right
        quick_sort(l, part + 1, high)

# https://www.geeksforgeeks.org/python-program-for-quicksort/

 
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
 
size = len(data)
 
quick_sort(data, 0, size - 1)
 
print('Sorted Array in Ascending Order:')
print(data)