import my_theater as mth
import mycolor

color = mycolor.Color()
print(color.PURPLE + "WELCOME TO MOVIE THEATER\n" + color.END)
row = int(input("Enter The Number Of Rows For Seating ::\n"))
col = int(input("Enter The Number Of Column For Seating ::\n"))
theater = mth.Theater(row, col)
theater.ticket_revenue()
print(color.DARK_CYAN + "-" * 45, "" + color.END)
print("\nWhat Action Would You Like To Perform from the available option")
theater.theater_menu()
while True:
    choice = int(input("Enter Your Choice Here: "))
    if choice == 1:
        print()
        print(color.PURPLE + "Available seats:" + color.END)
        theater.show_seats()
        print(color.DARK_CYAN + "-" * 45, "" + color.END)
        print("\n")
        print(color.GREEN + "Would You Like To Perform another task" + color.END)
        print("\n")
        theater.theater_menu()
    elif choice == 2:
        print()
        print(color.YELLOW + "Enter The Row And Column Number You Would Like To seat" + color.END)
        buy_row, buy_col = input().split()
        theater.buy_ticket(buy_row, buy_col)
        theater.show_seats()
        print(color.DARK_CYAN + "-" * 45, "" + color.END)
        print("\n")
        print(color.GREEN + "Would You Like To Perform another task" + color.END)
        print("\n")
        theater.theater_menu()
    elif choice == 3:
        print()
        print(color.PURPLE + "Here Are The Statistics" + color.END)
        theater.show_seats()
        theater.get_status()
        print(color.DARK_CYAN + "-" * 45, "" + color.END)
        print("\n")
        print(color.GREEN + "Would You Like To Perform another task" + color.END)
        print("\n")
        theater.theater_menu()
    elif choice == 4:
        print()
        print(color.YELLOW + "Enter Booked Seat Number To Get Booked Ticket User Info" + color.END)
        get_row, get_col = input().split()
        print(color.PURPLE + "Here Are The Booked Ticket User Info" + color.END)
        theater.user_info(get_row, get_col)
        print(color.DARK_CYAN + "-" * 45, "" + color.END)
        print("\n")
        print(color.GREEN + "Would You Like To Perform another task" + color.END)
        print("\n")
        theater.theater_menu()
    elif choice == 0:
        print(color.DARK_CYAN + "-" * 45, "" + color.END)
        print()
        print(color.BLUE + "Thank You, For Visiting Our Theater, wish to see you again  Have A Great Day!!" + color.END)
        exit()
    else:
        print(color.RED + "Enter Valid Input" + color.END)
