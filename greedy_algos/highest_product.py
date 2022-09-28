# given an array of N integers, find the highest product by multiplying 3 elements
# https://www.youtube.com/watch?v=bC7o8P_Ste4

# 2 negative and one positive returns a positive value
# highest 3 elements in sorted array
# 2 lowest and 1st highest

def max3p(arr):
    arr.sort() # sort in place, ascending
    
    high3 = arr[-1] * arr[-2] * arr[-3]
    low2high1 = arr[-1] * arr[0] * arr[1]
    
    return max(high3, low2high1)

# this solution puts rules in place to deal with all possible cases in the sorted array. 
# only works if the list is sorted

