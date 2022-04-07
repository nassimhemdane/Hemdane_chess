from Piece import Piece

class Queen(Piece):
    def valid_moves(self):
        moves = []
        moves = moves + self.left() + self.right() + self.top() + self.down() + self.right_top() + self.left_top() + self.right_down() + self.left_down()
        return moves

    def left(self):
        lmoves=[]
        pos = self.position
        possible = True
        while(possible):
            if(pos[1]== 0):
                possible = False
                break
            pos=(pos[0],pos[1]-1)
            pot_object = self.gs.get_table()[pos[0],pos[1]]
            if(pot_object==0):
                lmoves.append(pos)
            else:
                if(pot_object.get_team()==self.team):
                    possible=False
                    break
                else:
                    lmoves.append(pos)
                    possible=False
        return lmoves
    def right(self):
        rmoves=[]
        pos = self.position
        possible = True
        while(possible):
            if(pos[1]== 7):
                possible = False
                break
            pos=(pos[0],pos[1]+1)
            pot_object = self.gs.get_table()[pos[0],pos[1]]
            if(pot_object==0):
                rmoves.append(pos)
            else:
                if(pot_object.get_team()==self.team):
                    possible=False
                    break
                else:
                    rmoves.append(pos)
                    possible=False
        return rmoves
        
    def top(self):
        tmoves=[]
        pos = self.position
        possible = True
        while(possible):
            if(pos[0]== 0):
                possible = False
                break
            pos=(pos[0]-1,pos[1])
            pot_object = self.gs.get_table()[pos[0],pos[1]]
            if(pot_object==0):
                tmoves.append(pos)
            else:
                if(pot_object.get_team()==self.team):
                    possible=False
                    break
                else:
                    tmoves.append(pos)
                    possible=False
        return tmoves
    
    def down(self):
        dmoves=[]
        pos = self.position
        possible = True
        while(possible):
            if(pos[0]== 7):
                possible = False
                break
            pos=(pos[0]+1,pos[1])
            pot_object = self.gs.get_table()[pos[0],pos[1]]
            if(pot_object==0):
                dmoves.append(pos)
            else:
                if(pot_object.get_team()==self.team):
                    possible=False
                    break
                else:
                    dmoves.append(pos)
                    possible=False
        return dmoves

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