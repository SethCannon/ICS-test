'''Ace Fitness Club'''
class AceFitnessClub():
  
  def __init__(self, firstName, lastName, age, gender, memType, weightPound):
    self.firstName = firstName
    self.lastName = lastName
    self.age = age
    self.gender = gender
    self.memType = memType
    self.weightPound = weightPound
    self.weightKilo = round(weightPound/2.2)
    
  def membership_fee(self):
    Fulltime = 200
    if self.memType == "Fulltime" and self.age < 65:
      return Fulltime
    elif self.memType == "Parttime" and self.age > 65:
      return Fulltime * 0.75
    else:
      return Fulltime * 0.50
    
#convert pounds to kilograms
  def convertWeight(self):
    self.weightPound = self.weightPound/2.2
    return self.weightPound

class weightRoom(AceFitnessClub):
  pass
weight_1 = weightRoom("Bob", "Slug", 85, "Female", "Fulltime", 895)

class aquaticsUser(AceFitnessClub):
  pass
aquatics_1 = aquaticsUser("Margret", "Beetle", 9, "Male", "Fulltime", 1000)
memCost_pool = 300
print (memCost_pool)
  
class gymUser(AceFitnessClub):
  pass
gym_1 = gymUser("Xavier", "Daren", 1, "Female", "Parttime", 17)

#membership data
mem_1 = AceFitnessClub("Bob", "Slug", 85, "Female", "Fulltime", 895)
mem_2 = AceFitnessClub("Margret", "Beetle", 9, "Male", "Fulltime", 1000)
mem_3 = AceFitnessClub("Xavier", "Daren", 1, "Female", "Parttime", 17)
mem_4 = AceFitnessClub("Obadiah", "Stamkos", 99, "Male", "Parttime", 1)

print (mem_1.firstName)
print (mem_2.lastName)
print (mem_3.age)
print (mem_4.gender)
print (mem_1.memType)
print (mem_2.weightPound)
print (mem_3.convertWeight())
print (mem_1.weightKilo)
print (mem_1.membership_fee())
print (mem_2.membership_fee())
print (mem_3.membership_fee())
print (mem_4.membership_fee())
