
class Piece:
  def __init__(self, name, id, team,gs, position=None ):
    self.name = name
    self.gs = gs
    self.position = position
    self.id = id
    self.team = team
    self.movedonce=False


  def set_moved_one(self):
      self.movedonce = True
  def get_name(self):
      return self.name

  def get_team(self):
      return self.team

  def get_id(self):
      return self.id

  def get_position(self):
      return self.position
    
  def set_position(self,position):
      self.position=position
