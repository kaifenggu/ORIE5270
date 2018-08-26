import unittest
from codes.bellman_ford import find_negative_cycles


class TestBellmanFord(unittest.TestCase):

    def test_bellman_ford(self):
        name_txt_file1 = 'graph1.txt'
        res1 = find_negative_cycles(name_txt_file1)
        assert res1 == []
        name_txt_file2 = 'graph2.txt'
        res2 = find_negative_cycles(name_txt_file2)
        assert res2 == ['5', '7', '8', '5']
