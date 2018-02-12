import random

class Deck(object):
    ###
    ###A new deck is created once game is on
    ###
    newDeck={"Ace of Hearts":1,"2 of Hearts":2,"3 of Hearts":3,"4 of Hearts":4,"5 of Hearts":5,"6 of Hearts":6,"7 of Hearts":7,"8 of Hearts":8,\
            "9 of Hearts":9,"Jack of Hearts":10,"Queen of Hearts":10,"King of Hearts":10,"Ace of Clubs":1,"2 of Clubs":2,"3 of Clubs":3,\
            "4 of Clubs":4,"5 of Clubs":5,"6 of Clubs":6,"7 of Clubs":7,"8 of Clubs":8,"9 of Clubs":9,"Jack of Clubs":10,\
            "Queen of Clubs":10,"King of Clubs":10,"Ace of Diamonds":1,"2 of Diamonds":2,"3 of Diamonds":3,"4 of Diamonds":4,"5 of Diamonds":5,\
            "6 of Diamonds":6,"7 of Diamonds":7,"8 of Diamonds":8,"9 of Diamonds":9,"Jack of Diamonds":10,"Queen of Diamonds":10,"King of Diamonds":10,\
            "Ace of Spades":1,"2 of Spades":2,"3 of Spades":3,"4 of Spades":4,"5 of Spades":5,"6 of Spades":6,"7 of Spades":7,"8 of Spades":8,\
            "9 of Spades":9,"Jack of Spades":10,"Queen of Spades":10,"King of Spades":10,"10 of Hearts":10,"10 of Clubs":10,"10 of Spades":10,"10 of Diamond":10}

class Player(object):

    def __init__(self,name,totalMoney):
        self.name=name
        self.totalMoney=totalMoney

    def getMoney(self):
        return self.totalMoney

    def setMoney(self,totalMoney):
        self.totalMoney=totalMoney

def playerInput():
    pInput=""
    while not pInput.startswith("s") or not pInput.startswith("h"):
            pInput=input("Would you like to Stand or Hit it: ")
            return pInput.lower()

def playGame(a,player):
    pTotal=0
    dTotal=0
    tMoney=int(player.getMoney())

    while not pTotal==21:
        #pass not pTotal==21:
        rList=[]
        printCard=[]

        for k in a.keys():
            rList.append(k)

        print("Let's shuffle the cards..")
        random.shuffle(rList)
        bet=int(input("How much money do you wanna bet?\n"))
        print("Player's card: \n")
        pCard1=rList.pop()
        printCard.append(pCard1)
        print(pCard1)               #print the first player card
        pTotal+=int(a[pCard1])
        print("Dealer's card: \n")
        dCard1=rList.pop()
        print(dCard1)               #print dealer's first card
        dTotal+=int(a[dCard1])
        print("Player's card: \n")
        pCard2=rList.pop()
        printCard.append(pCard2)
        print(pCard1,"\t",pCard2)   #print player's both cards
        pTotal+=int(a[pCard2])
        #print("Dealer's card: \n")
        dCard2=rList.pop()
        print("Dealer's second card is hidden...\n")   #Dealer's second card will be hidden
        dTotal+=int(a[dCard2])
        pInput=playerInput()

        while pInput.startswith("h"):
            print("Your next card..")
            pCard=rList.pop()
            printCard.append(pCard)
            length=(len(printCard) +1)

            for n in range(0,length):
                print(printCard[n],"\t")   #print player's all cards
                pTotal+=int(a[pCard])

                if(pTotal>21):
                    print(pTotal)
                    print("You are busted.. Your money is now mine bitch\n")
                    tMoney-=bet
                    player.setMoney(tMoney)
                    tMoney=player.getMoney()
                    print("You have ",tMoney," in total")
                    break
                    break

                else:
                    continue
                    pInput=playerInput()

        while pInput.startswith("s"):
            print("Revealing delear's hand: \n")
            print(dCard1,"\t",dCard2)
            print("Dealer's total is: ",dTotal)

            if(dTotal==21):
                print("Dealer hits blackjack, you lose\n")
                tMoney-=bet
                player.setMoney(tMoney)
                tMoney=player.getMoney()
                print("You have ",tMoney," in total")
                break

            else:

                if(pTotal>dTotal):
                    bet*=1.5
                    print("Congratulations..",name," you won.\n","You get ",bet)
                    tMoney+=bet
                    player.setMoney(tMoney)
                    tMoney=player.getMoney()
                    print("You have ",tMoney," in total")
                    break
                    break

                elif(dTotal>pTotal):
                    print("You lose sucker...\n")
                    tMoney-=bet
                    player.setMoney(tMoney)
                    tMoney=player.getMoney()
                    print("You have ",tMoney," in total")
                    break

                else:
                    print("Oops it's a bust..\n You can keep your money")
                    print("You have ",tMoney," in total")
                    break

    print("Whoa you hit a blackjack......")
    bet*=2
    print("You won ",bet)
    tMoney=player.totalMoney
    tMoney+=bet
    player.setMoney(tMoney)
    tMoney=player.getMoney()
    print("You have in total ",tMoney)

def playAgain():
    pInput=""
    while not pInput=="y" or not pInput=="n":
        pInput=input("Do you wish to play again?(y/n): ")
        return pInput.lower()

A=Deck()
a=A.newDeck
status=1
name=input("Whats your name? \n")
tMoney=input("\nHow much money do you wanna play with? \n")
player=Player(name,tMoney)
while status:
    playGame(a,player)
    if(playAgain()=="y"):
        continue
    else:
        status=0
