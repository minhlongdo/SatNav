How to use the class SatNav

Parameter 'streets' takes in the information between the routes as a list.
satNav = SatNav(streets = ['AB5', 'BC4', 'CD7', 'DC8', 'AD5', 'CE2', 'EB3', 'AE7'])


To calculate the length of the predetermined route:
route: ABC

satNav.normal_route("ABC") -> 9
satNav.normal_route("AD")  -> 5
satNav.normal_route("ADC") -> 13
satNav.normal_route("AED") -> NO SUCH ROUTE


To find the shortest distance between 2 points:
Starting point: A
Destintion point: C

satNav.shortest_route("A", "C") -> 9
satNav.shortest_route("B", "B") -> 9
satNav.shortest_route("D", "A") -> NO SUCH ROUTE


To find route with the exact specified junction value from starting to destination point:
start: A
end: C
junction = 4

satNav.find_route_with_junctions("A", "C", 4, exact=True) -> 3


To find route with a maximum of the specified junction value from starting to destination point:
start: C
end: C
junction = 3

satNav.find_route_with_junctions("C", "C", 3, exact=False) -> 2


To find number of routes with a distance less than the specified value:
start: C
end: C
threshold = 30

satNav.number_of_routes("C", "C", threshold=30, exact=False) -> 9

If exact = True, then it is to find the number of routes with the exact distance of 30.
