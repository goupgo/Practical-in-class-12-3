import random
class Main:

    #====================GuessNumber function====================
    def GuessNumber(self, number):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART========
        number = int(number)
        randnum = random.randint(0, number)
        while True:
            opinion = str(input(f'Is {randnum} too high(h), too low(l), or correct(c): '))
            if opinion == 'c':
                break
            elif opinion == 'h':
                randnum = random.randint(0, randnum)
            elif opinion == 'l':
                randnum = random.randint(randnum, number)
                
        print(f"Well done, the comuter guessed your number {randnum} correctly!")
            
        # end def

#==================DO NOT CHANGE THE CODE BELOW=====================
    def main(self):
        number = input("Enter a range for guessed number: ")
        print("OUTPUT")
        self.GuessNumber(number)
        print("FINISH")
main = Main()
main.main()

