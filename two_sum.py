# Given an array of numbers and a target, find two integers that sum to the target.
# If you find two integers that add up to the target, return True, else return False

# example = [1, 2, 3, 4] target = 7

def two_sum(arr, target):
    '''Solve problem using dictionary, return True or False'''
    seen = {}
    for e in arr:
        complement = target - e
        if not complement in seen:
            seen[e] = True
        else:
            return True
    return False

def two_sum(arr, target):
    '''Solve problem using dictionary and return indices of elements'''
    seen = {}
    for i, e in enumerate(arr):
        complement = target - e
        if complement in seen:
            return [seen[complement], i]
        seen[e] = i
    return []