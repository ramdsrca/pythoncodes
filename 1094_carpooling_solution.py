# carpooling_solution.py
def carPooling1(trips, capacity):
    """
    Determines if it is possible to pick up and drop off all passengers for all the given trips without exceeding the vehicle's capacity.
    Args:
        trips (List[List[int]]): A list of trips, where each trip is represented as a list of three integers:
            - num_passengers (int): The number of passengers for the trip.
            - start_location (int): The starting location of the trip.
            - end_location (int): The ending location of the trip.
        capacity (int): The maximum number of passengers that the vehicle can hold.
    Returns:
        bool: True if it is possible to pick up and drop off all passengers without exceeding the vehicle's capacity, False otherwise.
    """
    # Create a list to record passenger changes at each location
    locations = [0] * 1001
    
    # Update passenger changes for each trip
    print("Initial locations list:", locations)
    for trip in trips:
        num_passengers, start_location, end_location = trip
        locations[start_location] += num_passengers
        locations[end_location] -= num_passengers
        print(f"After processing trip {trip}: locations = {locations}")
    
    # Check if capacity is exceeded at any point
    current_passengers = 0
    for i, num_passengers in enumerate(locations):
        current_passengers += num_passengers
        print(f"Location {i}: current_passengers = {current_passengers}")
        if current_passengers > capacity:
            return False
    
    return True

# carpooling_solution_dynamic.py
def carPooling(trips, capacity):
    # Create a dictionary to record passenger changes at each location
    locations = {}
    
    # Update passenger changes for each trip
    print("Initial locations dictionary:", locations)
    for trip in trips:
        num_passengers, start_location, end_location = trip
        if start_location not in locations:
            locations[start_location] = 0
        if end_location not in locations:
            locations[end_location] = 0
        
        locations[start_location] += num_passengers
        locations[end_location] -= num_passengers
        print(f"After processing trip {trip}: locations = {locations}")
    
    # Check if capacity is exceeded at any point
    current_passengers = 0
    for location in sorted(locations):
        current_passengers += locations[location]
        print(f"Location {location}: current_passengers = {current_passengers}")
        if current_passengers > capacity:
            return False
    
    return True

# Test the function with the example input
trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4
result = carPooling(trips, capacity)
print(f"Can we accommodate all trips? {result}")

# Test the function with the example input
trips = [[2, 1, 5], [3, 3, 7],[2, 5, 7]]
capacity = 5
result = carPooling(trips, capacity)
print(f"Can we accommodate all trips? {result}")
