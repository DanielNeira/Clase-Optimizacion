"""
This file contains utilities and other basic tools used in the homework exercise.

It contains code related to loading a TSP problem, and some initial simple implementations.
"""
import random
import math

def random_initial_value(n, dist):
    """
    Generate an random initial value for a TSP problem with n places and an distance matrix dist.
    
    Note that the distance matrix dist is ignored as the value is random.
    """
    initial = list(range(n))
    random.shuffle(initial)
    return initial

def objective_tsp(sequence, dist):
    """
    Calculate the objective value for a tour defined by this sequence.
    
    The last element connects back to the first element.
    """
    return sum(dist[i][j] for (i, j) in zip(sequence, sequence[1:])) + \
        dist[sequence[len(sequence)-1]][ sequence[0]] 

def load_tsp_problem():
    """
    Loads the TSP problem for this assignment.
    
    Returns (n, dist, opt)
    """
    
    n = -1
    opt = math.inf
    coord = []
    with open("instances/berlin52.tsp", 'r') as f:
        header = True
        for line in f.readlines():
            if len(coord) == n:  # Must break before EOF
                break
            if header:
                header = "NODE_COORD_SECTION" not in line 
                if "DIMENSION" in line:
                    n = int(line.split()[1])
                if "OPT" in line:
                    opt = float(line.split()[1])
            else:
                x = float(line.split()[1])
                y = float(line.split()[2])
                coord.append((x, y))
        
    distances = calculate_distances(coord)
    return n, distances, opt
    
def distance(p, q):
    """
    Calculate the distance between two points p and q.
    """
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

def generate_euclid_tsp_problem(n, lower, upper):
    """
    Generate an TSP problem with Euclidian distances.
    
    Returns (n, dist)
    """
    
    # Generate n random 2D points.
    points = [(random.uniform(lower, upper), random.uniform(lower, upper)) for _ in range(n)]
    # Update distance matrix.
    dist = calculate_distances(points)
    return n, dist

def calculate_distances(points):
    n = len(points)
    
    # Create empty n x n matrix.
    dist = empty_matrix(n, n)
    
    # Calculate distances
    for p in range(n):
        for q in range(p + 1, n):
            d = distance(points[p], points[q])
            dist[p][q] = d
            dist[q][p] = d
    
    return dist

def empty_matrix(m, n):
    """
    Generates an empty m x n matrix (m lines, n columns)
    
    Returns:
        An empty m x n matrix
    """
    
    return [[0 for _ in range(n)] for _ in range(m)]
