import math
import unittest


def maxSubArrayOfSizeK(k, arr):
    """
    Given an array of positive numbers and a positive number k, 
    find the maximum sum of any contiguous subarray of size k.
    Input: [2, 1, 5, 1, 3, 2], k=3 
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].
    Input: [2, 3, 4, 1, 5], k=2 
    Output: 7
    Explanation: Subarray with maximum sum is [3, 4].
    """
    # add up to k, then slide through it, removing
    maxSum, currSum, windowStart = 0, 0, 0

    if len(arr) == 0:
        return 0
    
    for index in range(len(arr)):
        currSum += arr[index]

        if index >= k-1:
            maxSum = max(maxSum, currSum)
            currSum -= arr[windowStart]
            windowStart += 1
    return maxSum


def SmallestSubarryGivenSum(arr, sum):
    """
    Smallest Subarray with a given sum (easy)
    Input: [2, 1, 5, 2, 3, 2], 7
    Output: 2
    Input: [2, 1, 5, 2, 8], S=7 
    Output: 1
    Input: [3, 4, 1, 1, 6], S=8
    Output: 3
    """
    # iterate through the list adding up to k, 
    # then if we've found k, start removing the behind

    totalSum = 0
    minSize = math.inf
    last = 0
    currSize = 0
    for index in range(len(arr)):
        totalSum += arr[index]
        currSize += 1
        while totalSum >= sum:
            minSize = min(currSize, minSize)
            currSize -= 1
            totalSum -= arr[last]
            last += 1
    return minSize


def LongestSubtringofKDistinctCharacters(str, k):
    """
    Given a string, find the length of the longest 
    substring in it with no more than K distinct characters.
    Input: "araaci", K=2
    Output: 4
    Input: "araaci", K=1
    Output: 2
    Input: "cbbebi", K=3
    Output: 5

    code: 
    iterate through the str, keeping track of the frequency of each letter. 
    (we would keep track of the freqency with hashMap (We used a hashmap so
    we can find the distinct number of elements but still be able to remove 
    the elements) if we have more than K distinct items, iterativelty remove 
    the last item in the str's sliding window, also reduce the char's frequency, 
    and if the frequency is 0, remove it from the hashmap). 
    Then set the max_length to be the max between our previously stored maxlength, 
    and the distance between the starting and closing index + 1 since last 
    element wasn't counted
    """
    lastIndex = 0
    maxLength = 0
    CharFre = { }
    for index in range(len(str)):
        currChar = str[index]
        if currChar not in CharFre:
            CharFre[currChar] = 0
        CharFre[currChar] += 1
        
        while len(CharFre) > k:
            leftChar = str[lastIndex]
            CharFre[leftChar] -= 1
            if CharFre[leftChar] == 0:
                del CharFre[leftChar]
            lastIndex += 1
        maxLength = max(maxLength, index-lastIndex+1)
    return maxLength


def FruitsIntoBasket(fruits):
    """
    https://leetcode.com/problems/fruit-into-baskets/
    problem: 
    Given an array of characters where each character represents a fruit tree, 
    you are given two baskets and your goal is to put maximum number of fruits 
    in each basket. The only restriction is that each basket can have only one 
    type of fruit. You can start with any tree, but once you have started you 
    cant skip a tree. You will pick one fruit from each tree until you cannot,
    i.e., you will stop when you have to pick from a third fruit type. Write 
    a function to return the maximum number of fruits in both the baskets.
    code: 
    
    similar to longest distinct element substring elements?
    iterate through the list adding to a hashmap or incrementing the 
    hashmaps counter. if k > # of fruits, remove last item. iteratively 
    save the max sum 

    """
    currElements = {}
    lastIndex = 0
    maxSize = 0
    for index in range(len(fruits)):
        rightFruit = fruits[index]
        # acessing list takes time, so we remember the name once and use it
        if rightFruit not in currElements:
            currElements[rightFruit] = 0
        currElements[rightFruit] += 1

        while len(currElements) > 2:
            leftFruit = fruits[lastIndex]
            currElements[leftFruit] -= 1
            if currElements[leftFruit] == 0:
                del currElements[leftFruit]
            lastIndex += 1
        maxSize = max(maxSize, index-lastIndex + 1)

    return maxSize


def NoRepeatSubstring(str):
    """
    medium
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
    problem: 
    Given a string, find the length of the longest substring 
    which has no repeating characters
    code:
    iterate through the string recording the max length of the str. 
    use a hashset to store strings. once at a repeated substring, 
    start deleting backwards till it doesn't repeat.
    DATA STRUCTURE: 
    """
    maxLength = 0
    chars = set()
    lastChar = 0
    totalStrs = 0

    for index in range(len(str)):
        while str[index] in chars:
            chars.remove(str[lastChar])
            lastChar += 1
            totalStrs -= 1

        chars.add(str[index])
        totalStrs += 1
        maxLength = max(maxLength, totalStrs)
    return maxLength

def LongestStrWithSameLettersAfterReplacement(str, k):
    """
    HARD ***
    Given a string with lowercase letters only, if you are 
    allowed to replace no more than k letters with any letter, 
    find the length of the longest substring having the same letters 
    after replacement
    """
    maxLength = 0
    MaxLetRepeat = 0
    FreqMap = {}
    lastIndex = 0

    for index in range(len(str)):
        currElem = str[index]
        if currElem not in FreqMap:
            FreqMap[currElem] = 0
        FreqMap[currElem] += 1
        # maxLetRepeat is currently the maximum repeating character
        MaxLetRepeat = max(MaxLetRepeat, FreqMap[currElem])
        
        # now, in the window, we have a max repeating letter and some other letters. We would make
        # sure that the window = max repeating letter + k pr shrink it
        if ( index - lastIndex + 1 - MaxLetRepeat) > k:
            lastChar = str[lastIndex]
            FreqMap[lastChar] -= 1
            lastIndex += 1
        maxLength = max(maxLength, index - lastIndex + 1)
    return maxLength

def LongestStrWithSameOnessAfterReplacement(arr, k):
    """
    HARD ***
    Given an array containing 0s and 1s, if you are allowed to replace no more than 
    k 0s with 1s, find the length of the longest contiguous subarray having all 1s
    """
    maxLength = 0
    FreqMap = {1: 0, 0: 0}
    lastIndex = 0
    
    # main idea, sliding window + compare size between 1's + k non ones
    for index in range(len(arr)):
        FreqMap[arr[index]] += 1

        if ( index - lastIndex + 1 - FreqMap[1]) > k:
            FreqMap[arr[lastIndex]] -= 1
            lastIndex += 1
        maxLength = max(maxLength, index - lastIndex + 1)
    return maxLength


"""
Problem challenges
"""

def find_permutation(str, pattern):
    """
    HARD ***
    Find pattern in the str
    Understanding the solution. add all chars and their frequencies to a hashmap. Create a sliding window, 
    and for every iteration, if the char is in pattern: 
    then remove it from the freq (we'll add it later) if the freq is 0, then set matched = 0. once matched == len(pattern),
    we'll return true. If windowstart-windowend + 1 <= patternlength, 
    """
    window_start, matched, = 0, 0
    character_frequency = {}
    for letter in pattern:
        if letter not in character_frequency:
            character_frequency[letter] = 0
        character_frequency[letter] += 1
    # our goal is to match all the characters from the char_frequency with the current window.
    # try to extend the range [windowstart, windowend]
    n = len(str)
    for window_end in range(n):
        rightChar = str[window_end]
        if rightChar in character_frequency:
            # decrement the freq of the char
            character_frequency[rightChar] -= 1
            if character_frequency[rightChar] == 0:
                matched += 1

        if matched == len(character_frequency):
            return True
        
        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in character_frequency:
                if character_frequency[left_char] == 0:
                    matched -= 1
                character_frequency[left_char] += 1           
    return False


def findStringAnagrams(str, pattern):
    """
    Given a string and a pattern, find all anagrams of the pattern in the given string.
    Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:
    Input: String="ppqp", Pattern="pq"
    Output: [1, 2]
    Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
    Example 2:

    Input: String="abbcabc", Pattern="abc"
    Output: [2, 3, 4]
    Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
    so, return the starting index of the start of the anagram
    """
    # slide through the window, when we any item in the anagram, start a while loop to check if 
    # we did find 
    # add all characters in the pattern to patternSet 
    window_start, matched, = 0, 0
    character_frequency = {}
    return_indexes = []
    for letter in pattern:
        if letter not in character_frequency:
            character_frequency[letter] = 0
        character_frequency[letter] += 1
    # our goal is to match all the characters from the char_frequency with the current window.
    # try to extend the range [windowstart, windowend]
    n = len(str)
    for window_end in range(n):
        rightChar = str[window_end]
        if rightChar in character_frequency:
            # decrement the freq of the char
            character_frequency[rightChar] -= 1
            if character_frequency[rightChar] == 0:
                matched += 1

        if matched == len(character_frequency):
            return_indexes.append(window_start)
        
        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in character_frequency:
                if character_frequency[left_char] == 0:
                    matched -= 1
                character_frequency[left_char] += 1           
    return return_indexes


def MinimumWindowSubstring(s1, s2):
    """
    Hard. Skipped: https://leetcode.com/problems/minimum-window-substring/
    Given a string and a pattern, find the smallest substring in the given string 
    which has all the characters of the given pattern.
    keep searching till we find the str, then start reducing the window, keeping track of the smallest
    """
    return None


def MinimumWindowSubstring(s1, s2):
    """
    Hard. Skipped: https://leetcode.com/problems/minimum-window-substring/
    Given a string and a list of words, find all the starting indices of substrings 
    in the given string that are a concatenation of all the given words exactly once 
    without any overlapping of words. It is given that all words are of the same length.
    """
    return None
                


