def board(x_state,z_state):
    for i in range(9):

        if i == 2 or i == 5 or i == 8:
              sep = "\n"
        else:
              sep = "||"
        
        if not flag[i]:
            if x_state[i]:
                    print(x_state[i],end = sep)
                    if sep == "\n":
                          print("=======")
            else:
                    print(z_state[i],end = sep)
                    if sep == "\n":
                          print("=======")
        else:
            print(i,end = sep)   
            if sep == "\n":
                          print("=======") 

def myMove(action,player1):
    if player1:
            mark = choice1
            state = xState
    else:
            mark = choice2
            state = zState
      
    match action:
                case 0:
                        state[0]=mark
                        flag[actn] = False         
                case 1:
                        state[1]=mark
                        flag[actn] = False
                case 2:
                        state[2]=mark
                        flag[actn] = False
                case 3:
                        state[3]=mark
                        flag[actn] = False
                case 4:
                        state[4]=mark
                        flag[actn] = False
                case 5:
                        state[5]=mark
                        flag[actn] = False
                case 6:
                        state[6]=mark
                        flag[actn] = False
                case 7:
                        state[7]=mark
                        flag[actn] = False
                case 8:
                        state[8]=mark
                        flag[actn] = False
                case default:
                        print("Please enter the integer value which the respective box is denoting.")
        
def baseCond(state,choice):
    if state[0] == choice and state[1] == choice and state[2] == choice:
          return True
    elif state[3] == choice and state[4] == choice and state[5] == choice:
          return True
      
    elif state[6] == choice and state[7] == choice and state[8] == choice:
          return True
      
    elif state[0] == choice and state[3] == choice and state[6] == choice:
          return True
      
    elif state[1] == choice and state[4] == choice and state[7] == choice:
          return True
      
    elif state[2] == choice and state[5] == choice and state[8] == choice:
          return True
      
    elif state[2] == choice and state[4] == choice and state[6] == choice:
          return True
      
    elif state[0] == choice and state[4] == choice and state[8] == choice:
          return True
    else:
          return False  


if __name__ == "__main__":
      
    xState = [None, None, None, None, None, None, None, None, None]
    zState = [None, None, None, None, None, None, None, None, None]
    global flag 
    flag = [True, True, True, True, True, True, True, True, True]
    
    print("Welcome to TIC TAC TOE")
   
    global choice1, choice2
   
    while True:
        
        choice1 = input("Player 1 how do you want to move || \t X or 0\n")
        
        if choice1 == "X" or choice1 == "0":
            if choice1 == "X":
                choice2 = "0"
                break
            else:
                choice2 = "X"
                break
        else:
            print("Comply with the options provided...")

    player1 = True

    while True:
        x = baseCond(xState,choice1)
        z = baseCond(zState,choice2)
        if x:
            print("CONGRATULATIONS!!!  Player1 won...")
            break
        elif z:
            print("CONGRATULATIONS!!!  Player2 won...")
            break
        else:
              if True not in flag:
                    print("OOps...You both are smart...it resulted in porridge >_<")
                    break
        
        board(xState,zState)
        
        
        if player1:
              
            print("Player1 your turn:")
            
            actn = int(input("enter mumber of the box:"))
 
            if actn < 9:
                if flag[actn]:    
                        myMove(actn,player1)
                        player1 = False            
                else:
                        print("You cant perform that action...Go again!")
            else:
                print("Comply with the options provided...")
                      
        else:

            print("Player2 your turn:")
            
            actn = int(input("enter mumber of the box:"))
            
            if actn < 9:
                if flag[actn]:    
                        myMove(actn,player1)
                        player1 = True            
                else:
                        print("You cant perform that action...Go again!")
            else:
                print("Comply with the options provided...")