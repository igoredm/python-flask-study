class UserModel():
  
  def __init__(self, login, senha):
    self.login = login
    self.senha = senha

  def toJson(self):
    return {
      'login': self.login,
      'senha': self.senha
    }