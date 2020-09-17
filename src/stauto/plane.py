def odds_of_last_passenger_getting_correct_seat(total_seats):
    return total_seats if total_seats < 2 else .5


def odds_that_seat_is_available_for_last(total_seats):
    if total_seats < 2:
        return total_seats
    numerator = total_seats - 1
    denominator = total_seats
    for _ in range(2, total_seats):
        numerator -= 1
        denominator -= 1
    return 1 - numerator/denominator



