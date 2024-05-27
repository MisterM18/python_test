def find_busiest_intersections(data):
    # สร้างพจนานุกรมเพื่อเก็บจำนวนรถของแต่ละทางแยก
    intersections = {}

    max_count = 0
    busiest_intersections = []

    # นับจำนวนรถของแต่ละทางแยก
    for line in data:
        road, cars = line.strip().split(",")
        intersection = road.split("-")[1]  # ตัดชื่อทางแยกออกมา
        cars = int(cars)

        # ตรวจสอบว่าจำนวนรถของทางแยกปัจจุบันมากกว่าที่เคยเจอหรือไม่
        if cars > max_count:
            max_count = cars
            busiest_intersections = [intersection]
        elif cars == max_count:
            busiest_intersections.append(intersection)

    return busiest_intersections, max_count
