"""
A complete binary tree is a binary tree in which all the levels are completely 
filled except possibly the lowest one, which is filled from the left.
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
