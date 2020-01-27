class User:
  def __init__(self):
    self.name = ""
    self.email = ""
    self.pwd = ""

  def setName(self, name):
    self.name = name

  def setEmail(self, email):
    self.email = email

  def setPwd(self, pwd):
    self.pwd = pwd

  def getName(self):
    return self.name
  
  def getEmail(self):
    return self.email
  
  def getPwd(self):
    return self.pwd
    