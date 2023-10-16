
import itertools

cities = {'A':{"B":10,'C':15,'D': 20},
          'B': {'A':10, "C":35, "D":25},
          'C': {'A':15,'B': 35,'D':30},
          'D': {"A":20,"B":25,"C":30}
          }

def calculate_total_distance(route):
    total_distance = 0
    for i in range (len(route)-1):
        total_distance +=cities[route[i]][route[i+1]]

    total_distance += cities[route[-1]][route[0]]
    return total_distance

all_permutation = itertools.permutations(cities.keys())

shortest_route = None
shortest_distance = float('inf')


for perm in all_permutation:
    distance = calculate_total_distance(perm)
    if distance <shortest_distance:
        shortest_distance = distance
        shortest_route = perm
        
print("shortest route: ",shortest_route)
print("shortest distance: ", shortest_distance)