#mult_list(): This function will take a list of numbers as input and return the product of all the numbers in the list.
def mult_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result
