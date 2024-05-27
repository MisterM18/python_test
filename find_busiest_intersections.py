def find_busiest_intersections(intersections):
    # Handle edge case: empty dictionary
    if not intersections:
        return []

    max_vehicles = max(intersections.values())
    busiest_intersections = [
        intersection
        for intersection, vehicles in intersections.items()
        if vehicles == max_vehicles
    ]
    return busiest_intersections
