from stauto.plane import Plane


def test_plane_has_a_number_of_seats():
    plane = Plane(5)
    assert plane.get_seats() == [0, 1, 2, 3, 4]


def test_plane_has_passengers_for_seats():
    plane = Plane(4)
    assert plane.get_preboard_list() == [1, 2, 3, 4]


def test_generate_boarding_pattern_with_first_seat_right():
    plane = Plane(2)
    assert plane.generate_boarding_pattern(0) == [1, 2]


def test_generate_boarding_pattern_with_first_seat_wrong():
    plane = Plane(2)
    assert plane.generate_boarding_pattern(1) == [2, 1]
