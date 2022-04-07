from Piece import Piece


class Pawn(Piece):




    def valid_moves(self):
        moves=[]
        pos = self.position
        if(self.team==0):
           pas = 1
        else:
           pas=-1
        pos = (pos[0]+pas,pos[1])
        if(not (pos[0]<0 or pos[0]>7 or pos[1]<0 or pos[1]>7)):
            pot_object = self.gs.get_table()[pos[0],pos[1]]
            if(pot_object==0):
                moves.append(pos)
        if(not self.movedonce):
            pos2 = (pos[0]+pas,pos[1])
            if(not (pos2[0]<0 or pos2[0]>7 or pos2[1]<0 or pos2[1]>7)):
                pot_object = self.gs.get_table()[pos2[0],pos2[1]]
                if(pot_object==0):
                    moves.append(pos2)
        pos = (pos[0],pos[1]+1)
        if(not (pos[0]<0 or pos[0]>7 or pos[1]<0 or pos[1]>7)):
            pot_object = self.gs.get_table()[pos[0],pos[1]]
            if(not pot_object==0):
                if(pot_object.get_team()!=self.team):
                    moves.append(pos)
        pos = (pos[0],pos[1]-2)
        if(not (pos[0]<0 or pos[0]>7 or pos[1]<0 or pos[1]>7)):
            pot_object = self.gs.get_table()[pos[0],pos[1]]
            if(not pot_object==0):
                if(pot_object.get_team()!=self.team):
                    moves.append(pos)
        return moves


        
