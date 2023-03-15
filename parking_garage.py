# Create a parking garage class with tickets, parking paces, payment, and
# an exit message

from sys import exit
from IPython.display import clear_output

class ParkingGarage():
    """A simple attempt to model a parking garage."""
    
    def __init__(self):
        """Initialize attributes."""
        self.tickets = [10,9,8,7,6,5,4,3,2,1]
        self.parkingSpaces = [1,2,3,4,5,6,7,8,9,10]
        self.currentTicket = {
            'paid': False,
            'number': '',
            'parking spot': ''
            }
        self.payment = ''
        
    def takeTicket(self):
        """
        Give user a ticket.
    `   Adjust amount of tickets and parking spaces by -1
        """
        # If there are spaces and tickets left, move one of each to the
        # current ticket
        if self.tickets and self.parkingSpaces:
            print("\nPrinting ticket...")
            print("Here is your ticket. Please find a parking space.\n")
            self.currentTicket['number'] = self.tickets.pop(-1)
            self.currentTicket['parking spot'] = self.tickets.pop(-1)
        
        # If there is no room left, notify user and stop execution of code
        elif not self.tickets or not self.parkingSpaces:
            print("\nAttempting to print ticket...")
            print("This garage is full. Please return at a later time.\n")
            sys.exit("Program exited. Parking Garage is full.")

    def payForParking(self):
        """
        Asks user for payment.
        Stores valid payment in variable.
        """

        print("Accessing ticket...")

        self.payment = input("Please insert payment and enter 10.50:\n")
        if self.payment == '10.50':
            print("\nThank you for paying. Please exit the garage within 15 minutes.\n")
            self.currentTicket['paid'] = True
        else:
            print("\nYou have not paid the correct ticket amount. You will be asked again upon exit.\n")
        clear_output()

    def leaveGarage(self):
        """Check user payment variable and display appropriate prompt or message."""

        print("Attempting to leave...")

        # User has paid, move ticket and space back to their attribute list
        if self.currentTicket['paid'] == True:
            print("Accessing ticket...")
            print("Thank you, have a nice day!")
            self.tickets.append(self.currentTicket['number'])
            self.currentTicket['number'] = ''
            self.parkingSpaces.append(self.currentTicket['parking spot'])
            self.currentTicket['parking spot'] = ''
        
        # User has not paid, prompt until correct input then restore attributes
        else:
            while self.currentTicket['paid'] == False:
                print("Accessing ticket...")
                self.payment = input("Please reinsert valid payment and enter 10.50:\n")
                if self.payment == '10.50':
                    print("\nThank you for paying. You may exit.")
                    self.currentTicket['paid'] = True
                    self.tickets.append(self.currentTicket['number'])
                    self.currentTicket['number'] = ''
                    self.parkingSpaces.append(self.currentTicket['parking spot'])
                    self.currentTicket['parking spot'] = ''
                else:
                    print("You have not paid the correct ticket amount. Enter 10.50:\n")

# Execution example
my_garage = ParkingGarage()
my_garage.takeTicket()
my_garage.payForParking()
my_garage.leaveGarage()