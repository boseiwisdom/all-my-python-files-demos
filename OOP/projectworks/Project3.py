class Flight:
    def __init__(self,flight_number,destination,capacity,booked_seat=0):
        self.flight_number=flight_number
        self.destination=destination
        self.capacity=capacity
        self.booked_seat=booked_seat
    def book_seat(self):
        if self.capacity==0:
            return "The flight is all booked"
        
        self.booked_seat+=1
        self.capacity-=1
        return "Booked "
    def cancel_seat(self):
        if self.booked_seat!=0:
            self.booked_seat-=1
            self.capacity+=1
            return "seat Cancel"
    def available_seats(self):
        return self.capacity
class Passenger:
    def __init__(self,name,passport_number,):
        self.name=name
        self.passport_number=passport_number
    def book_flight(self,flight):
        if flight.available_seats()!=0:
            flight.book_seat()
            return "booked"
        return "The flight is all booked"
class Airline:
    def __init__(self,flight,passenger=None):
        self.flight=flight
        self.passenger=passenger
        

plan1=Flight(20,"london",2,0)
bio=Passenger("Osei",11)
lon=Airline(plan1,bio)
print()
print(lon.passenger.book_flight(plan1))
# print(lon.passenger.book_flight(plan1))
# print(lon.passenger.book_flight(plan1))

# print(lon.flight.cancel_seat())
print(lon.flight.available_seats())
    
    
    
