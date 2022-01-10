from math import trunc
import random


class poke():
    def __init__(self) -> None:
        super().__init__()
        self.Isshuffle = 0
        self.Cardlibrary = [
            {'symbol': "♠A ",'value': 14},
            {'symbol': "♠2 ",'value': 15},
            {'symbol': "♠3 ",'value': 3},
            {'symbol': "♠4 ",'value': 4},
            {'symbol': "♠5 ",'value': 5},
            {'symbol': "♠6 ",'value': 6},
            {'symbol': "♠7 ",'value': 7},
            {'symbol': "♠8 ",'value': 8},
            {'symbol': "♠9 ",'value': 9},
            {'symbol': "♠10",'value': 10},
            {'symbol': "♠J ",'value': 11},
            {'symbol': "♠Q ",'value': 12},
            {'symbol': "♠K ",'value': 13},
            {'symbol': "♥A ",'value': 14},
            {'symbol': "♥2 ",'value': 15},
            {'symbol': "♥3 ",'value': 3},
            {'symbol': "♥4 ",'value': 4},
            {'symbol': "♥5 ",'value': 5},
            {'symbol': "♥6 ",'value': 6},
            {'symbol': "♥7 ",'value': 7},
            {'symbol': "♥8 ",'value': 8},
            {'symbol': "♥9 ",'value': 9},
            {'symbol': "♥10",'value': 10},
            {'symbol': "♥J ",'value': 11},
            {'symbol': "♥Q ",'value': 12},
            {'symbol': "♥K ",'value': 13},
            {'symbol': "♣A ",'value': 14},
            {'symbol': "♣2 ",'value': 15},
            {'symbol': "♣3 ",'value': 3},
            {'symbol': "♣4 ",'value': 4},
            {'symbol': "♣5 ",'value': 5},
            {'symbol': "♣6 ",'value': 6},
            {'symbol': "♣7 ",'value': 7},
            {'symbol': "♣8 ",'value': 8},
            {'symbol': "♣9 ",'value': 9},
            {'symbol': "♣10",'value': 10},
            {'symbol': "♣J ",'value': 11},
            {'symbol': "♣Q ",'value': 12},
            {'symbol': "♣K ",'value': 13},
            {'symbol': "♦A ",'value': 14},
            {'symbol': "♦2 ",'value': 15},
            {'symbol': "♦3 ",'value': 3},
            {'symbol': "♦4 ",'value': 4},
            {'symbol': "♦5 ",'value': 5},
            {'symbol': "♦6 ",'value': 6},
            {'symbol': "♦7 ",'value': 7},
            {'symbol': "♦8 ",'value': 8},
            {'symbol': "♦9 ",'value': 9},
            {'symbol': "♦10",'value': 10},
            {'symbol': "♦J ",'value': 11},
            {'symbol': "♦Q ",'value': 12},
            {'symbol': "♦K ",'value': 13},
            {'symbol': "§j ",'value': 16},
            {'symbol': "§J ",'value': 17}
        ]
        self.user1Card = []
        self.user2Card = []
        self.user3Card = []
        self.underCard = []
        self.cardDraw = []
        self.cardDrawnum = 0

    def DrawCard(self, user):
        cardnum = 0
        drawcard = False
        while (drawcard == False):
            cardnum = random.randint(0, 53)
            drawcard = True
            for i in self.cardDraw:
                if (i == cardnum):
                    drawcard = False
        self.cardDraw.append(cardnum)
        self.cardDrawnum = self.cardDrawnum + 1
        if (user == 0):
            self.user1Card.append(self.Cardlibrary[cardnum])
        if (user == 1):
            self.user2Card.append(self.Cardlibrary[cardnum])
        if (user == 2):
            self.user3Card.append(self.Cardlibrary[cardnum])
        if (user == 3):
            self.underCard.append(self.Cardlibrary[cardnum])

    def DrawCards(self):
        self.user1Card = []
        self.user2Card = []
        self.user3Card = []
        self.underCard = []
        self.cardDraw = []
        self.cardDrawnum = 0
        user = 0
        underCard = 3
        while (self.cardDrawnum < 51):
            user += 1
            user = user % 3
            self.DrawCard(user)
        while (underCard > 0):
            underCard -= 1
            self.DrawCard(3)

    def ShowUser1Card(self):
        print("---USER 1---")
        self.PrintCard(self.user1Card)

    def ShowUser2Card(self):
        print("---USER 2---")
        self.PrintCard(self.user2Card)

    def ShowUser3Card(self):
        print("---USER 3---")
        self.PrintCard(self.user3Card)

    def ShowUnderCard(self):
        print("---UNDER---")
        self.PrintCard(self.underCard)

    def PrintCard(self,Arr):
        Arr = self.sortCard(Arr)
        t = "_"
        d = "|"
        s = "|"
        for i in Arr:
            t += "____"
            d += "___|"
            s += i['symbol'] + "|"
        print(t)
        print(s)
        print(d)
        print()
        return s
    def sortCard(self, Arr):
        check = False
        while (check == False):
            for i in range(len(Arr) - 1):
                if (Arr[i]['value'] > Arr[i + 1]['value']):
                    temp = Arr[i + 1]
                    Arr[i + 1] = Arr[i]
                    Arr[i] = temp
            check = True
            for i in range(len(Arr) - 1):
                if (Arr[i]['value'] > Arr[i + 1]['value']):
                    check = False
        return Arr
    
    def UseCard(self,usrCards,num):
        print("---Use Card---")
        str1 = " "
        index = 0;
        success = False
        card = []
        for i in usrCards:
            str1 = i['symbol']
            str1 = str1.replace("♠","")
            str1 = str1.replace("♥","")
            str1 = str1.replace("♣","")
            str1 = str1.replace("♦","")
            str1 = str1.replace(" ","")
            
            if str1 == num:
                index = usrCards.index(i)
                card.append(i)
                self.PrintCard(card)
                usrCards.remove(i)
                success = True
                break
        if success == False:
            print("出牌失败,查无此牌")
        
# ---USER 1---
# _____________________________________________________________________
# |♠3 |♦5 |♥5 |♦6 |♥6 |♥8 |♥9 |♣9 |♣10|♦10|♣Q |♥Q |♠Q |♠K |♥2 |♣2 |♦2 |
# |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|

# ---USER 2---
# _____________________________________________________________________
# |♥3 |♦4 |♣4 |♣5 |♠6 |♥7 |♦7 |♣8 |♠8 |♦9 |♠9 |♥10|♦J |♥J |♣K |♦A | ♠A|
# |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|

# ---USER 3---
# _____________________________________________________________________
# |♣3 |♥4 |♠4 |♠7 |♣7 |♦8 |♠10|♣J |♠J |♦Q |♦K |♥K |♣A |♥A |♠2 |§J |§J |
# |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|

# ---UNDER---
# _____________
# |♦3 |♠5 |♣6 |
# |___|___|___|