
def same_element_count(array1,array2):
    return len(array1) == len(array2)

def same_nested_structure(arr1, arr2):
    for i in range(len(arr1)):
        if (type(arr1[i]) == list or type(arr2[i]) == list):
            if not same_structure_as(arr1[i], arr2[i]): return False
    return True
            

def same_structure_as(original,other):
    if (not type(original) == list) or (not type(other) == list): return False

    return True if same_element_count(original, other) and same_nested_structure(original, other) else False

