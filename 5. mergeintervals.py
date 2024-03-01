import math
from heapq import *
"""
Merge intervals
"""


def mergeintervals(intervals: list[list[int]]):
    """
    three cases for a or b being compared: in not overlap, partly, fully engulfs
    goal: merge two intervals whenever they overlap
    go through list, if a overlaps b return start a and end b, if a engulfs b, remove b, if a comes after
    O(nlogn)
    [1, 2], [2, 4] = [1, 4]
    [1, 6], [2, 5] = [3, 5]
    """
    if len(intervals) < 2:
        return intervals
    intervals.sort(key= lambda x: x[0])

    output = [intervals[0]]

    for index in range(1, len(intervals)):
        start = intervals[index][0]
        end = intervals[index][1]
        lastAddedEnd = output[-1][1]
        # start, end are an index in ...
        if start <= lastAddedEnd:
            output[-1][1] = max(end, lastAddedEnd)
            # covers the case of 
        else:
            output.append([start, end])
    return output


assert mergeintervals( [[1,4], [2,5], [7,9]] ) ==  [[1,5], [7,9]]
assert mergeintervals( [[6,7], [2,4], [5,9]] ) == [[2,4], [5,9]]



def insertIntervals(intervals: list[list[int]], newinterval: list[int]):
    """
    given a set of non overlapping intervals, insert a new interval into the intervals.
    merge if necessary
    [1, 3], [4,5], [7, 9], \ [6, 8]:
    [1, 3], [4,5], [6, 9]
    """
    ret = []
    index = 0
    # skip till we get to something that overlaps
    # keep adding till it doesn't overlap
    # add the rest of the list
    
    for index in range(len(intervals)):
        if newinterval[1] < intervals[index][0]: # newinterval start < intervals[index].start
            ret.append(newinterval)
            return ret + intervals[1:]
        elif newinterval[0] > intervals[index][1]:
            ret.append(intervals[index])
        else:
            newinterval = [min(newinterval[0], intervals[index][0]), max(newinterval[1], intervals[index][1])]
    
    ret.append(newinterval)
    return ret


assert insertIntervals( [[1, 3], [4,5], [7, 9]], [6, 8] ) ==  [[1,3], [4,5], [6, 9]]


def intervalsIntersection(a, b):
    """
    Given two lists of intervals, find the intersection of these two lists. 
    Each list consists of disjoint intervals sorted on their start time.
    [[1, 3], [5, 6], [7, 9]], 
    [[2, 3], [5, 7]] ) 
    ==  [[2, 3], [5, 6], [7, 7]]
    1,2,3,4,5,6,7,8,9
    # find where they intercept and add to list
    for each intervals, starting at index 0,0 check overlapping and do the 
    appropraite, then
    """
    result, i, j, start, end = [], 0, 0, 0, 1

    while i < len(a) and j < len(b):
        # check if intervals overlap and if a[i]'s start time is inside b[j]'s start time
        aoverlapsb = a[i][0] >= b[j][0] and a[i][0] <= b[j][1]
        boverlapsa = a[i][0] >= b[j][0] and a[i][0] <= b[j][1]

        # store the intersection part
        if aoverlapsb or boverlapsa:
            result.append([max(a[i][0], b[j][0]), min(a[i][1], b[j][1])])
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1

    return result

# assert intervalsIntersection( [[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]] ) ==  [[2, 3], [5, 6], [7, 7]]
# assert intervalsIntersection( [[1, 3], [5, 7], [9, 12]], [[5, 10]] ) ==  [[5, 7], [9, 10]]



def conflictingappointments(intervals):
    """
    Given an array of intervals representing N appointments, find out if a person 
    can attend all the appointments.
    bascally check if they are non overlapping? -> sort
    """
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True








class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end
    

def minimumMeetingRooms(meetings):
    """
    Given a list of intervals representing the start and end time of 
    N meetings, find the minimum number of rooms required to hold all the 
    meetings.
    ex: [[1,4], [2,5], [7,9]], output = 2. Since [1,4] and [2,5] need different
    rooms, and [7,9] can be held in any other room
    1. keep track of rooms 1, 2, 3
    2. Sort by start time and iterate, checking for empty rooms form room 1, and adding a meeting to a room
    Algorithm:
    1. Sort all the meetings on their start time.
    2. Create a min-heap to store all the active meetings. This min-heap will also be used to find the 
    active meeting with the smallest end time.
    3. Iterate through all the meetings one by one to add them in the min-heap. 
    Let's say we are trying to schedule the meeting m1.
    4. Since the min-heap contains all the active meetings, so before scheduling m1 we can remove all meetings 
    from the heap that have ended before m1, i.e., remove all meetings from the heap that have an end time smaller 
    than or equal to the start time of m1. Now add m1 to the heap.
    5. The heap will always have all the overlapping meetings, so we will need rooms for all of them. Keep a counter 
    to remember the maximum size of the heap at any time which will be the minimum number of rooms needed.
    """
    meetings.sort(key=lambda x: x.start)

    minrooms = 0
    minHeap = []
    for meeting in meetings:
        # remove all meetings that have ended
        while (len(minHeap) > 0) and meeting.start >= minHeap[0].end:
            heappop(minHeap)
        # add the current meeting into min_heap
        heappush(minHeap, meeting)
        # all active meetings are in the min_heap, so we need rooms for all of them.
        minRooms = max(minRooms, len(minHeap))
    return minRooms

class job:

    def __init__(self, start, end, cpu_load) :
        self.start = start
        self.end
        self.cpu_load = cpu_load
    def __lt__(self, other):
        #min heap based on job.end
        return self.end < other.end

def find_max_cpu_load(jobs):
    """
    We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. 
    Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.
    Jobs: [[1,4,3], [2,5,4], [7,9,6]]
    Output: 7
    Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the 
    """
    jobs.sort(key=lambda x: x.start)
    max_cpu_load, current_cpu_load = 0, 0
    min_heap=[]

    for j in jobs:
        # remove all the jobs that have ended
        while (len (min_heap) > 0 and j.start >= min_heap [0].end) :
            current_cpu_load -= min_heap[0].cpu_load
            heappop (min_heap)
        # add the current job into min_heap
        heappush (min_heap, j)
        current_cpu_load += j.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)
    return max_cpu_load


