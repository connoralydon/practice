
# recursive calls happen in this function
def merge_sort(l):
    
    # base case
    if len(l) == 1:
        return l
    
    mid = len(l) // 2 # floor division, # dont need +1 because 0 indexed
    
    left_half = merge_sort(l[:mid]) # right side is exclusive
    right_half = merge_sort(l[mid:]) # doing mid + 1 to keep it truly different than left half
    
    merged_l = merge(left_half, right_half)
    
    return merged_l
    


# merging two lists
def merge(a,b):
    c = []
    
    # can also do this using pointers rather than popping elements from a & b
    while a and b:
        if(a[0] < b[0]):
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
            
    # one list is still good
    
    while a:
        c.append(a[0])
        a.pop(0)
    
    while b:
        c.append(b[0])
        b.pop(0)
        
    return c

def main():
    array = [5,6,2,7,9,2,1,0]
    print(array)
    
    result = merge_sort(array)
    
    print(result)
    
if __name__ == "__main__":
    main()