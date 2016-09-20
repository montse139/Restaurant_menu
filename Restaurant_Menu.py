import datetime
today = datetime.date.today()

daily_dishes = {}

while True:
    menu = raw_input("Enter the name of the dish: ")
    menu_price = raw_input("Enter the price of the dish: ")
    daily_dishes[menu] = menu_price

    new = raw_input("Would you like to add another dish? (yes/no) ")
    if new != "yes":
        print "Welcome to Restaurant Pepe"
        print today
        print "DAILY MENU"
        for key in daily_dishes:
            print key
            print "Price: %s" % daily_dishes[key]
        break

with open("daily_dishes.txt", "w+") as f:
    f.write("Welcome to Restaurant Pepe" + "\n")
    f.write(str(today) + "\n")
    f.write("DAILY MENU" + "\n")
    for key in daily_dishes:
        f.write(str(key) + "\n")
        f.write("- Price: " + str(daily_dishes[key]) + "\n")
# Restaurant_menu
