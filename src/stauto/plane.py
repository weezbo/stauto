class Plane:
    def __init__(self, seats):
        self.seats = seats
        self.passenger_list = [number for number in range(1, seats + 1)]
        self.available_seat_indexes = [number for number in range(seats)]
        self.boarding_patterns = [[]]

    def get_seats(self):
        return self.available_seat_indexes

    def get_preboard_list(self):
        return self.passenger_list

    def generate_boarding_pattern(self, first_seat):
        board_pattern = [0]*self.seats
        open_seats = self.available_seat_indexes
        board_pattern[first_seat] = self.passenger_list[0]
        open_seats.remove(first_seat)

        for passenger in self.passenger_list:
            if passenger - 1 in open_seats:
                board_pattern[passenger-1] = passenger
            elif len(open_seats) == 1:
                board_pattern[open_seats[0]] = passenger
        return board_pattern
