from collections import deque
"""
This pattern is based on the Breadth First Search (BFS) technique to traverse a tree.
Any problem involving the traversal of a tree in a level-by-level order can be efficiently 
solved using this approach. We will use a Queue to keep track of all the nodes of a level 
before we jump onto the next level. This also means that the space complexity of the 
algorithm will be O(W), where w is the maximum number of nodes on any level.
Lets jump onto our first problem to understand this pattern.
"""

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left, self.right, self.next = None, None, None


def traverse(root):
    """
    Given a binary tree, populate an array to represent its level-by-level traversal. 
    You should populate the values of all nodes of each level from left to right in separate
    sub-arrays. Basically populate it with the first array of arrays to be 
    should be recursive
    """
    # add head to return array
    # recursivelt call traverse on left and right
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    while queue:
        # queue is not empty
        levelsize = len(queue)
        currentLevel = []
        for roots in range(levelsize):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.append(currentLevel)
    return result

def reverse_tree(root):
    """
    Given a binary tree, populate an array to represent its level-by-level traversal in reverse 
    order, i.e., the lowest level comes first. You should populate the values of all nodes in
    each level from left to right in separate sub-arrays.
    """
    result = []
    if root is None:
        return result
    queue = deque()
    queue.append(root)
    while queue:
        # queue is not empty
        levelsize = len(queue)
        currentLevel = []
        for roots in range(levelsize):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result = [currentLevel] + result
    return result

def zizagtraversal(root):
    """
    Given a binary tree, populate an array to represent its zigzag level order traversal. 
    You should populate the values of all nodes of the first level from left to right, then right
    to left for the next level and keep alternating in the same manner for the following levels.
    adding position variable to BFS traversal
    """
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    lefttoright = True
    while queue:
        # queue is not empty
        levelsize = len(queue)
        currentLevel = deque()
        for roots in range(levelsize):
            currentNode = queue.popleft()

            if lefttoright:
                # so if we're going left to right, we would add values to the return array from left to right.
                # otherwise we would add values to the return array from right to left
                currentLevel.append(currentNode.val)
            else:
                currentLevel.appendleft(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                # this is adding to the queue
                queue.append(currentNode.right)
        result.append(list(currentLevel))
        lefttoright = not lefttoright
    return result

def find_level_averages(root):
    """
    Given a binary tree, populate an array to represent the averages of all of its levels.
    instead of adding values in queuelength to result, add to count. or add up the values at the end, rather than
    adding the list
    """
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    while queue:
        # queue is not empty
        levelsize = len(queue)
        currentaverage, currentcount = 0, 0
        for roots in range(levelsize):
            currentNode = queue.popleft()
            currentaverage += currentNode.val
            currentcount += 1
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.append((currentaverage/currentcount))
    return result

def find_minimum_depth(root):
    """
    Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path 
    from the root node to the nearest leaf node.
    Solution:
    keep track of minimum, and compare using min whenever we reach a leaf
    """
    if root is None:
        return 0
    
    queue = deque()
    queue.append(root)
    minimumTreeDepth = 0
    while queue:
        # queue is not empty
        minimumTreeDepth += 1
        levelsize = len(queue)
        for roots in range(levelsize):
            currentNode = queue.popleft()
            # check if this is a leafnode
            if not currentNode.left and not currentNode.right:
                return minimumTreeDepth
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return 0

def find_successor(root, key):
    """
    Given a binary tree and a node, find the level order successor of the given node in the tree. 
    The level order successor is the node that appears right after the given node in the level order traversal.
    solution:
    The only difference will be that we will not keep track of all the levels. Instead we will keep 
    inserting child nodes to the queue. As soon as we find the given node, we will return the next node 
    from the queue as the level order successor.
    """
    if root is None:
        return None
    queue = deque()
    queue.append(root)
    while queue:
        currentNode = queue.popleft()
        # insert the children of current node in the queue
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        if currentNode.val == key:
            break
    return queue[0].val if queue else None




def connect_level_order_siblings(root):
    """
    Given a binary tree, connect each node with its level order successor. 
    The last node of each level should point to a null node.
    """
    if root is None:
        return
    
    queue = deque()
    queue.append(root)
    while queue:
        previousnode = None
        levelsize = len(queue)
        currentLevel = []
        for roots in range(levelsize):
            # nodes on the same level
            currentNode = queue.popleft()
            # saved a pointer to last element, then set the last element's next value to current value and moved pointer
            if previousnode:
                previousnode.next = currentNode
            previousnode = currentNode

            currentLevel.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)

def connect_all_successors_using_next(root):
    """
    Given a binary tree, connect each node with its level order successor. 
    The last node of each level should point to the first node of the next level
    """
    if root is None:
        return
    
    queue = deque()
    queue.append(root)
    currentNode, previousnode = None, None
    while queue:
        currentNode = queue.popleft()
        # saved a pointer to last element, then set the last element's next value to current value and moved pointer
        if previousnode:
            previousnode.next = currentNode
        previousnode = currentNode
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)


def tree_right_view(root):
    """
    Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree 
    is the set of nodes visible when the tree is seen from the right side. 
    also just rightmost value on each level
    """
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    while queue:
        # queue is not empty
        levelsize = len(queue)
        currentLevel = []
        for roots in range(levelsize):
            currentNode = queue.popleft()
            currentLevel.append(currentNode.val)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        # reached rightmost element, before going to the next level
        result.append(currentNode.val)
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("reversed" + str(tree_right_view(root)))

main()