class HotelModel():
  
  def __init__(self, id, nome, estrelas, diaria, cidade):
    self.id = id
    self.nome = nome
    self.estrelas = estrelas
    self.diaria = diaria
    self.cidade = cidade

  def toJson(self):
    return {
      'id': self.id,
      'nome': self.nome,
      'estrelas': self.estrelas,
      'diaria': self.diaria,
      'cidade': self.cidade
    }