"""
This pattern is based on the Depth First Search (DFS) technique to traverse a tree.
We will be using recursion (or we can also use a stack for the iterative approach) to keep track of all the previous 
(parent) nodes while traversing. This also means that the space complexity of the algorithm will be 
O(H), where H is the maximum height of the tree.
Lets jump onto our first problem to understand this pattern.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left, self.right, self.next = None, None, None
        self.maxSum = 0
        self.treeDiameter = 0

    def findDiameter(self, root):
        self.calculate_height(root)
        return self.treeDiameter
    
    def maxSum(self, root):
        self.maximumSumofaPath(root)
        return self.maxSum
    
    def calculate_height(self, currentNode):
        """
        Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between
        any two leaf nodes. 
        How: for every node, find the heights of the left and right paths then add 1
        return the maximum of the above iteration
        """
        if currentNode is None:
            return None
        
        leftTreeHeight = self.calculate_height(currentNode.left)
        rightTreeHeight = self.calculate_height(currentNode.right)

        diameter = leftTreeHeight + rightTreeHeight + 1

        # update the global tree diameter for this tree
        self.treeDiameter = max(self.treeDiameter, diameter)

        # returns the height of the tree
        return max(leftTreeHeight, rightTreeHeight) + 1
    
def maximumSumofaPath(currentNode):
    """
    Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum. 
    A path can be defined as a sequence of nodes between any two nodes and doesnt necessarily pass through the root.
    """
    if currentNode is None:
        return 0
    
    leftTreeMax = maximumSumofaPath(currentNode.left)
    rightTreeMax = maximumSumofaPath(currentNode.right)

    maxSum = leftTreeMax + rightTreeMax + currentNode.val

    # update the global tree diameter for this tree
    globalmaxSum = max(maxSum, globalmaxSum)

    # returns the max of the tree
    return max(leftTreeMax, rightTreeMax) + currentNode.val
    

def dfs_sum_path(root, sum):
    """
    Given a binary tree and a number s, find if the tree has a path from root-to-leaf such that the sum of all 
    the node values of that path equals s
    """
    if root is None:
        return False
    if root.val == sum and root.left is None and root.right is None: # a leaf and totals sum
        return True
    
    return dfs_sum_path(root.left, sum - root.val) or dfs_sum_path(root.right, sum - root.val)

def dfs_find_paths_for_sum(root, sum):
    """
    Given a binary tree and a number sum, find all paths such that the sum of all the node values 
    of each path equals S.
    """
    allPaths = []
    find_paths_recursive(root, sum, [], allPaths)
    return allPaths


### HELPER FUNCTION ###
def find_paths_recursive(currentNode, sum, currentPath, allPaths):
    """
    helper for dfs_find_paths_for_sum
    """
    if currentNode is None:
        return
    # if not None, add the current node to the path
    currentPath.append(currentNode.val)
    if currentNode.val == sum and currentNode.left is None and  currentNode.right is None:
        allPaths.append(list(currentPath))
    else:
        find_paths_recursive(currentNode.left, sum-currentNode.val, currentPath, allPaths)
        find_paths_recursive(currentNode.right, sum-currentNode.val, currentPath, allPaths)
    del currentPath[-1]

def dfs_traversal(root):
    """
    Return a DFS list of the tree
    """
    currentPath = []
    # call a recursive function instead
    dfs(root, currentPath)
    return currentPath


### HELPER FUNCTION ###
def dfs(root, currentPath):
    """
    DFS recursive function
    """
    if root is None:
        return
    else:
        # root is not none so add to 
        currentPath.append(root.val)
        # non None root
        # call recursive function on left and right nodes
        dfs(root.left, currentPath)
        dfs(root.right, currentPath)
        
def find_all_paths(root):
    """
    Find all paths in a binary tree
    """
    returnlist = []
    # call a recursive function instead
    dfs_all_paths(root, returnlist, [ ])
    return returnlist


### HELPER FUNCTION ###
def dfs_all_paths(root, returnList, currentPath):
    """
    DFS recursive function
    """
    if root is None:
        return
    # root is not none so add to 
    currentPath.append(root.val)
    if root.left is None and root.right is None:
        returnList.append(list(currentPath))              # found a path
    else:
        # non None root
        # call recursive function on left and right nodes
        dfs_all_paths(root.left, returnList, currentPath)
        dfs_all_paths(root.right, returnList, currentPath)
    # remove most recently added node, because when we're moving onto a path without this node, it 
    # shouldnt include this node
    del currentPath[-1]

def CountPathsWithSum(root: Optional[TreeNode], sum):
    """
    Given a binary tree and a number S, find all paths in the tree such that the sum of all the node values of each path equals S. 
    Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).
    """

    return CountPathsWithSumrecursivehelper(root, sum, [])

### HELPER FUNCTION ###
def CountPathsWithSumrecursivehelper(currentNode, sum, currentPath):
    if currentNode is None:
        return 0
    # add current node to path
    currentPath.append(currentNode.val)
    pathCount, pathSum = 0, 0
    # find the sum of all possible sub-paths in the currentPath 
    for i in range(len(currentPath)-1, -1, -1):     # range(len(currentPath)-1, -1, -1) counts backwards from currentpath-1 to 0
        pathSum += currentPath[i]
        if pathSum == sum:
            pathCount += 1
    # traverse to the left tree
    pathCount += CountPathsWithSumrecursivehelper(currentNode.left, sum, currentPath)
    # traverse to the left right
    pathCount += CountPathsWithSumrecursivehelper(currentNode.right, sum, currentPath)
    # remove the current node from the path once we reach this point because we are no longer on a path with this node
    del currentPath[-1]
    return pathCount
    



def findSequence(root: Optional[TreeNode], sequence: list):
    """
    Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in 
    the given tree.
    Solution:
    traverse using DFS, but in each node, check in leftmost sequence char is node. if no: reset path. if yes, 
    move to next sequnce"""
    if root is None:
        return len(sequence) == 0
    return findSequencehelper(root, sequence, 0)

def findSequencehelper(currentNode, sequence, sequenceIndex):
    if currentNode is None:
        return False
    seqLen = len(sequence)
    if sequenceIndex >= seqLen or currentNode.val != sequence[sequenceIndex]:
        return False
    if currentNode.left is None and currentNode.right is None and sequenceIndex == seqLen - 1:
        return True
    return findSequencehelper(currentNode.left, sequence, sequenceIndex+1) or findSequencehelper(currentNode.right, sequence, sequenceIndex+1)
    

    

def findSumOfPaths(root: Optional[TreeNode]):
    """
    Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number. 
    Find the total sum of all the numbers represented by all paths.
    ex: #     12 -> 7, 1 -> 4, null, 10, 5: 1274 + 1210 + 1215 = 
    """
    return findSumOfPathshelper(root, 0)

def findSumOfPathshelper(currentNode, total):
    if currentNode is None:
        return 0
    
    # caclculate the path number of the current node
    pathSum = 10 * pathSum + currentNode.val            # rightshift type code. works how it needs to
    if currentNode.left is None and currentNode.right is None:
        return pathSum
    
    return findSumOfPathshelper(currentNode.left, total) + findSumOfPathshelper(currentNode.right, total)



    





def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.left.left = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    # sum = 23
    # print("Trees paths with sum " + str(sum) + ": " + str(find_paths(root, sum)))
    # print("Trees paths with sum " + ": " + str(find_all_paths(root)))
    #     12
    #   7     1
    # 4     10  5
    print("Tree has paths: " + str(maximumSumofaPath(root)))

main()