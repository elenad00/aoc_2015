""" 
Part One:
Santas elves have provided him the distances between pairs of locations. 
He can start and end at any two (different) locations he wants.
He must visit each location exactly once. 
What is the shortest distance he can travel to achieve this?

For example, given the following distances:
    London to Dublin = 464
    London to Belfast = 518
    Dublin to Belfast = 141
    
The possible routes are therefore:
    Dublin -> London -> Belfast = 982
    London -> Dublin -> Belfast = 605
    London -> Belfast -> Dublin = 659
    Dublin -> Belfast -> London = 659
    Belfast -> Dublin -> London = 605
    Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?
"""

from data.d9 import input_data

def parse_coords(data_in):
    distances = {}
    for line in data_in:
        locations, distance = line.split(" = ")
        location_a, location_b = locations.split(" to ")
        distance = int(distance)
        coords_from_a = [location_b, distance]
        coords_from_b = [location_a, distance]
        if location_a in distances:
            distances[location_a].append(coords_from_a)
        else:
            distances[location_a] = [coords_from_a]
        if location_b in distances:
            distances[location_b].append(coords_from_b)
        else:
            distances[location_b] = [coords_from_b]
    for val in distances:
        distances[val] = sorted(
            distances[val], key=lambda item: item[1])
    return distances

def get_next_stop(distances, current_point, visited):
    choices = distances[current_point]
    for possible in choices:
        city, distance = possible
        if city not in visited:
            # print(f"Next stop: {city} - {distance} miles")
            current_point = city
            visited.append(city)
            return city, distance, visited
                
def plan_route(distances, starting_point):
    # print(f"Starting from {starting_point}")
    visited = [starting_point]
    total_distance = 0
    current_point = starting_point
    for stop in range(len(distances)-1):
        current_point, distance, visited = get_next_stop(
            distances, current_point, visited)
        total_distance+=distance
    return total_distance
          
                    
test_data = [
    "London to Dublin = 464",
    "London to Belfast = 518",
    "Dublin to Belfast = 141"
]             
            
def part_one():
    smallest_distance = 10000
    # distances = parse_coords(data_in=test_data)
    distances = parse_coords(data_in=input_data)
    for starting_point in distances:
        travelled = plan_route(distances, starting_point)
        if travelled < smallest_distance:
            smallest_distance = travelled
    print(smallest_distance)
    return # 117

def part_two():
    return

part_one()
part_two()