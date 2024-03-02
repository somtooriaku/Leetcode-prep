"""
In many problems, where we are given a set of elements such that we can divide them 
into two parts. To solve the problem, we are interested in knowing the smallest element 
in one part and the biggest element in the other part. This pattern is an efficient approach 
to solve such problems.
This pattern uses two Heaps to solve these problems; A Min Heap to find the 
smallest element and a Max Heap to find the biggest element.
Lets jump onto our first problem to see this pattern in action.
Like a tree, but stores min and max values
"""
from heapq import *     # functions for a predefined heap 


# # popular questions:
# Design a class to calculate the median of a number stream. 
# The class should have the following two methods:
# insertNum(int num): stores the number in the class
# findMedian(): returns the median of all numbers inserted in the class

class MedianOfAStream:
    maxHeap = []   # contains the first half of the numbers <= median
    minHeap = []   # contains the second half of the numbers >= median
    """
    Insert numbers and they should be sorted and have a median number
    """
    def __init__(self, num) -> None:
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)


    def insertNum(num):
        """stores the number in the class
        """
        return 0
    def findMedian():
        """returns the median of all numbers inserted in the class
        """
        return 0.0
