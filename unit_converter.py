

print "Hi there, I am your distance buddy. \nI convert km into miles."

while True:
    print "Just type the number of km you want to convert."
    km = raw_input("kilometers: ")

    try:
        km = float (km.replace(",", "."))

        miles = km * 0.621371

        print "{0} kilometers is {1} miles.".format(km, miles)
    except Exception as e:
        print "Please enter a number, not text!"

    choice = raw_input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        print "Thanks for using distance buddy."
        break