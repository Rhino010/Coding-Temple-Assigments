class ParkingGarage():

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        self.parkingSpaces = [1,2,3,4,5,6,7,8,9,10]
        self.currentTicket = {}

    
    def takeTicket(self):
        for i in self.tickets:
            print('Welcome to Premium Parking your ticket number is {i}. Parking is $1/hour. We hope you enjoy your stay.')
            self.currentTicket[i] = False
            self.tickets.pop(i)
            self.parkingSpaces.pop(i)            

    
    def payForParking(self):
       tickNum = int(input('What number is your ticket? '))
       self.num = int(input('How many hours were you parked? '))
       paid = int(input(f'Your total is ${self.num}. Please enter your total payment.'))
       self.currentTicket[tickNum] = True

    def leaveGarage(self):
        tickNum = int(input('Please verify your ticket has been paid by entering your ticket number. '))
        if self.currentTicket[tickNum] == True:
            print('Thank you and have a great day.')

        else:
            int(input(f'Please pay ${self.num}. Enter your payment here.'))
            self.tickets.append(self.num)
            self.parkingSpaces.append(self.num)

garage = ParkingGarage()    
garage.takeTicket('')
garage.payForParking('')
garage.leaveGarage('')
        
            

    
