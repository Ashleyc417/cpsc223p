# main.py
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (i != j and nums[i] + nums[j] == target):
                return [i, j]
    #pass

def length_of_last_word(s):
    last_word_length = 0
    
    for i in range(len(s) - 1, -1, -1):
        if not s[i].isspace():
            last_word_length += 1
        elif last_word_length > 0:
            break

    return last_word_length
    #pass

def search_insert(nums, target):
    low = 0
    high = len(nums) - 1

    # Perform binary search
    while low <= high:
        mid = (low + high) // 2

        # Check if the target is equal to the current element
        if nums[mid] == target:
            return mid

        # If the target is less than the current element, move the high index to the left
        elif nums[mid] > target:
            high = mid - 1

        # Otherwise, move the low index to the right
        else:
            low = mid + 1

    # If the target is not found, return the low index
    return low
    #pass
