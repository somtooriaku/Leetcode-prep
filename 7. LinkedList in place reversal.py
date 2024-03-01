import math
import unittest

"""
Linked list reversal
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end = " ")
            temp = temp.next
        print()

def reverseLinkedlist(head):
    """
    Reversing the linked list in place
    """
    # none, a, b, c, d
    prev, current = None, head
    while current:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    return slow


def reverseSubLinkedlist(head,  firstindex, secondindex):
    """
    Given the head of a LinkedList and two positions p, q, reverse the 
    LinkedList from position firstsize to secondsize.
    """
    if firstindex == secondindex:
        # the list is one Node long
        return head
    
    # after skipping to firstsize - 1 nodes, we're at the node before firstsize's node
    current, previous = head, None
    i = 0
    while current is not None and i < firstindex-1:
        previous = current
        current = current.next
        i += 1
        # iterate  to the p-1 th node
    
    # we are interested in three parts of the linked list, the part before index firstindex
    # the part between indexes firstindex and secondindex and the part after secondindex
    lastnodeoffirstpart = previous
    # after reversing the linkedlist ' current' will become the last node of the sub list
    lastnodeofsublist = current

    i = 0
    currnext = None
    while current is not None and i < (secondindex - firstindex + 1): # sublist size
        currnext = current.next
        previous = current
        previous = current
        current = currnext
        i += 1
        # this reverses the sublist up until the sublist ending

    if lastnodeoffirstpart is not None:
        lastnodeoffirstpart.next = previous
    else:
        head = previous
    
    lastnodeofsublist.next = current
    return head

def reverse_every_k_elements(head, k):
    """
    Given the head of a LinkedList and a number k, reverse every k sized sub-list 
    starting from the head. If, in the end, you are left with a sub-list with less than 
    k elements, reverse it too.
    SOlution:
    eg: 1,2,3,4,5,6,7,8 -> 3,2,1,6,5,4,8,7
    Solution: go up to the kth element, then reverse the list. then change the head to the end
    of the new list. keep doing this till the end
    """
    if k <= 1 or head is None:
        return head
    
    current, previous = head, None
    while True:
        last_node_of_previous_part = previous
        last_node_of_sub_list = current
        next = None
        i = 0
        while current is not None and i < k: # reverse up to k nodes
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1
        # connect with the previous part
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous
        
        last_node_of_sub_list.next = current

        # after reversing the linkedlist ' current' will become the last node of the sub list
        if current is None:
            break
        previous = last_node_of_sub_list
    return head

def reverse_alternating_k_element_sublist(head, k):
    """
    Given the head of a LinkedList and a number k, reverse every alternating k sized 
    sub-list starting from the head. If, in the end, you are left with a sub-list with 
    less than k elements, reverse it too. k = 2:
    ex: 1 2 3 4 5 6 7 8 => 2 1 3 4 6 5 7 8
    Solution:
    starting at head, switch to kth element, then go up to k and switch again.
    """
    # initiate variables start
    if k <= 1 or head is None:
        return head
    current, previous = head, None
    while True:
        last_node_of_previous_part = previous
        last_node_of_sub_list = current
        next = None
        i = 0
        while current is not None and i < k: # reverse up to k nodes
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1
        # connect with the previous part
        if last_node_of_previous_part is not None:
            last_node_of_previous_part.next = previous
        else:
            head = previous
        last_node_of_sub_list.next = current

        # after reversing the linkedlist ' current' will become the last node of the sub list
        if current is None:
            break
        previous = last_node_of_sub_list
        # iterate to k elements:
        i = 0
        while current is not None and i < k:
            previous = current
            current = current.next
            i += 1
        if current is None:
            break
    return head

def rotate_linkedList(head, rotations):
    """
    Given the head of a Singly LinkedList and a number k, rotate the LinkedList to the right by k nodes. 
    ex: 1 2 3 4 5 6, k = 8 ==> 3 4 5 1 2. explanation: right shift by 8 mod size
    solution:
    1. make last node.next = first none. to make linked list a cycle 
    2. cycle to  kth + 1 element and make it the next list's head
    3. make the kth element . next be None as the new last element
    """
    last_node = head
    list_length = 1
    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1
    last_node.next = head # circular list

    rotations = rotations % list_length
    skip_length = list_length  - rotations

    last_node_of_rotated_list = head
    for i in range(skip_length - 1):
        last_node_of_rotated_list = last_node_of_rotated_list.next
    
    head = last_node_of_rotated_list.next
    last_node_of_rotated_list.next = None
    return head


    