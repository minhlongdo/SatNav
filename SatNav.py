#/usr/bin/python

import unittest

class SatNav:

    def __init__(self, streets = ['AB5', 'BC4', 'CD7', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']):
        """
        This initialize the SatNav with the routes and its given distances.

        E.g AB4 - A -> B = 4 - distance from A to B is 4, but not B to A.

        Args:
            streets (list): A list of street names. Default to ['AB5', 'BC4', 'CD7', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
        """
        self.all_streets, self.routes = self.__construct_graph(streets)


    def __split_nodes(self, street):
        # Split up the information with the length between 2 routes
        return street[0], street[1], int(street[2:])


    def __construct_graph(self, streets):
        graph = dict()
        all_streets = set()
        for street in streets:
            # Extract start and destination streets and their length
            start, dest, length = self.__split_nodes(street)
            # Records name of streets
            all_streets.add(start)
            all_streets.add(dest)
            if start not in graph.keys():
                graph[start] = {dest:length}
            else:
                graph[start][dest] = length

        return all_streets, graph


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

            if start not in self.routes.keys():
                return "NO SUCH ROUTE"
            if dest not in self.routes[start].keys():
                return "NO SUCH ROUTE"

            length += self.routes[start][dest]

        return length


    def __dijkstra(self, start, dest):
        """
        Using Dijkstra's algorithm since it can be safely assumed that there are no negative distance values.
        """

        # Initialize empty visited dict() to record already visited nodes
        visited = dict()
        # Initialize all unvisited nodes with None for +inf
        unvisited = {node : None for node in self.all_streets}
        current = start
        currentDistance = 0
        unvisited[current] = currentDistance

        while True:
            for neighbour, distance in self.routes[current].items():
                if neighbour not in unvisited:
                    continue
                newDistance = currentDistance + distance
                if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                    unvisited[neighbour] = newDistance
            # Record visited node with its distance
            visited[current] = currentDistance

            # Delete element from unvisited
            del unvisited[current]

            # Ending condition: no unvisited nodes left
            if not unvisited:
                break

            # Get all nodes from the unvisited collection with a non-None value
            candidates = [node for node in unvisited.items() if node[1]]

            if not candidates:
                break

            # Sort candidates in ascending order
            # The first one is the smallest in this list of neighbours
            current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

        if start == dest:
            min_dist = float('inf')

            for key in self.routes.keys():
                for val, dist in self.routes[key].items():
                    if val == dest:
                        if val in visited.keys():
                            if key in visited.keys():
                                min_dist = min(min_dist, visited[key] + dist)
                            break

            if min_dist == float('inf'):
                return "NO SUCH ROUTE"
            return min_dist

        if dest in visited.keys():
            return visited[dest]
        return "NO SUCH ROUTE"


    def shortest_route(self, start, dest):
        """
        Calculate the shortest distance between two streets by using Dijkstra's algorithm.
        E.g.
            satNat = SatNat()

            print satNat.shortest_route("A", "C")
            9

            print satNat.shortest_route("B", "B")
            9

            print satNat.normal_route("D", "A")
            NO SUCH ROUTE
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

    def testShortestRoute2(self):
        self.assertEqual(9, self.satNav.shortest_route("B", "B"))

    def testShortestRoute3(self):
        self.assertEqual("NO SUCH ROUTE", self.satNav.shortest_route("D", "A"))

    def testShortestRoute4(self):
        self.assertEqual("NO SUCH ROUTE", self.satNav.shortest_route("A", "A"))

    def testShortestRoute5(self):
        self.assertEqual(7, self.satNav.shortest_route("C", "D"))

    def testShortestRoute6(self):
        self.assertEqual(9, self.satNav.shortest_route("C", "C"))

    def testShortestRoute7(self):
        self.assertEqual(15, self.satNav.shortest_route("D", "D"))

    def testShortestRoute8(self):
        self.assertEqual(9, self.satNav.shortest_route("E", "E"))

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
