import math

"""
Cyclic Sort
numbers in a range
This pattern describes an interesting approach to deal with problems involving arrays containing numbers 
in a given range. For example, take the following problem:
"""

def cyclicsort(nums):
    i = 0
    while i < len(nums):
        numatIndex = nums[i] - 1
        if nums[i] != nums[numatIndex]:
            # switch the numbers because it's not at the appropriate index
            nums[i], nums[numatIndex] = nums[numatIndex], nums[i] # swap
        else:
            i += 1
    return nums


def findMissingNumber(nums):
    """
    sort array using cyclic sort, then return item not at it's index
    """
    i = 0
    n = len(nums)
    while (i < n):
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i] # swap
        else:
            i += 1
    # we have put all the nums in their index
    for i in range(n):
        if nums[i] != i:
            return i
    return n


def findAllMissingNumber(nums):
    """
    sort array using cyclic sort, then return item not at it's index
    """
    i = 0
    n = len(nums)
    while (i < n):
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i] # swap
        else:
            i += 1

    missingNumbers = []
    # we have put all the nums in their index
    for i in range(n):
        if nums[i] !=  i + 1:
            missingNumbers.append(i + 1)
    return missingNumbers


def findDuplicateNumber(nums):
    """
    We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to n. 
    The array has only one duplicate but it can be repeated multiple times. 
    Find that duplicate number without using any extra space. 
    ex: [1, 4, 4, 3, 2] = 4
    """
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] != i+1: # wrong index
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i] # index was filled already, and we found a a number for that index
        else:
            i += 1
    return -1


def findAllDuplicateNumbers(nums):
    """
    We are given an unsorted array containing ‘n +1’ numbers taken from the range 1 to n. 
    The array has some duplicates, find all the duplicate numbers without using any extra space.
    ex: [3, 4, 4, 5, 5] = [4,5]
    Sort and append wrong index
    """
    i = 0
    n = len(nums)
    while (i < n):
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i] # swap
        else:
            i += 1

    duplicatenumbers = []
    # we have put all the nums in their index
    for i in range(n):
        if nums[i] !=  i + 1:
            duplicatenumbers.append(nums[i])
    return duplicatenumbers



def findCorruptPair(nums):
    """
    We are given an unsorted array containing n numbers taken from the range 1 to n. 
    The array originally contained all the numbers from 1 to n, but due to a data error, 
    one of the numbers got duplicated which also resulted in one number going missing. 
    Find both these numbers.
    """
    # cyclic sort and return number and array
    i = 0
    numlen = len(nums)
    while (i < numlen):
        # swap items with index
        number_at_index_i = nums[i] - 1
        if nums[number_at_index_i] != nums[i]:
            # we want to check if index and num item at index and the
            nums[i], nums[number_at_index_i] = nums[number_at_index_i], nums[i]
        else:
            i += 1
    # corrupt pair should be item not at index and index+1 of duplicate
    ret = [-1, -1]
    for k in range(numlen):
        if nums[k] != k+1:
            ret = [nums[k], k+1]
    return ret

def smallestmissingpositivenum(nums):
    """
    We are given an unsorted array containing n numbers taken from the range 1 to n. 
    The array originally contained all the numbers from 1 to n, but due to a data error, 
    one of the numbers got duplicated which also resulted in one number going missing. 
    Find both these numbers.
     
    while (i < n):
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i] # swap
        else:
            i += 1
    
    [1, 3, 1] = 1, 31
    sort by index 0 to n,
    check 0 to n, once number not found, return
    """
    i = 0
    n = len(nums)
    while (i < n):
        number_at_index_i = nums[i] - 1
        if 0 <= number_at_index_i < n and nums[number_at_index_i] != nums[i]:
            nums[number_at_index_i], nums[i] = nums[i], nums[number_at_index_i]
        else:
            i += 1
    for k in range(n):
        if nums[k] != k+1:
            return k+1
    # every num at index 0 to n-1 has a value, so it should me n left
    return n+1


def FirstKMissingPositiveNumbers(nums, count):
    """ HARD
    We are given an unsorted array containing n numbers taken from the range 1 to n. 
    The array originally contained all the numbers from 1 to n, but due to a data error, 
    one of the numbers got duplicated which also resulted in one number going missing. 
    Find both these numbers.

    Answer:
    we would cyclic sort the array. after the sort, we would loop through the array and store
    numbers missing from their index while output < count. We would get the k output array 
    by using the missing numbers and numbers > array length + 1 that are not in the nums array.
    It's sorted because we iterate from the length of the array to the end. Use set to 
    keep track of the numbers we've seen.
    Stop adding when we've gone up to k. Start adding from missing indixes in the cyclic sort array
    once we've gotten past the nums array, start adding from the length of nums making sure to not add
    numbers in the array.
    """
    i = 0
    n = len(nums) 
    while (i < n):
        j = nums[i] - 1
        if nums[j] != nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
        else:
            i += 1
    missingnumbers = []
    extraNumbers = set()

    for num in range(n):
        # only add while len(missingnumbers) < k:
        if len(missingnumbers) < count:
            if nums[num] != num+1:
                missingnumbers.append(num+1)
                extraNumbers.add(nums[num])
    
    # add the remaining missing numbers 
    while len(missingnumbers) < count:
        candidateNumber = i + n
        # ignoring numbers already in the nums array
        if candidateNumber not in extraNumbers:
            missingnumbers.append(candidateNumber)
        i += 1
    return missingnumbers