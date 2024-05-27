import unittest


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


class TestFindBusiestIntersections(unittest.TestCase):
    def test_busiest_intersections(self):
        # ข้อมูลทดสอบ
        test_data = [
            "Road-Intersec1,10\n",
            "Road-Intersec2,15\n",
            "Road-Intersec2,5\n",
            "Road-Intersec3,8\n",
        ]

        # Act
        busiest_intersections, max_count = find_busiest_intersections(test_data)

        # Assert
        self.assertEqual(busiest_intersections, ["Intersec2"])
        self.assertEqual(max_count, 20)
        print("ทางแยกที่มีจำนวนรถมากที่สุด:", busiest_intersections)


if __name__ == "__main__":
    unittest.main()
