class StarCinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall_obj):
        if isinstance(hall_obj, Hall):
            cls._hall_list.append(hall_obj)
            print(f"In hall_list added Hall {hall_obj._hall_no} ")
        else:
            print("Invalid hall object. Provide an object of class Hall")


class Hall:
    def __init__(self, hall_no, rows, cols):
        self._seats = {}
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._show_list = []

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self._show_list.append(show_info)
        seats = [['Free' for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[show_id] = seats

    def view_available_seats(self, show_id):
        if show_id in self._seats:
            print(f"Available seats for Show ID {show_id}:")
            seats_available = self._seats[show_id]
            for i, row in enumerate(seats_available, start=1):
                for j, seat in enumerate(row, start=1):
                    if seat == 'Free':
                        print(f"Row: {i}, Col: {j}")
        else:
            print(f"No show found with ID: {show_id}")

    def book_seats(self, show_id, seats_to_book):
        if show_id in self._seats:
            seats_available = self._seats[show_id]
            for seat in seats_to_book:
                row, col = seat
                if 1 <= row <= self._rows and 1 <= col <= self._cols:
                    if seats_available[row - 1][col - 1] == 'Free':
                        seats_available[row - 1][col - 1] = 'Booked'
                        print(f"Seat ({row}, {col}) booked successfully for Show ID: {show_id}")
                    else:
                        print(f"Error: Seat ({row}, {col}) is already booked.")
                else:
                    print(f"Error: Invalid seat ({row}, {col}). Seat is out of range.")
        else:
            print(f"Error: Invalid show ID: {show_id}. Show ID does not exist.")
class Counter:
    def view_all_shows(self, hall):
        print("View all shows:")
        for show_id, movie,time in hall._show_list:
            print(f"Show ID: {show_id}, Movie: {movie} , Time: {time}")

    def view_available_seats(self, hall, show_id):
        hall.view_available_seats(show_id)

    def book_tickets(self, hall, show_id, seats_to_book):
        hall.book_seats(show_id, seats_to_book)


hall = Hall(hall_no=1, rows=10, cols=10)
hall.entry_show(1, "Avengers", "7:00 PM")
hall.entry_show(2, "Spider-Man", "9:00 PM")
hall.book_seats(1, [(1, 2), (2, 3), (3, 4)])
counter = Counter()

while True:
    print("\nSelect an option:")
    print("1. View all shows")
    print("2. View available seats for a show")
    print("3. Book tickets for a show")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        counter.view_all_shows(hall)
    elif choice == '2':
        show_id = int(input("Enter Show ID: "))
        counter.view_available_seats(hall, show_id)
    elif choice == '3':
        show_id = int(input("Enter Show ID: "))
        seats = input("Enter seats to book : ")
        seats_to_book = [tuple(map(int, seat.split(','))) for seat in seats.split()]
        counter.book_tickets(hall, show_id, seats_to_book)
    elif choice == '4':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")
