class HotelModel():
  
  def __init__(self, nome, estrelas, diaria, cidade):
    self.nome = nome
    self.estrelas = estrelas
    self.diaria = diaria
    self.cidade = cidade

  def toJson(self):
    return {
      'nome': self.nome,
      'estrelas': self.estrelas,
      'diaria': self.diaria,
      'cidade': self.cidade
    }