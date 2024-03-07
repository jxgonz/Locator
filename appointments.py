from datetime import datetime

class Appointment:
    def __init__(self, appointmentID: int, serviceID: int, userID: int, status: str, appointmentDate: datetime):
        self.appointmentID = appointmentID
        self.serviceID = serviceID
        self.userID = userID
        self.status = status
        self.appointmentDate = appointmentDate  
    
    def bookAppointment(self):
        self.status = "Booked"
        print(f"Appointment {self.appointmentID} has been booked for {self.appointmentDate.strftime('%Y-%m-%d %H:%M:%S')}.")
    
    def cancelAppointment(self):
        self.status = "Cancelled"
        print(f"Appointment {self.appointmentID} has been cancelled.")
    
    def rescheduleAppointment(self, newDate: datetime):
        self.appointmentDate = newDate
        self.status = "Rescheduled"
        print(f"Appointment {self.appointmentID} has been rescheduled to {self.appointmentDate.strftime('%Y-%m-%d %H:%M:%S')}.")
