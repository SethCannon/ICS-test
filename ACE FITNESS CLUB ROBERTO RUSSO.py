class ace_fitness_club():
  def __init__(self, firstname, lastname, age, gender, membership, weight,weightpound):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.gender = gender
    self.membership = membership
    self.weight = weight
    self.weightpound = weightpound
    self.weightkilo = round(weightpound/2.2)
    
  def membership_fee(self):
    full_membership = 200
    if self.membership == "premium" and self.age < 65:
      return full_membership
    elif self.membership == "trial":
        return full_membership * 0.75
    else:
        return full_membership * 0.5
        
        
    def pool_cost(self, aquatics):
      aquatics = 300
      
      
    
    def convertweight(self,weight):
      self.weight = weight/2.2
      return self.weight


class weight_room(ace_fitness_club):
  pass
class running(ace_fitness_club):
  pass
class aquatics(ace_fitness_club):
  def membership_fee(self):
    full_membership = 250

pfit_1 = ace_fitness_club("rick", "ross", 50, "premium", "male",250,2)
pfit_2 = ace_fitness_club("drake", "sher",50,"premium", "male",250,2)
pfit_3 = ace_fitness_club("bob", "billy", 120, "premium", "male",250,2)


print(help(ace_fitness_club))




club_1 = ace_fitness_club("Brock", "tool", 20, "male", "premium", 200, 200)
club_2 = ace_fitness_club("Rj","Russo", 22,"male", "premium", 220, 220)
club_3 = ace_fitness_club("jenny","block", 25, "female", "trial", 150, 150)
club_4 = ace_fitness_club("guila", "matrix", 20,"female", "premium", 120, 120)
    
    
    
print (club_2.weightkilo)
print (club_4.firstname)
print (club_1.gender)
print (club_3.membership)
print (help(aquatics))


  
  
  
