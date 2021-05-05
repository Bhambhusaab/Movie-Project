import mycolor

color = mycolor.Color()


class Theater:
    # Theater Menu is to see the available option for movie ticket booking
    def theater_menu(self):
        print("1 Show The Seats")
        print("2 Buy A Ticket")
        print("3 Get Statistics")
        print("4 Show Booked Ticket User Info")
        print("0 Exit")

    # TO CREATE THE AUDITORIUM OF THE THEATER
    def __init__(self, row, col):

        self.row = row
        self.col = col
        self.details = {}
        self.matrix = []
        self.pricing = {}
        for i in range(self.row):
            a = []
            for j in range(self.col):
                a.append("S")
            self.matrix.append(a)
        print("Total Seats:", self.row * self.col)

    # TO DISPLAY UPDATED THE SEATS STORE IN MATRIX
    def show_seats(self):
        a1 = 0
        print(end="  ")
        for j in range(1, self.col + 1):
            print(j, end=" ")
        print()
        for i in self.matrix:
            a1 = a1 + 1
            print(a1, end=" ")
            print(" ".join(i), sep=",")

    # TO CALCULATE THE PRICE
    def ticket_revenue(self):
        if self.row * self.col <= 60:
            for i in range(1, self.row + 1):
                for j in range(1, self.col + 1):
                    a2 = {(i, j): 10}
                    self.pricing.update(a2)
        elif self.row * self.col > 60:
            c = self.row // 2
            for i in range(1, self.row + 1):
                for j in range(1, self.col + 1):
                    a2 = {(i, j): 8}
                    self.pricing.update(a2)
            for i in range((c + 1), self.row + 1):
                for j in range(1, self.col + 1):
                    a2 = {(i, j): 10}
                    self.pricing.update(a2)

    # TO GET THE STATISTICS OF THE THEATER
    def get_status(self):
        booked_seat = 0
        vacant_seat = 0
        booked_seat_income = 0
        total_income = 0
        for i in self.details.items():
            x = i[1]
            b = x[4]
            booked_seat_income = booked_seat_income + b
        for i in self.pricing.items():
            total_income = total_income + i[1]
        for i in self.matrix:
            for j in i:
                if j == 'B':
                    booked_seat = booked_seat + 1
                elif j == 'S':
                    vacant_seat = vacant_seat + 1
        print("Number Of Purchased Tickets: ", booked_seat)
        print("Percentage Of Booked Tickets: ", (booked_seat / (vacant_seat + booked_seat)) * 100)
        print("Current Income: ", booked_seat_income)
        print("Total Income: ", total_income, " " + color.END)

    # TO GET THE BOOKED TICKET USER INFO
    def user_info(self, row, col):
        self.get_row = row
        self.get_col = col
        if (int(self.get_row), int(self.get_col)) not in self.details:
            print(color.RED + "\nPlease Enter The Booked Seat Number\n" + color.END)
        else:
            print("Name: ", self.details[int(self.get_row), int(self.get_col)][0])
            print("Gender: ", self.details[int(self.get_row), int(self.get_col)][1])
            print("Age: ", self.details[int(self.get_row), int(self.get_col)][2])
            print("Phone Number: ", self.details[int(self.get_row), int(self.get_col)][3])
            print("Ticket Price: ", self.details[int(self.get_row), int(self.get_col)][4], "\n " + color.END)

    # TO BOOK THE SEAT
    def buy_ticket(self, row, col):
        self.buy_ticket_row = row
        self.buy_ticket_col = col
        if (int(self.buy_ticket_row), int(self.buy_ticket_col)) not in self.pricing:
            print(color.RED + "Please Enter The Correct Seat Number" + color.END)
        else:
            if self.matrix[int(self.buy_ticket_row)][int(self.buy_ticket_col)] == "B":
                print("Seat Already Booked Book Another Seat" + color.END)
            else:
                print("Price Of The Ticket: ", self.pricing[(int(self.buy_ticket_row), int(self.buy_ticket_col))])
                confirm = input("To Confirm Your Booking Click Y\n")
                if confirm == "Y":
                    a12 = {}
                    customer_name, customer_gender, customer_age, customer_phone = input(
                        "Enter Your Name Gender Age Phone Number: \n").split()
                    if int(customer_age) > 17 and len(customer_phone) == 10:
                        a12[int(self.buy_ticket_row), int(self.buy_ticket_col)] = list(
                            (customer_name, customer_gender, int(customer_age),
                             int(customer_phone), self.pricing[
                                 (int(self.buy_ticket_row), int(self.buy_ticket_col))]))
                        self.details.update(a12)
                        self.matrix[int(self.buy_ticket_row)][
                            int(self.buy_ticket_col)] = "B"
                        print(color.GREEN + "Your Booking Is Done" + color.END)
                    else:
                        print(
                            color.CYAN + "\nPeople Between Age 18 and 60 Are Allowed and Check If The Phone Number "
                                         "Enter Is Correct \n" + color.END)
                else:
                    print(color.PURPLE + "Your Current Booking Was Terminated" + color.END)

