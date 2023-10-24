class patient:
  def __init__(self):
    self.patient_list = {}
    self.appointmentlist={"hema":[],"latha":[],"aswin":[],"siva":[],"samy":[],"dinesh":[]}
    self.patient_history = {}
  def appointment(self,data):
    patient_id = input("Do you have your patient id? if yes please enter the patient ID else enter no")
    if patient_id == "no":
      if len(self.patient_list) == 0:
        patient_id ="NH"+ str(0)
      else:
        patient_id = "NH"+str(len(self.patient_list))
      self.name = input("Enter your name: ")
      self.age = int(input("enter your age: "))
      self.contact_info = int(input("enter your contact details: "))
      self.location = input("Enter your address: ")
      self.patient_list[patient_id] = list([self.name,self.age,self.contact_info,self.location])
      self.patient_history[patient_id] = []
      if len(self.appointmentlist[data]) >=10:
        print("appointments closed")
      else:
         self.appointmentlist[data].append(patient_id)
         print(f"Appointment booked")
    else:
      if patient_id in self.patient_list:
          if len(self.appointmentlist[data]) >=10:
               print("appointments closed")
          else:
                self.appointmentlist[data].append(patient_id)
                print(f"Appointment booked")
      else:
          print("you doesnot hold any ID prior kindly register")
          self.appointment(DoctorName)


  def show(self):
    print(self.appointmentlist)

class hospital(patient):
  def __init__(self):
    self.icu = []
    self.general=[]
    self.emergency=[]
    super().__init__()


  def consult(self,data):
    for x in self.appointmentlist:
      for i in self.appointmentlist[x]:
        if i == data:
          remarks = input("update the patients case history")
          self.patient_history[data].append(remarks)

    patient_status = int(input("""Enter patient status as
    1 for Critical,
    2 for Immediate assistance required ,
    3 for Minor illness"""))

    if patient_status == 1:
      print("patient to be admitted in icu")
      pat_decision =input("enter yes to proceed and no to stop the treatment")
      if len(self.icu) <10 and pat_decision == "yes" :
        self.icu.append(data)
        print("patient admitted treatment started")
      else:
        print("No Beds available requesting to visit nearby hospitals")

    if patient_status == 2:
      print("patient to be admitted in emergency ward")
      pat_decision =input("enter yes to proceed and no to stop the treatment")
      if len(self.emergency) <10 and pat_decision == "yes" :
        self.emergency.append(data)
        print("patient admitted treatment started")
      else:
        print("No Beds available requesting to visit nearby hospitals")

    if patient_status == 3:
      print("patient to be admitted in general ward")
      pat_decision =input("enter yes to proceed and no to stop the treatment")
      if len(self.general)<10 and pat_decision == "yes":
        self.general.append(data)
        print("patient admitted treatment started")
      else:
        print("No Beds available requesting to visit nearby hospitals")

  def admin(self):
    bill = int(input("1 for complete billing done 2 for due in bill"))
    if bill == "1":
      return True
    else:
      return False

  def update_status(self,data):
    current_status = int(input("Enter 1 for under recovery and 2 for completely recovered"))
    if current_status == 1 :
      print("customer is recovering")

    if current_status == 2:
      print("customer recovered discharge initiated")

      while True:
        admin_update = hospital.admin()
        if admin_update == "True":
          if data in self.icu:
            self.icu.remove(data)
            print ("patient is completely recovered and discharged ")
            break
          elif data in self.emergency:
            self.emergency(data)
            print ("patient is completely recovered and discharged ")
            break
          else:
              self.general.remove(data)
              print ("patient is completely recovered and discharged ")
              break
        else:
          print("complete your pending dues")

    def medi_status(self,data):
      print(self.patient_history[data])


import datetime
class doctor:
  def __init__(self):
    self.doclist=["hema","latha","siva","samy","dinesh","aswin"]
    self.appointment = {"Monday":["hema","latha","siva"],"Tuesday":["siva","samy"],
                        "Wednesday":["latha","siva","samy"],"Thursday":["dinesh","aswin"],
                        "Friday":["hema","latha"],"Saturday":["dinesh","siva"],"Sunday":[]}


  #Prints the list of available doctors
  def show(self):
    print(self.doclist)


  #Adds newly recruited doctors
  def add(self,data):
    self.doclist.append(data)
    available_days = list(input("Enter the days of availability").split(','))
    for i in available_days:
      self.appointment[i].append(data)
    print("Updation successful")
    print(self.appointment)


  #Removes the resigned doctors
  def remove(self,data):
    self.doclist.remove(data)
    for i in self.appointment:
      for j in self.appointment[i] :
        if j == data:
         self.appointment[i].remove(data)
    print("updation successful")
    print(self.appointment)


  #Checks the availability of a doctor
  def availability_inquiry(self,name,date):
    date = date.split("/")
    date = datetime.datetime(int(date[2]),int(date[1]),int(date[0]))
    day = date.strftime("%A")
    if name in self.appointment[day]:
      print("Doctor available")
      return True
    else:
      print("Doctor is not available")
      return False


  #checks the availability for the day (today)
  def availability_today(self,name):
    date = datetime.datetime.today()
    day = date.strftime("%A")
    if name in self.appointment[day]:
      print("Doctor available")
      return True
    else:
      print("Doctor is not available")
      return False

nh = hospital()

doc = doctor()

hema = patient()



while True:

  print("\nWelcome to Grace Hospital")
  print("""Enter your choice:
  1 Addition of Doctors
  2 Deletion of doctors
  3 Check availability of the specified doctor on specified date
  4 Booking of appointment
  5 Appointment booking status
  6 Consultation with doctor
  7 Patient medical status
  8 Patient medical history
  9 Exit
  """
  )
  selection = int(input("Enter your requirement: "))
  if selection ==1:
    data = input("Enter the doctor name to be added")
    doc.add(data)
  if selection ==2:
    data = input("Enter the doctor name to be added")
    doc.remove(data)
  if selection ==3:
    doc.show()
    DoctorName = input("Enter the name of doctor to book an appointment ")
    dateofappointment = input("enter the date in dd/mm/yyyy format ")
    doc.availability_inquiry(DoctorName,dateofappointment)
  if selection == 4:
      doc.show()
      DoctorName = input("Enter the name of doctor to book an appointment ")
      result = doc.availability_today(DoctorName)
      if result == True:
        hema.appointment(DoctorName)
  if selection == 5:
    hema.show()
  if selection == 6:
    id = input("enter the patient id")
    nh.consult(id)
  if selection ==7:
    nh.update_status(id)
  if selection == 8:
    nh.medi_status(id)
  if selection == 9:
    break
  else:
    print("Invalid Entry")





