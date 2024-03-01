


"""
Fast and slow pointers pattern
The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that 
uses two pointers which move through the array (or sequence/LinkedList) at different speeds. This approach 
is quite useful when dealing with cyclic LinkedLists or arrays.
By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are 
bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.
One of the famous problems solved using this technique was Finding a cycle in a LinkedList. Let's jump onto 
this problem to understand the Fast & Slow pattern.
"""

# linked list definition
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()



def has_cycle(head):
    """
    Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle 
    in it or not.
    """
    # cycle through list
    first, second = head, head
    while second is not None and second.next is not None:
        second = second.next.next
        first = first.next
        if first == second:
            return True
    return False


def find_cycle_length(head):
    # cycle through list
    first, second = head, head
    
    while second is not None and second.next is not None:
        second = second.next.next
        first = first.next
        if first == second:
            # calculate length
            current = second.next
            count = 1
            while current != second:
                current = current.next
                count += 1
            return count
    return 0


def find_cycle_start(head):
    # move ptr1 to head, move ptr2 to length of the cycle. Start iterating both gradually.
    # once we reach the cycle start, ptr should have gone the length of the cycle, and is 
    # now also at the cycle start
    ptr1, ptr2 = head, head
    len = find_cycle_length(head)

    while len > 0:
        ptr2 = ptr2.next
        len -= 1
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1


def happy_number(num):
    # use a hashmap? once we reach a cycle, we've lost
    slow, fast = num, num
    while True:
        slow = findSquareNum(slow)
        fast = findSquareNum(findSquareNum(fast))
        if slow == fast:
            break
    return slow == 1


def findSquareNum(num):
    ret = 0
    while (num > 0):
        # get last digit
        digit = num % 10
        ret += digit * digit
        num //= 10
    return ret

# print( str( happy_number(23) ) + '= True')
# print( str( happy_number(12)) + '= False')


def findMiddleOfLinkedList(head):
    """
    We can use the Fast & Slow pointers method such that the fast pointer is always twice the nodes ahead of the slow pointer. 
    This way, when the fast pointer reaches the end of the LinkedList, the slow pointer will be pointing at the middle node.
    """
    ptr1, ptr2 = head, head

    while(ptr2 is not None and ptr2.next is not None):
        ptr2 = ptr2.next.next
        ptr1 = ptr1.next
    return ptr1




def PalindromeLinkedList(head):
    """ 
    Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
    bounds: O(N), O(1)
    1 - 2 - 3 - 4 - 3 - 2 - 1
    Solution: find middle, reverse list, compare reversed and start,  reverse back
    """
    fast, slow = head, head

    #find middle
    while(fast and fast.next):
        fast = fast.next.next
        slow = slow.next

    #reverse second half none, a-> b -> c -> d -> e. therefore left always greater than right
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # check if it's a palindrome. prev is the end of the reversed list
    left, right = head, prev
    while right is not None and left is not None:
        if right.value != left.value:
            return False
        right = right.next
        left = left.next
    
    # reverse the list back
    prev = None
    while right:
        temp = right.next
        right.next = prev
        prev = right
        right = temp
    return True


def rearrangeLinkedList(head):
    """
    1. split list
    2. reverse list
    3. insert list
    """
    # split list
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    

    # now we have middle and end
    # reverse the middle linked list in place
    # prev, 1, 2, 1
    # odd, middle = middle
    prev = None
    while slow is not None:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    
    # insert list start=1,2,3 - prev=6,5,4
    start = head
    while start is not None and prev is not None:
        temp = start.next
        start.next = prev
        start = temp

    # setting last node.next to none
    if start is not None:
        start.next = None

        
head = Node("a")
head.next = Node("n")
head.next.next = Node("d")
head.next.next.next = Node("n")
head.next.next.next.next = Node("a")

# head.next.next.next.next.next.next = head.next.next
# print("True: " + str(PalindromeLinkedList(head)))

# head.next.next.next.next.next = Node(6)
# print("Middle Node: " + str(findMiddleOfLinkedList(head).value))

# head.next.next.next.next.next.next = Node(7)
# print("Middle Node: " + str(findMiddleOfLinkedList(head).value))

def cyclecirculararary(arr):
    """
    We are given an array containing positive and negative numbers. Suppose the array contains a number 
    M at a particular index. Now, if M is positive we will move forward M indices and if M is negative 
    move backwards M indices.
    circular array that continues after being stopped
    Write a method to determine if the array has a cycle.
    Example 1:
    [1, 2, -1, 2, 2]
    [0, 1,  2, 3, 4]


    Input: [1, 2, -1, 2, 2] = true
    Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
    Input: [2, 2, -1, 2] = true
    Explanation: The array has a cycle among indices: 1 -> 3 -> 1
    Input: [2, 1, -1, -2] = false
    Explanation: The array does not have any cycle.
    Subproblems:
    1. for each index, check if we find cycle.
    2. if we encounter different direction, or a one element cycle, leave index
    """
    for i in range(len(arr)):
        # get direction
        is_forward = arr[i] >= 0
        slow, fast = i, i
        
        while True:
            # moving a single step for slow pointer
            slow = find_next_index(arr, is_forward, slow)
            # movign a single step for fast pointer
            fast = find_next_index(arr, is_forward, fast)
            if (fast != -1):
                fast = find_next_index(arr, is_forward, fast)
            if slow == -1 or fast == -1 or slow == fast:
                break
        if slow != -1 and slow == fast:
            return True
    return False

def find_next_index(arr, is_forward, current_index):
    direction = arr[current_index] >= 0

    if is_forward != direction:
        return -1 # differing directions
    
    next_index = (current_index + arr[current_index]) % len(arr) # adding indices using modulo 
    # arithmetic to make sure we don't overextend ourselves

    if next_index == current_index:
        # one element cycle
        next_index = -1
    return next_index


