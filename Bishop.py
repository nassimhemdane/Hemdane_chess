import Piece

class Bishop(Piece.Piece):
    
    def valid_moves(self):
        moves = []
        moves = moves + self.right_top() + self.left_top() + self.right_down() + self.left_down()
        return moves

    def left_top(self):
        ltmoves=[]
        pos = self.position
        possible = True
        while(possible):
            if(pos[0]==0 or pos[1]== 0):
                possible = False
                break
            pos=(pos[0]-1,pos[1]-1)
            pot_object = self.gs.get_table()[pos[0],pos[1]]
            if(pot_object==0):
                ltmoves.append(pos)
            else:
                if(pot_object.get_team()==self.team):
                    possible=False
                    break
                else:
                    ltmoves.append(pos)
                    possible=False
            

        return ltmoves
    def right_top(self):
        rtmoves=[]
        pos = self.position
        possible = True
        while(possible):
            if(pos[0]==0 or pos[1]== 7):
                possible = False
                break
            pos=(pos[0]-1,pos[1]+1)
            pot_object = self.gs.get_table()[pos[0],pos[1]]
            if(pot_object==0):
                rtmoves.append(pos)
            else:
                if(pot_object.get_team()==self.team):
                    possible=False
                    break
                else:
                    rtmoves.append(pos)
                    possible=False
            
        return rtmoves

    def right_down(self):
        rdmoves=[]
        pos = self.position
        possible = True
        while(possible):
            if(pos[0]==7 or pos[1]== 7):
                possible = False
                break
            pos=(pos[0]+1,pos[1]+1)
            pot_object = self.gs.get_table()[pos[0],pos[1]]
            if(pot_object==0):
                rdmoves.append(pos)
            else:
                if(pot_object.get_team()==self.team):
                    possible=False
                    break
                else:
                    rdmoves.append(pos)
                    possible=False
            
        return rdmoves
    def left_down(self):
        ldmoves=[]
        pos = self.position
        possible = True
        while(possible):
            if(pos[0]==7 or pos[1]== 0):
                possible = False
                break
            pos=(pos[0]+1,pos[1]-1)
            pot_object = self.gs.get_table()[pos[0],pos[1]]
            if(pot_object==0):
                ldmoves.append(pos)
            else:
                if(pot_object.get_team()==self.team):
                    possible=False
                    break
                else:
                    ldmoves.append(pos)
                    possible=False
            
        return ldmoves