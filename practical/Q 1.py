import math
class Main:
    
    #====================f1====================
    def f1(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        inputString_split= inputString.split(', ')
        for move in inputString_split:
            print(move)
        
        # end def


    #====================f2====================
    def f2(self, inputString):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        x = 0
        y = 0
        moves = inputString
        move_list = moves.split(', ')
        
        move_dict = {}
        for move in move_list:
            move_parts = move.split()
            key = move_parts[0]
            value = int(move_parts[1])
            move_dict[key] = value
            
        for movement in move_dict:
            y = move_dict['UP'] - move_dict['DOWN']
            x = - move_dict['LEFT'] + move_dict['RIGHT']
        
        print(round(math.sqrt(x*x + y*y)))
         
        # end def

#================DO NOT CHANGE THE CODE BELOW===============================
    def main(self):
        print(" 1. Test f1 (2 mark)")
        print(" 2. Test f2 (1 mark)")
        print(" Your selection (1 -> 2): ")
        choice = int(input())
        inputString = input()
        print("OUTPUT")
        if choice == 1:
            self.f1(inputString)
        elif choice == 2:
            self.f2(inputString)
        else:
            print("Wrong select")
        print("FINISH")
main = Main()
main.main()

