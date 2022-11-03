# k_fold_cross_validation.py

# building k fold cross validation algorithm.
# this is made to split a dataset into k points either in chronological order or randomly selected



# methodology, use hashing to hash the value of the columns or an "id" variable
# this assumes that the hashing algorithm equally distributes he last number in a string across the number of folds k

my_data = []

for i in range(50):
    my_data.append(i)
    
def hash_data(li):
    hashed_list = []
    
    # need to hash on a unique identifier or combination of elements.
    # simply using the index of the element in a dataframe can return the hashed number and the appropriate fold
    
    for element in li: # this assumes it is a single element
        hashed_list.append(hash(str(element)))
    
    return hashed_list

my_data_hashed = hash_data(my_data)

my_data_fold = []

def find_fold(li = [],k = 1):
    # doing modulo on the hashed number
    folded_list = []
    
    for element in li:
        elem_fold = element % k
        folded_list.append(elem_fold)
    
    return folded_list


# all of these lists are matched on index in the list