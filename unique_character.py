# Remembering elements you've seen before
# Given an array of characters (letters, numbers, punc):
# determine if the array has unique characters
# Return True if all characters are unique, return False if there is any repetition

# example = ["a", "b", "c", "d"] => True
# example2 = ["a", "b", "c", "a"] => False

# Two data structures that are constant O(1) = Dictionary {}, set()
# Dictionary or a Set

# Solve the problem using a dictionary {}

def unique_character1(arr):
    '''Utilize a dictionary {} to solve the problem'''
    seen = {}
    for e in arr:
        if not e in seen:
            seen[e] = True
        else:
            return False
    return True

# seen = {
    # "a": True,
    # "b": True
# }

def unique_character2(arr):
    '''Utilize a set() to solve the problem'''
    seen = set()
    for e in arr:
        if not e in seen:
            seen.add(e)
        else:
            return False
    return True

def unique_character3(arr):
    '''Utilize Pythonic method (built-in functions) - 
    compare length of data structures - to solve the problem'''
    return len(arr) == len(set(arr))