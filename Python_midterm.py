class star_Cinema:
    hall_list = []  
    def entry_hall(self, hall_obj):
        self.hall_list.append(hall_obj)

class Hall(star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}  
        self.__show_list = []  
        self.rows = rows 
        self.cols = cols 
        self.hall_no = hall_no
        self.entry_hall(self)
    
    def entry_show(self , id, movie_name, time):
        t = (id, movie_name, time)
        self.__show_list.append(t)
        li = []
        for i in range(self.rows):
            a = []
            for j in range(self.cols):
                a.append(0)
            li.append(a)
            self.__seats[id] = li

    def book_seats(self , id , lis):
        if id not in self.__seats:
            print("Invalid show id")
            return
        pi = self.__seats[id]
        for i in lis:
            row, col = i
            if row < 1 or row > self.rows or col < 1 or col > self.cols:
                print(f"Invalid seat {row},{col}, please choose a valid seat")
                continue
            if pi[row-1][col-1] == 1:
                print(f"Seat {row},{col} is already booked")
            else:
                pi[row-1][col-1] = 1
                print(f"Seat {row},{col} booked successfully")
        self.__seats[id] = pi
        
    def view_show_list(self):
        count = 1
        for show in self.__show_list:
            print("------------------")
            print(f"show : {count}")
            print("------------------")
            print(f"ID : {show[0]}")
            print(f"Movie Name: {show[1]}")
            print(f"Time : {show[2]}")
            print()
            count+=1
            
    
    def view_available_seats(self , id):
        if id not in self.__seats:
            print(f'Invalid show id')
        
        count = 0
        pi = self.__seats[id]
        print(f"Available seats for show {id}: ")
        for i in range(self.rows):
            for j in range(self.cols):
                if pi[i][j]==0:
                    print(f"seat ({i+1}, {j+1}) is available")
                    count+=1
                elif pi[i][j]==1:
                    print(f"seat ({i+1}, {j+1}) is already booked")
        print(f"Number of available seats : {count}")


print()
print("""
        ------------------------
        |   Hall Details       |
        ------------------------
        """)
print()
print("Enter hall information: ")
print()
row = int(input("Enter row of hall : "))
col = int(input("Enter column of hall : "))
hallno = int(input("Enter hall no : "))
obj = Hall(row,col,hallno)

obj.entry_show('1002' , 'Dirilis','10:30 am')
obj.entry_show('1004' , 'Kurulus','12:30 pm')
obj.entry_show('1005' , 'Seljuk','3:30 pm')
obj.entry_show('1006' , 'Barbaroslar','5:00 pm')
obj.entry_show('1008' , 'Fatih Sultan','7:30 pm')
while True:
    print("""
            --------------------------------------------
                1. View all shows
                2. View available tickets for a show
                3. Book seats
                4. Exit
            ---------------------------------------------""")
    choose = input("Press a number : ")
    
    if choose == "1":
        print()
        print("""
              ------------------------
              |   View Show detail   |
              ------------------------
              """)
        print()
        for show in star_Cinema.hall_list:
            show.view_show_list()
    elif choose == "2":
        print()
        print("""
              ----------------------------------------
              |   View Available seats for Show      |
              ----------------------------------------
              """)
        print()
        show_id = input("Enter the show id : ")
        obj.view_available_seats(show_id)
    elif choose == "3":
        print()
        print("""
              ------------------------
              |   Seat Booking       |
              ------------------------
              """)
        print()
        show_id = input("Enter the ID of the show: ")
        num_seat = int(input("Enter the number of seats to book: "))
        seats_book = []
        for i in range(num_seat): 
            row = int(input("Enter the row of the seat: "))
            col = int(input("Enter the column of the seat: "))
            seats_book.append((row, col))
        obj.book_seats(show_id, seats_book)
    elif choose == "4":
        print("Exit the system")
        break
    else:
        print("Invalid choice. Please Enter a valid choice.")