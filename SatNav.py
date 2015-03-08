#/usr/bin/python

import unittest

class SatNav:
    """
    Attributes
    ----------

    Examples
    --------
    """
    def __init__(self, streets = ['AB5', 'BC4', 'CD7', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']):
        """
        This initialize the SatNav with the routes and its given distances.

        E.g AB4 - A -> B = 4 - distance from A to B is 4, but not B to A.

        Args:
            streets (list): A list of street names. Default to ['AB5', 'BC4', 'CD7', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
        """
        self.routes = self.__construct_graph(streets)


    def __split_nodes(self, street):
        # Split up the information with the length between 2 routes
        return street[0], street[1], int(street[2:])


    def __construct_graph(self, streets):
        graph = dict()
        all_streets = set()
        for street in streets:
            # Extract start and destination streets and their length
            start, dest, length = self.__split_nodes(street)
            all_streets.add(start)
            all_streets.add(dest)
            if start not in graph.keys():
                graph[start] = {dest:length}
            else:
                graph[start][dest] = length

        return graph



    def normal_route(self, route):
        """
        Use this function only if there is a specific order the route has to be traversed.
        Expected input format: ABC
        E.g.
            satNat = SatNat()

            print normal_route("ABC")
            9

            print satNat.normal_route("AD")
            5

            print satNat.normal_route("ADC")
            13

            print satNat.normal_route("AED")
            NO SUCH ROUTE
        """
        length = 0
        for x in range(1, len(route)):
            start, dest = route[x-1], route[x]

            if start not in self.routes:
                return "NO SUCH ROUTE"
            if dest not in self.routes:
                return "NO SUCH ROUTE"

            if dest in self.routes[start]:
                length += self.routes[start][dest]
            else:
                return "NO SUCH ROUTE"
        return length

    def __dijkstra_extract_min(self, start, visited=[]):
        min_node = None
        min_dist = None
        # Go through all the links in
        for v in self.routes[start].keys():
            if v not in visited:
                if min_node is None:
                    min_node = v
                    min_dist = self.routes[start][v]
                else:
                    if self.routes[start][v] < min_dist:
                        min_node = v
                        min_dist = self.routes[start][v]
        return min_node


    def __dijkstra(self, start, dest):
        """
        Using Dijkstra's algorithm since it can be safely assumed that there are no negative distance values.
        """
        # Check if starting and destination nodes exist
        if start not in self.routes.keys():
            return "NO SUCH ROUTE"
        if dest not in self.routes:
            return "NO SUCH ROUTE"
        pass





    def shortest_route(self, start, dest):
        """
        Calculate the shortest distance between two streets by using Dijkstra's algorithm.
        """

        return self.__dijkstra(start, dest)


    def min_junctions(self, start, dest):
        """
        Calculate the number of minimum junctions between the starting and destiation street.

        Args:
            start (str): Starting street.
            dest (str): Destination street.

        Return:
            int: Number of minimum junctions, -1 otherwise.
        """
        # Generate all possible paths

        pass


    def number_of_routes(self, start, dest, threshold):
        """
        Calculate the total possible different routes from starting to destination street
        less than the specified threshold.

        Args:
            start (str): Starting street.
            dest (str): Destination street.

        Returns:
            int: Total possible different routes, -1 otherwise.
        """
        pass


class SatNavTest(unittest.TestCase):

    def setUp(self):
        # With the given test data
        self.satNav = SatNav(streets = ['AB5', 'BC4', 'CD7', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7'])

    def testNormalRoute1(self):
        self.assertEqual(9, self.satNav.normal_route("ABC"))

    def testNormalRoute2(self):
        self.assertEqual(5, self.satNav.normal_route("AD"))

    def testNormalRoute3(self):
        self.assertEqual(13, self.satNav.normal_route("ADC"))

    def testNormalRoute4(self):
        self.assertEqual(21, self.satNav.normal_route("AEBCD"))

    def testNormalRoute5(self):
        self.assertEqual("NO SUCH ROUTE", self.satNav.normal_route("AED"))

    def testShortestRoute1(self):
        self.assertEqual(9, self.satNav.shortest_route("A", "C"))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
