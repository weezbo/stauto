from stauto.plane import odds_of_last_passenger_getting_correct_seat


def test_odds_checker_returns_zero_if_plane_has_zero_seats():
    assert odds_of_last_passenger_getting_correct_seat(0) == 0


def test_odds_checker_returns_one_if_plane_has_one_seat():
    assert odds_of_last_passenger_getting_correct_seat(1) == 1


def test_odds_checker_returns_half_if_plane_has_more_seats():
    assert odds_of_last_passenger_getting_correct_seat(2) == .5
    assert odds_of_last_passenger_getting_correct_seat(100) == .5
