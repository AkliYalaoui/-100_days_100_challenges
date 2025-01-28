"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
from typing import List

OPENING = "("
CLOSING = ")"

class Node : 
    def __init__(self, v):
        self.v = v 
        self.lc = None
        self.rc = None 
    
    def add_left_child(self, lnode): 
        self.lc = lnode

    def add_right_child(self, rnode): 
        self.rc = rnode

def can_append(comb: str, n, direction) -> bool : 
    opening_brackets = 0
    closing_brackets = 0
    for c in comb :
        if c == OPENING : 
            opening_brackets +=1
        else : 
            closing_brackets += 1

    if direction == "LEFT"  : 
        return opening_brackets < n
    else : 
        return closing_brackets < opening_brackets


def construct_tree(node: Node, n: int, d = 0) :
    if d == n*2 : 
        return

    if can_append(node.v, n, "LEFT") : 
        n_l = Node(node.v + OPENING)
        node.add_left_child(n_l)
        construct_tree(n_l, n, d + 1)
    
    if can_append(node.v,n, "RIGHT") : 
        n_r = Node(node.v + CLOSING)
        node.add_right_child(n_r)
        construct_tree(n_r, n, d + 1)


def generate_parentheses(n:int) -> List[str] : 
    if n <= 0 :
        return [""]
    root = Node(OPENING)
    construct_tree(root, n)
    combinations = []
    def get_all_valid_combination(node: Node) : 
        if not node : 
            return
        if not (node.lc or node.rc) : 
            combinations.append(node.v)

        get_all_valid_combination(node.lc)
        get_all_valid_combination(node.rc)

    get_all_valid_combination(root)
    return combinations


import unittest

class TestGeneration(unittest.TestCase):

    def test_generation(self):
        self.assertEqual(["()"], generate_parentheses(1))
        self.assertEqual(["((()))","(()())","(())()","()(())","()()()"], generate_parentheses(3))
        self.assertEqual(["(())", "()()"], generate_parentheses(2))


if __name__ == "__main__":
    unittest.main()