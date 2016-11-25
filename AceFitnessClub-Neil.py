'''Ace Fitness Club'''
class AceFitnessClub():
  
  def __init__(self, firstName, lastName, age, gender, memType, weightPound):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
    self.gender = gender
    self.memType= memType
    self.weightPound = weightPound
    self.weightKilo = int(round(weightPound/2.2, 0))
    
def membership_fee(self):
  fulltime_membership = 200
  if memType == "Fulltime":
    return fulltime_membership
  elif self.memType == "Parttime":
    return fulltime_membership * 0.75
  else:
    return membership_fee * 0.5

class weightroom(AceFitnessClub):
  pass

class runningroom(AceFitnessClub):
  pass

class aquaticroom(AceFitnessClub):
  pass

#convert pounds to kilograms
  def convertWeight(self):
   self.weightPound = self.weightPound/2.2
   return self.weightPound
   
  
mem_1 = AceFitnessClub("Sam", "Roberts", 17, "Male", "2 Year", 165)
mem_2 = AceFitnessClub("Bobby", "Smith", 45, "Male", "4 Year", 185)
mem_3 = AceFitnessClub("Rob", "Crosby", 23, "Male", "6 year", 190)

print (membership_fee)

print (mem_1.firstName)
print (mem_2.lastName)
print (mem_3.age)
print (mem_1.gender)
print (mem_2.memType)
print (mem_3.age)
print (mem_1.weightKilo)


print (mem_2.weightKilo)
print (mem_1.memType)
print (mem_3.weightKilo)
