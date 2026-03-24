class TrainTicket:
    def __init__(self, passenger, source="Delhi", destination="Jaipur"):
        self.passenger = passenger
        self.source = source 
        self.destination = destination
        
    def show_ticket(self):
        print(f"Passenger: {self.passenger} | Route: {self.source} to {self.destination}")
    
    def calculate_fare(self):
        pass 

t1 = TrainTicket("Mahesh")
t2 = TrainTicket("Mukesh", "Pune", "Indore")
t3 = TrainTicket("Suresh", "Bangalore", "Hyderabad")

t1.show_ticket()
t2.show_ticket()
t3.show_ticket()

