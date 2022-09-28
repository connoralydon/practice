# given a list of intervals 
# https://www.interviewbit.com/problems/disjoint-intervals/

# given a list of intervals, [start,end]

# find the length of the maximal set of mutually disjoint intervals
# a disjoint interval are intervals that don't overlap
# if they share a start/end time they are not disjoint

# rule is that current block can't look at another block where the start/end overlap at all, inclusive

# heuristic - choosing intervals that end earlier

def solve(arr):
    arr.sort(key=lambda x:x[1]) # sort intervals on engine positons
    
    prev_s, prev_e = arr[0] # intervals that ends earliest
    
    count = 1 # selected the first interval
    
    for s, e in arr:
        if s <= prev_e: # if the start intersects with the previous interval
            pass
        else:
            prev_s, prev_e = s, e
            count += 1
    

    return count
    