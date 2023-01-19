print("Name: Lakshay")
print("Enrollment No.: BT20HCS125")

class Left_Reccursion():
  def __init__(self, dictionary):
    self.dictionary = dictionary
    self.count = 0
    self.remove_production = ''
  
  def Checker(self):
    temp = []
    for i in self.dictionary.keys():
      for j in self.dictionary[i]:
          if j[0] == i:
            temp.append(i)
      print()
    
    prev_var = '0'
    for i in temp:
      if prev_var == i:
        self.count += 1
      else:
        self.count = 0
      self.passing(i, self.count)
      prev_var = i
    self.show()

  def passing(self, i, count):
    if self.count == 0:
      self.dictionary[f"{i}'"] = []
      self.dictionary[f"{i}'"].append('ε')
    self.remove_production = str(self.dictionary[i][count])
    self.dictionary[f"{i}'"].append(self.remove_production[1] + f"{i}'")    
    terminal = self.dictionary[i][-1]
    self.dictionary[i].insert(0, terminal + f"{i}'")
    self.dictionary[i].remove(terminal)
    self.dictionary[i].remove(self.remove_production)

  def show(self):
    print('Production rules are as follows: ', self.dictionary)
    for i in self.dictionary.keys():
      start = ''
      print(f'{i} : ', end='')
      for j in self.dictionary[i]:
        print(f'{start}{j}', end='')
        start = '/'
      print()

grammar = open('C:/Users/laksh/Desktop/Random1.txt', 'r')
Variable = []
p = [] 
Production = {}

for i in grammar:
  Variable.append(i.strip().split(' : '))

for i in range(len(Variable)):
  Production[Variable[i][0]] = Variable[i][1].split('/')

lr = Left_Reccursion(Production)
grammar.close()
lr.Checker()