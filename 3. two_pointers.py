import math
"""
Two pointers pattern: mostly for sorted arrays

"""


def pair_with_targetsum(arr, target):
    """
    given a sorted array, return the numbers that add up to target_sum. 
    with non-negative numbers included.
    to use negative numbers, :
    Use HASHMAP
    We're looking for X+Y = target
    code: using hashtable, to iterate through the list with X, 
    if "target - Y" in hashtable, we have found the solution 
    needed to store index, value and quick lookup. this only comes 
    with experience
    only for positive numbers:
    """
    leftIndex = 0
    rightIndex = len(arr) - 1
    while leftIndex < rightIndex:
        if (arr[leftIndex] + arr[rightIndex]) == target:
            return [leftIndex, rightIndex]
        elif target > (arr[leftIndex] + arr[rightIndex]):
            leftIndex += 1
        else:
            rightIndex -= 1
    return [-1, -1]

def remove_duplicates(arr):
    """
    Given an array of sorted numbers, remove all duplicates from it. 
    You should not use any extra space. after removing the duplicates 
    in-place return the new length of the array.
    """
    # loop through the list with two pointers. 
    # one is current number, the other pointer is index+1
    # check if they are the same and iterate, or remove [123]
    if len(arr) < 2:
        return 1
    index = 0
    while index <= len(arr) - 2:
        if arr[index] == arr[index + 1]:
            arr.pop(index + 1)
        else:
            index += 1
    return len(arr)

def makeSquares(arr):
    """
    given an array with neq and positive numbers, return a sorted 
    array of the numbers without using a sort function
    """
    # find 0 and use two pointers to pos and neg numbers to iterate 
    # through the array
    # [-3. 0, 3]
    length = len(arr)
    # put 0 in an array of same length
    squares = [0 for x in range(length)]

    highestSquareIndex = length - 1
    leftIndex = 0
    rightIndex = length - 1

    # number can be -1
    while leftIndex <= rightIndex:
        if abs(arr[leftIndex]) >= arr[rightIndex]:
            squares[highestSquareIndex] = arr[leftIndex] * arr[leftIndex]
            leftIndex += 1
        else:
            squares[highestSquareIndex] = arr[rightIndex] * arr[rightIndex]
            rightIndex -= 1
        highestSquareIndex -= 1
    
    return squares
"""
print(str(makeSquares([-2, -1, 0, 2, 3])) + ' = [0, 1, 4, 4, 9]')
print(str(makeSquares([-3, -1, 0, 1, 2])) + '= [0, 1, 1, 4, 9]')
"""


def TripleSumtoZero(arr):
    """
    Given an array of unsorted numbers, find all unique triplets 
    in it that add up to zero.
    [-3, 0, 1, 2, -1, 1, -2]
    """
    # for each item we find the target sum, and if we encounter duplicate numbers, we
    # skip the number
    arr.sort()
    triplets = []

    for index in range(len(arr)):
        # skip same elements to avoid duplicate triplets
        if index > 0 and arr[index] == arr[index - 1]:
            continue
        targetSum =  -arr[index]
        leftIndex = index+1
        rightIndex = len(arr) - 1
        while (leftIndex < rightIndex):
            currentSum = arr[leftIndex] + arr[rightIndex]
            if currentSum == targetSum: # found the triplet
                triplets.append([-targetSum, arr[leftIndex], arr[rightIndex]])
                leftIndex += 1
                rightIndex -= 1
                while leftIndex < rightIndex and arr[leftIndex] == arr[leftIndex - 1]:
                    leftIndex += 1 # skip same element to avoid duplicate triplet
                while leftIndex < rightIndex and arr[rightIndex] == arr[rightIndex + 1]:
                    rightIndex -= 1 # skip same element to avoid duplicate triplet
            elif targetSum > currentSum:
                leftIndex += 1 # we need a pair with a bigger sum
            else:
                rightIndex -= 1 # we need a pair with a bigger sum
    return triplets

"""
print(str( TripleSumtoZero([-3, 0, 1, 2, -1, 1, -2]) ) + ' = [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]')
print(str( TripleSumtoZero([-5, 2, -1, -2, 3]) ) + '= [[-5, 2, 3], [-2, -1, 3]]')
"""






def TripleSumCloseToTarget(arr, target_sum):
    """
    Given an array of unsorted numbers and a target number, find a triplet in the array whose sum 
    is as close to the target number as possible, return the sum of the triplet. If there are more 
    than one such triplet, return the sum of the triplet with the smallest sum
    use triple sum to zero [-3, -1, 1, 2], target=1 = 0 
    looking for a sum of 3 numbers that's closest to the target number.
    for each index, store the diff = target-sum. if diff = 0, return sum.
    else, store min(prev_min, diff)=> returns diff = target - sum, then sum = target - diff?
    0, -1. diff = 1, sum = 0-1= --1 = diff
    being able to do math there, is part of the skill
    come back = super confusing work
    """
    # also return smallest sum
    # tracking, sum, difference
    arr.sort()
    smallest_difference = math.inf
    for index in range(len(arr) -2):
        left = index + 1
        right = len(arr) - 1
        while (left < right):
            target_diff = target_sum - arr[index] - arr[left] - arr[right]
            if target_diff == 0:
                return target_sum - target_diff # found the exact sum in the target
            # search for closest sum
            # this is sentence is saying is we find a closer target, or an equal target and the sum is smaller
            if (abs(target_diff) < abs(smallest_difference)) or (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
                # found a closer number to target
                smallest_difference = target_diff
            if target_diff > 0:
                left += 1
            else:
                right -= 1
    return target_sum - smallest_difference
"""
print(str( TripleSumCloseToTarget([-2, 0, 1, 2], 2) ) + ' = 1')
print(str( TripleSumCloseToTarget([-3, -1, 1, 2], 1) ) + '= 0')
print(str( TripleSumCloseToTarget([1, 0, 1, 1], 100) ) + '= 3')
"""


def TripleWithSmallerSum(arr, target):
    """
    Given an array of unsorted numbers and a target number, count triplets less than target
    """
    # sort the list, then check for smaller triplets using two sum method
    # [-1, 4, 1, 2, 3, 4, 5]
    arr.sort()
    count = 0
    for index in range(len(arr)-2):
        left = index + 1
        right = len(arr) - 1
        while ( left < right):
            if target > arr[index] + arr[left] + arr[right]:
                count += right - left # all triplets < right should be counted automatically
                left += 1
            else:
                right -= 1
    return count
""" 
print(str( TripleWithSmallerSum([-1, 0, 2, 3], 3) ) + ' = 2')
print(str( TripleWithSmallerSum([-1, 4, 2, 1, 3], 5) ) + '= 4')
"""

def TripleWithSmallerSumList(arr, target):
    """
    Given an array of unsorted numbers and a target number, count triplets less than target
    """
    # sort the list, then check for smaller triplets using two sum method
    # [-1, 4, 1, 2, 3, 4, 5]
    arr.sort()
    triplets = []
    for index in range(len(arr)-2):
        left = index + 1
        right = len(arr) - 1
        while ( left < right):
            if target > arr[index] + arr[left] + arr[right]:
                for i in range(right, left, -1):
                    triplets.append([arr[index], arr[left], arr[i]]) # why numbers in the middle if we're later count them?
                left += 1
            else:
                right -= 1
    return triplets
"""
print(str( TripleWithSmallerSumList([-1, 0, 2, 3], 3) ) + ' = 2')
print(str( TripleWithSmallerSumList([-1, 4, 2, 1, 3], 5) ) + '= 4')
"""




def SubarraywithProductLessthanaTarget(arr, target):
    """
    Given an array with positive numbers and a target number, find all 
    of its contiguous subarrays whose product is less than the target number.
    starting from front of list starting multiplying neighboring elements till we can't find one?
    // sliding window / two pointers?
    slide through the array, and check if arr[index] < target. if it is, check if it's contigous 
    elements are
    """
    result = []
    for index in range(len(arr)):
        tempIndex = index
        product = arr[tempIndex]
        subarr = []
        while (tempIndex <= len(arr) - 1) and (product < target):
            subarr.append( arr[tempIndex] )
            tempIndex += 1
            result.append(subarr.copy())
            if tempIndex < len(arr):
                product *= arr[tempIndex]
    return result
    
"""
print(str( SubarraywithProductLessthanaTarget([2, 5, 3, 10], 30) ) + ' = [[2], [5], [2, 5], [3], [5, 3], [10]]')
print(str( SubarraywithProductLessthanaTarget([8, 2, 6, 5], 50 ) ) + '= [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]')
"""

def DutchNationalFlagProblem(arr):
    """
    Given an array containing 0s, 1s and 2s, sort the array in-place. 
    You should treat numbers of the array as objects, hence, we cant count 0s, 1s, and 2s 
    to recreate the array.
    """
    # sort the list, then check for smaller triplets using two sum method
    # [1, 0, 2, 1, 0] [1100]-[0011100]
    # iterate through the array, using low and high pointers,while iterating, we will move 
    # all 0s before low and all 2s after high so that in the end, all 1s will be between 
    # low and high.
    low = 0
    high = len(arr) - 1
    index = 0
    while ( index <= high): # because high starts at end and only accepts 2's
        # if the index is 1, switch it with low's index and iterate low. making sure that
        # low (which) starts at index 0 only gets 1's
        # once we pass the index, it's not 2, or 0
        if arr[index] == 0:
            arr[index], arr[low] = arr[low], arr[index]
            low += 1
            index += 1
        elif arr[index] == 1:
            index += 1
        else:
            arr[index], arr[high] = arr[high], arr[index]
            high -= 1
    return arr
    # arr[low] is always 1 or 0, because it starts of as 0, and only increments when 
    # we passed index
"""
print(str( DutchNationalFlagProblem([1, 0, 2, 1, 0]) ) + ' = [0, 0, 1, 1, 2]')
print(str( DutchNationalFlagProblem([2, 2, 0, 1, 2, 0] ) ) + '= [0, 0, 1, 2, 2, 2]')
"""


def searchQuadruplets(arr, target):
    """
    Given an array of unsorted numbers and a target number, find all unique 
    quadruplets in it, whose sum is equal to the target number.
    sort, iterate through array twice, and use find triplets approach
    since it's sorted, idk if 
    [1,2,3,4,5]
    It's ONE SHOT AT INSTACART, I CANNOT TAKE CHANCES: I didn't ignore duplicate numbers, making the sets not distinct
    """
    arr.sort()
    result = []
    for index in range(len(arr)-3):
        if index > 0 and arr[index] == arr[index - 1]:
            continue
        for secondIndex in range(index+1, len(arr)-2):
            if secondIndex > 0 and arr[secondIndex] == arr[secondIndex - 1]:
                continue
            left = secondIndex+1
            right = len(arr) - 1
            while (left < right):
                sum = arr[index] + arr[secondIndex] + arr[left] + arr[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    # we've found a quadruplet
                    result.append([arr[index], arr[secondIndex], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while(left < right and arr[left] == arr[left - 1]):
                        left += 1
                    while(left < right and arr[right] == arr[right - 1]):
                        right -= 1
    return result

""" 
print(str( searchQuadruplets([4, 1, 2, -1, 1, -3],1) ) + ' = [[-3, -1, 1, 4], [-3, 1, 1, 2]]')
print(str( searchQuadruplets([2, 0, -1, 1, -2, 2],2 ) ) + '= [[-2, 0, 2, 2], [-1, 0, 1, 2]]')
"""


def backspaceCompare(str1, str2): 
    """
    It's ONE SHOT AT INSTACART, I CANNOT TAKE CHANCES
    Given two strings containing backspaces (identified by the character #), 
    check if the two strings are equal.
    # set pointers two pointers to strings backwards, and iterate. is # exists, skip next one.
    after skips, check if index[ptr1] = ptr2[index]
    str1="xywrrmp", 
    str2="xywrrmu#p"
    """
    
    ptr1 = len(str1) -1
    ptr2 = len(str2) -1
    # during every iteration,
    while(ptr1 >= 0 or ptr2 >= 0):
        ptr1index = getValidcharHelper(str1, ptr1)
        ptr2index = getValidcharHelper(str1, ptr2)
        if ptr1index < 0 and ptr2index < 0:
            # go to the end of both strings
            return True
        if ptr1index < 0 or ptr2index < 0:
            # go to the end of only one strings, meaning different strings
            return False
        if str1[ptr1index] != str2[ptr2index]:
            # after backspaces, we're always at same index
            return False
        ptr1 -= 1
        ptr1 -= 2
    return True


def getValidcharHelper(strin, index):
    # want to get the next valid char
    # for given index, if '#' index -= 1 and if char, backspace removes one backspace 
    # and index
    backspace = 0
    while(index >= 0):
        if strin[index] == '#':
            backspace += 1
        elif backspace > 0:
            backspace -= 1
        else:
            break
        index -= 1
    return index
    



def MinimuimWindowSort(arr):
    """
    Given an array, find the length of the smallest subarray in it which when sorted 
    will sort the whole array.
    Solution: two pointers at end and begining. keep moving left till we meet an unsorted 
    index and do the same for the right. Find the maximum and minimum of this subarray.
    Extend the subarray from beginning to include any number which is bigger than the 
    minimum of the subarray. Similarly, extend the subarray from the end to include any
    number which is smaller than the maximum of the subarray.
    """
    leftindex = 0
    rightIndex = len(arr) - 1
    while(leftindex < rightIndex and arr[leftindex] <= arr[leftindex + 1]):
        leftindex += 1
        # should break when the array if empty or the left side is not sorted
    if leftindex == rightIndex:
        # the array is sorted, so the leftindex reached the end
        return 0
    while(leftindex < rightIndex and arr[rightIndex] >= arr[rightIndex - 1]):
        rightIndex -= 1
    
    # find max and min of the subarray
    subarryMin = -math.inf
    subarryMax = math.inf

    # find max and min inside subarray:
    for k in range(leftindex, rightIndex+1):
        subarryMin = min(subarryMin, arr[k])
        subarryMax = max(subarryMax, arr[k])
    # extending the subarray to include numbers bigger or smaller than the max and min
    while (leftindex > 0 and arr[leftindex-1] > subarryMin):
        # since it's sorted, only wrong once. Also we're moving backwards
        leftindex -= 1
    while (rightIndex > 0 and arr[rightIndex+1] > subarryMax):
        # since it's sorted, only wrong once. Also we're moving backwards
        rightIndex += 1
    
    return rightIndex - leftindex + 1


print(MinimuimWindowSort( [3, 2, 1] ))

