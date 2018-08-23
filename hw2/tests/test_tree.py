import unittest
from tree.tree import Tree, Node


class TestTree(unittest.TestCase):

    def test_get_tree_list1(self):
        """
        Test a single node tree
        :return:
        """
        a = Node(1, None, None)
        tree1 = Tree(a)
        assert tree1.get_tree_list(a) == ['1']

    def test_get_tree_list2(self):
        """
        Test a complete binary tree
        :return:
        """
        a = Node(1, None, None)
        b = Node(2, None, None)
        c = Node(3, None, None)
        d = Node(4, None, None)
        e = Node(5, None, None)
        f = Node(6, None, None)
        g = Node(7, None, None)
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.left = f
        c.right = g
        tree2 = Tree(a)
        expected_list2 = [['|', '|', '|', '1', '|', '|', '|'],
                          ['|', '2', '|', '|', '|', '3', '|'],
                          ['4', '|', '5', '|', '6', '|', '7']]
        assert tree2.get_tree_list(a) == expected_list2

    def test_get_tree_list3(self):
        """
        Test a tree with only left child nodes
        :return:
        """
        a = Node(1, None, None)
        b = Node(2, None, None)
        c = Node(3, None, None)
        a.left = b
        b.left = c
        tree3 = Tree(a)
        expected_list3 = [['|', '|', '|', '1', '|', '|', '|'],
                          ['|', '2', '|', '|', '|', '|', '|'],
                          ['3', '|', '|', '|', '|', '|', '|']]
        assert tree3.get_tree_list(a) == expected_list3

    def test_get_tree_list4(self):
        """
        Test a irregular shape tree
        :return:
        """
        a = Node(1, None, None)
        b = Node(2, None, None)
        c = Node(3, None, None)
        d = Node(4, None, None)
        e = Node(5, None, None)
        f = Node(6, None, None)
        g = Node(7, None, None)
        a.left = b
        a.right = c
        b.right = d
        d.left = e
        c.left = f
        c.right = g
        tree4 = Tree(a)
        exp_list4 = [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
                     ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '3', '|', '|', '|'],
                     ['|', '|', '|', '|', '|', '4', '|', '|', '|', '6', '|', '|', '|', '7', '|'],
                     ['|', '|', '|', '|', '5', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
        assert tree4.get_tree_list(a) == exp_list4
