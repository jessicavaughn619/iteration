# Reverse function in Python has a bug, we need to reverse strings manually

# Create and return a new string that is the reverse - challenge 1

# Modify existing string - challenge 2

# Example = "hello" => "olleh"

def reverse_string1(arr:str) -> str:
    '''Reverse string by creating a new string'''
    reverse = ""
    for e in arr:
        reverse = e + reverse
    return reverse