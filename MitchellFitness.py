#Ace_Fitness_Club
class AceFitnessClub():
  
  def __init__(self, firstname, lastname, age, gender, type_of_membership, weight):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.gender = gender
    self.type_of_membership = type_of_membership
    self.weight = weight
    self.weightkilo = round(weight/2.2, 0)
    
    #membership fee
  def membership_fee(self):
    fulltime_membership = 200
    if self.type_of_membership == "fulltime":
      return type_of_membership
    elif self.type_of_membership == "partime":
      return fulltime_membership * 0.75
    else:
     return membership_fee * 0.5 
     
class weightroom(AceFitnessClub):
  pass
  
class runningroom(AceFitnessClub):
  pass
class aquaticroom(AceFitnessClub):
  pass
  
  
    
    
    
    #Convert pounds to kilograms
  def ConvertWeight(self):
      self.weight = self.weight/2.2
      return self.weight


member_1 = AceFitnessClub('Mitchell', 'Benson', 16, 'Male', '2 Years', 130)
member_2 = AceFitnessClub('Kid', 'Benson', 66, 'Male', '6 Years', 9)
member_3 = AceFitnessClub('Sam', 'Smitch', 34, 'Male', '7 Years', 44)

print (membership_fee)

print (member_1.firstname)
print (member_2.lastname)
print (member_3.age)
print (member_1.gender)
print (member_2.type_of_membership)
print (member_3.weight)
print (member_3.weight)
print (member_1.membership_fee)
print (member_2.membership_fee)
print (member_3.membership_fee)



