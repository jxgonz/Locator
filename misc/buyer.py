class Buyer(User):
    def __init__(self):
        self.Appointment = []
    
    def addAppointment(self,appointment):
        self.Appointment.append(appointment)
        
    
    
