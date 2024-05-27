def find_busiest_intersections(data):
    # สร้างพจนานุกรมเพื่อเก็บจำนวนรถของแต่ละทางแยก
    intersections = {}

    # นับจำนวนรถของแต่ละทางแยก
    for line in data:
        road, cars = line.strip().split(",")
        intersection = road.split("-")[1]  # ตัดชื่อทางแยกออกมา
        if intersection in intersections:
            intersections[intersection] += int(cars)
        else:
            intersections[intersection] = int(cars)

    # หาว่าทางแยกใดมีจำนวนรถมากที่สุด
    max_count = max(intersections.values())
    busiest_intersections = [
        intersection
        for intersection, count in intersections.items()
        if count == max_count
    ]

    return busiest_intersections, max_count

