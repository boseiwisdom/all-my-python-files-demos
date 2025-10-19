# dictionary is the best option than this
class Patient:
    def __init__(self,patient_id,name,age,disease):
        self.patient_id=patient_id
        self.name=name
        self.age=age
        self.disease=disease
        self.assign_doctor_name=None
        self.assign_doctor_id=None
    def __str__(self):
        return f"Patient name: {self.name}  id :{self.patient_id} doctor :{self.assign_doctor_name} doctor id :{self.assign_doctor_id}"
class Doctor:
    def __init__(self,doctor_id,name,specialization):
        self.doctor_id=doctor_id
        self.name=name
        self.specialization=specialization
    def __str__(self):
        return f"name:{self.name}  id: {self.doctor_id}"
class Hospital:
    def __init__(self,name):
        self.name=name
        self.patients=[]
        self.doctors=[]
    def admit_patient(self,patient):
        for i in self.patients:
            if i.patient_id==patient.patient_id:
                return "Pateint already admitted "
        self.patients.append(patient)
        return "successfully added patient"
    def employ_doctor(self,doctor):
        for i in self.doctors:
            if i.doctor_id==doctor.doctor_id:
                return "Doctor already employed"
        self.doctors.append(doctor)
        return "successfully added doctor"
    def find_doctor_by_id(self,doctor_id):
        for i in self.doctors:
            if i.doctor_id==doctor_id:
                return i
    def find_patient_by_id(self,patient_id):
        for i in self.patients:
            if i.patient_id==patient_id:
                return i
    def assign_doctor(self,patient_id,doctor_id):
        patient=self.find_patient_by_id(patient_id)
        doctor=self.find_doctor_by_id(doctor_id)
        if patient==None and doctor==None:
            return "Both does not exist"
        if patient==None:
            return "Patient does not exist"
        if doctor==None:
            return "doctor not found"
        if patient and doctor and patient.assign_doctor_name==None:
            patient.assign_doctor_name=doctor.name
            patient.assign_doctor_id=doctor.doctor_id
            return "successfully assign patient"
        return "patient already have doctor"
    def discharge_patient(self,patient_id):
        for patient in self.patients:
            if patient.patient_id==patient_id:
                self.patients.remove(patient)
                return "successfully discharged patient"
        return "patient not found"  
    def show_patients(self):
        for i in self.patients:
            print (i)          
Bio=Patient(21,"yaw ",20,"malaria")
Ama=Patient(24,"kwasi ",40,"malaria")
osei=Doctor(23,"Bio ","specialist")
hos1=Hospital("first class")
print(hos1.admit_patient(Bio))
print(hos1.employ_doctor(osei))
print(hos1.assign_doctor(21,23))
print(hos1.assign_doctor(21,23))
print(hos1.admit_patient(Ama))
print(hos1.discharge_patient(24))
hos1.show_patients()