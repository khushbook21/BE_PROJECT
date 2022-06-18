import json
class sympt:
  def __init__(self):
      self.run = "run"

  def pancreatic(self):
    
    with open('tensorEnv/pancreatic.json') as f:
      data = json.load(f)
    return data
 
  def atherosclerosis(self):
    with open('tensorEnv/atherosclerosis.json') as f:
      data = json.load(f)
    return data
 
  def thyroid(self):
    with open('tensorEnv/thyroid.json') as f:
      data = json.load(f)
    return data

  def liverdisorders(self):
    with open('tensorEnv/liverdis.json') as f:
      data = json.load(f)
    return data

  def pulmonaryfibrosis(self):
    with open('tensorEnv/pulmonaryfibrosis.json') as f:
      data = json.load(f)
    return data

  def bloodcancer(self):
    with open('tensorEnv/bloodcancer.json') as f:
      data = json.load(f)
    return data
  
  def covid(self):
    with open('tensorEnv/covid-19.json') as f:
      data = json.load(f)
    return data
  
 