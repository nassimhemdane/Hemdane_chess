import sys
from GameState import GameState
def main():
    if(len(sys.argv)>1):
        f = open(sys.argv[1],"w")
    else: 
        f = open("test.txt","w")
    gs = GameState()
    while(not gs.get_finished()):
        sturn = ""
        if(gs.get_turn() == 0):
            sturn = "Black moves"
        else:
            sturn = 'White moves'
        pos1= input(sturn + "\n" + "Enter piece position: ")
        pos2 = input("Enter destination: ")
        if ((pos1[0] in gs.get_alphabetical()) and (pos1[1] in gs.get_numerical()) 
        and (pos2[0] in gs.get_alphabetical()) and (pos2[1] in gs.get_numerical())):
            p1 = (gs.get_numerical().index(pos1[1]),gs.get_alphabetical().index(pos1[0]))
            p2 = (gs.get_numerical().index(pos2[1]),gs.get_alphabetical().index(pos2[0]))
            if(not gs.step(p1,p2)):
                print("Impossible move")
            
            print(gs.print_board())
        else:
            print("error in input")
    if(gs.get_winner ==0 ):
        print("gg wp for the player 0!")
    else:
        print("gg wp for the player 1!")
    for i in gs.get_logs():
        f.write(i)
    f.close
    

    

if __name__=="__main__":
    main()