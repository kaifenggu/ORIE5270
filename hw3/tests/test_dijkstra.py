import unittest
from codes.dijkstra import find_shortest_path


class TestDijkstra(unittest.TestCase):

    def test_dijkstra(self):
        name_txt_file = 'graph1.txt'
        source = 1
        destination = 4
        res = find_shortest_path(name_txt_file, source, destination)
        assert res == (6, [1, 2, 4])
