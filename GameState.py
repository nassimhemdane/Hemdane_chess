import numpy as np
from Bishop import Bishop
from Piece import Piece
from King import King
from Pawn import Pawn
from Queen import Queen
from Rook import Rook
from Knight import Knight
class GameState:


    
    def __init__(self):
        self.logs =[]
        self.alphalist= ['a','b','c','d','e','f','g','h']
        self.nums = ['8','7','6','5','4','3','2','1']
        self.turn=1
        self.finished = False
        self.winner = -1
        self.vtable =  np.zeros((8, 8), dtype=object)
        self.table =  np.zeros((8, 8), dtype=object)
        self.table[0,0] = Rook("Back Rook 1","br",0,self, (0,0))
        self.table[0,1] = Knight("Back Knight 1","bk",0,self, (0,1))
        self.table[0,2] = Bishop("Black Bishop 1","bb",0,self,(0,2))
        self.table[0,3] = Queen("Black Queen","bq",0,self, (0,3))
        self.table[0,4] = King("Black King","bK",0,self, (0,4))
         
        self.table[0,5] = Bishop("Black Bishop 2","bb",0,self, (0,5))
        self.table[0,6] = Knight("Black Knight 2","bk",0,self, (0,6))
        self.table[0,7] = Rook("Black Rook 2","br",0,self, (0,7))
        for i in range(8):
            self.table[1,i] = Pawn(("Black Pawn "+str(i+1)),"bp",0,self,(1,i))
        for i in range(8):
            self.table[6,i] = Pawn(("White Pawn "+str(8-i)),"wp",1,self,(6,i))
        self.table[7,0] = Rook("White Rook 2","wr",1,self, (7,0))
        self.table[7,1] = Knight("White Knight 2","wk",1,self, (7,1))
        self.table[7,2] = Bishop("White Bishop 2","wb",1,self,(7,2))
        self.table[7,3] = Queen("White Queen","wq",1,self, (7,3))
        self.table[7,4] = King("White King","wK",1,self, (7,4))
        self.table[7,5] = Bishop("White Bishop 1","wb",1,self, (7,5))
        self.table[7,6] = Knight("White Knight 1","wk",1,self, (7,6))
        self.table[7,7] = Rook("White Rook 1","wr",1,self, (7,7))
        
        
        self.update_v()
        print(self.print_board())
        

    def get_alphabetical(self):
        return self.alphalist
    
    def get_numerical(self):
        return self.nums

    def get_turn(self):
        return self.turn
    
    def get_logs(self):
        return self.logs
    
    def set_turn(self,t):
        self.turn = t
    
    def get_finished(self):
        return self.finished

    def set_finished(self,f):
        self.finished=f
    
    def get_table(self):
        return self.table
    def update_v(self):
        self.vtable =  np.zeros((8, 8), dtype=object)
        for i in range(8):
            for j in range(8):
                if(self.table[i,j]!=0):
                    self.vtable[i,j] = self.table[i,j].get_id()
                else:
                    self.vtable[i,j] = ".."
    
    def print_board(self):
        st = ""
        lst = "       -----------------------------------------------"
        for i in range(9):
            for j in range(9):
                if(i == 0):
                    if( j == 0):
                        st = st + "   \  "
                    else:
                        st = st + "   " + self.alphalist[j-1] + "  "
                else:
                    if(j==0):
                        st = st + "   " + self.nums[i-1] + "  "
                    else:
                        if(self.table[i-1,j-1]!=0):
                            st = st + "| " + self.table[i-1,j-1].get_id()+ " |"
                        else:
                            st = st + "| .. |"
            st = st + "\n"
            st = st + lst + "\n"
        return st
    
    def get_name(self):
      return self.name

    def step(self,p1,p2):
        buff = self.table[p1[0],p1[1]]
        if buff !=0 :
            if (buff.get_team()==self.turn):
               
                if p2 in buff.valid_moves():
                
                    target = self.table[p2[0],p2[1]]
                    if(target !=0 ):
                        if(target.get_id() == "wK"):
                            self.winner = 1
                            self.finished = True
                        if(target.get_id() == "bK"):
                            print("hehe voi")
                            self.winner = 0
                            self.finished = True

                    buff = self.table[p1[0],p1[1]]
                    self.table[p2[0],p2[1]] = buff
                    buff.set_position(p2)
                    buff.set_moved_one()
                    self.table[p1[0],p1[1]] = 0
                    if(target !=0 ):
                        self.logs.append("player " + str(self.turn) + " " + buff.get_name() + " at " + 
                        str( self.alphalist[p1[1]]) + str(self.nums[p1[0]]) + " to " + target.get_name() + " at " 
                        + str(self.alphalist[p2[1]])  + str(self.nums[p2[0]])+ "\n")
                    else: 
                        self.logs.append("player " + str(self.turn) + " " + buff.get_name() + " at " + 
                        self.alphalist[p1[1]] + str(self.nums[p1[0]]) + " to " 
                        + str(self.alphalist[p2[1]])  + str(self.nums[p2[0]]) + "\n")

                    self.update_v()
                    if(self.turn ==0):
                        self.turn=1
                    else:
                        self.turn=0

                    return True
        return False

    def get_vtable(self):
        return self.vtable
    
    def get_winner(self):
        return self.winner
            

    
   
  

