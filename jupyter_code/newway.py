class ParkingGarage():

    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        self.parkingSpaces = [1,2,3,4,5,6,7,8,9,10]
        self.currentTicket = {}
        self.usedTickets = []
    
    def takeTicket(self):
            print(f'Welcome to Premium Parking your ticket number is {self.tickets[0]}. Parking is $1/hour. We hope you enjoy your stay.')
            self.currentTicket[0] = False
            self.usedTickets.append(self.tickets[0])
            self.tickets.pop(0)
            self.parkingSpaces.pop(0)

    def payForParking(self):
        tickNum = int(input('What number is your ticket? '))
        if tickNum not in self.usedTickets:
            print('There is an error in your entry. How about we start over!?')
            
        else:
            self.num = int(input('How many hours were you parked? '))
            self.paid = int(input(f'Your total is ${self.num}. Please enter your total payment. '))
            if self.paid < self.num:
                print('You will need to pay upon leaving.')
            else:
                self.currentTicket[self.num]=True
       

    def leaveGarage(self):
        ticket = int(input('Please verify your ticket has been paid by entering your ticket number. '))
        if self.currentTicket[ticket] == True:
            print('You have 15 minutes to exit. Thank you and have a great day.')
            self.tickets.append(self.num)
            self.parkingSpaces.append(self.num)

        else:
            int(input(f'Please pay ${self.num}. Enter your payment here. '))
            self.tickets.append(self.num)
            self.parkingSpaces.append(self.num)

garage = ParkingGarage()
while True:

    userinput = input('Hello, please type, "get" to receive a ticket, "pay" to pay your tickect, "leave" to leave the garage, or "q" to quit. ')
    if userinput.lower() == 'get':
        garage.takeTicket()
    elif userinput.lower() == 'pay':
        garage.payForParking()
    elif userinput.lower() == 'leave':
        garage.leaveGarage()
    elif userinput.lower() == 'q':
        break
    else:
        print('Sorry that is not recognized. Please select one of the original options.')


        
            

    
