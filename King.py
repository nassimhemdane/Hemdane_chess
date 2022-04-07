from Piece import Piece

class King(Piece):
   def valid_moves(self):
       moves=[]
       pos_moves=[(1,0),(1,1),(0,1),(-1,0),(-1,1),(0,-1),(-1,-1),(1,-1)]
       for t in pos_moves:
           bpos =self.position
           bpos = (bpos[0]+t[0],bpos[1]+t[1])
           if(not (bpos[0]<0 or bpos[1]<0 or bpos[0]>7 or bpos[1]> 7)):
                pot_object = self.gs.get_table()[bpos[0],bpos[1]]
                if(pot_object==0):
                    moves.append(bpos)
                else:
                    if(pot_object.get_team()==self.team):
                        pass
                    else:
                        moves.append(bpos)
       return moves


                