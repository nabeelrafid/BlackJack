####################################################################
# Name:Nabeel Rafid                                                #
# Date:21/01/2016                                                  #
# File Name:blackjack.py                                           #
# Description:This is a game of Blackjack. The goal of the game is #
# to get a total score of 21 without busting(getting a score higher#
# than 21) If both the dealer and the player obtain a score that is#
# less than 21, the one with the most points win.                  #
#                                                                  # 
####################################################################

from graphics import *
from button import *
import random
import time
import winsound

#Display a message when the player busts
def bust():
    hitButton.deactivate()
    standButton.deactivate()
    dcard2.draw(win)
    bust = Text(Point(600, 500), "Bust")
    bust.setSize(36)
    bust.setFill("red")
    
    bust.draw(win)

    winsound.PlaySound("Lose_Music.wav", 1)
    for i in range(6):
        t(0.07)
        bust.setFill("black")
        t(0.07)
        bust.setFill("red")
    bust.undraw()
    rect.undraw()

#Initiate cards to a full deck and corresponding values in a second list
def init_cards():

    value = []
    card_list = []
    
    for i in "ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king":
        for j in "_of_clubs.png", "_of_diamonds.png", "_of_hearts.png",\
        "_of_spades.png":
            card_list.append(str(i)+ j)
            
    value += [11] * 4
    for i in range(2, 11):
        for j in range(4):
            value.append(i)
    value += [10] * 12

    return card_list, value

#Rename the time.sleep function for easier typing
def t(n):
    time.sleep(n)

#Check the status of the game and display message accordingly
def checkWin(player_score, dealer_score):
    if sum(player_score) >= 21 or sum(dealer_score) >= 21:
        hitButton.deactivate()
        standButton.deactivate()
        if sum(player_score) == 21 and sum(dealer_score) != 21:
            hitButton.deactivate()
            standButton.deactivate()
            blackjack = Text(Point(600, 500), "BLACKJACK")
            blackjack.setSize(36)
            blackjack.setFill("yellow")
            blackjack.draw(win)

            winsound.PlaySound("Win_Music.wav", 1)
            for i in range(15):
                t(0.07)
                blackjack.setFill("black")
                t(0.07)
                blackjack.setFill("yellow")
            blackjack.undraw()
            rect.undraw()
            rect_lost.undraw()
            return "Black Jack"
        
        elif sum(player_score) > 21 or sum(dealer_score) == 21 and \
           sum(player_score) != 21:
            hitButton.deactivate()
            standButton.deactivate()
            lost = Text(Point(600, 500), "You Lost")
            lost.setSize(36)
            lost.setFill("red")
            lost.draw(win)

            winsound.PlaySound("Lose_Music.wav", 1)
            for i in range(15):
                t(0.07)
                lost.setFill("black")
                t(0.07)
                lost.setFill("red")
            lost.undraw()
            rect.undraw()
            return "Player Lost"
        elif sum(dealer_score) > 21:
            hitButton.deactivate()
            standButton.deactivate()
            winner = Text(Point(600, 500), "You win")
            winner.setSize(36)
            winner.setFill("yellow")
            winner.draw(win)

            winsound.PlaySound("Win_Music.wav", 1)
            for i in range(15):
                t(0.07)
                winner.setFill("black")
                t(0.07)
                winner.setFill("yellow")
            winner.undraw()
            rect.undraw()
            rect_lost.undraw()
            return "Player Win"
        
        else:
            hitButton.deactivate()
            standButton.deactivate()
            push = Text(Point(600, 500), "Push")
            push.setSize(36)
            push.setFill("LightGoldenRod2")
            push.draw(win)
            for i in range(15):
                t(0.07)
                push.setFill("black")
                t(0.07)
                push.setFill("LightGoldenRod2")
            push.undraw()
            return "Push"
        
    elif sum(player_score) > sum(dealer_score):
        hitButton.deactivate()
        standButton.deactivate()
        winner = Text(Point(600, 500), "You win")
        winner.setSize(36)
        winner.setFill("yellow")
        winner.draw(win)

        winsound.PlaySound("Win_Music.wav", 1)
        for i in range(15):
            t(0.07)
            winner.setFill("black")
            t(0.07)
            winner.setFill("yellow")
        winner.undraw()
        rect.undraw()
        rect_lost.undraw()
        return "Player Win"
    
    elif sum(player_score) < sum(dealer_score):
        hitButton.deactivate()
        standButton.deactivate()
        lost = Text(Point(600, 500), "You Lost")
        lost.setSize(36)
        lost.setFill("red")
        lost.draw(win)

        winsound.PlaySound("Lose_Music.wav", 1)
        for i in range(15):
            t(0.07)
            lost.setFill("black")
            t(0.07)
            lost.setFill("red")
        lost.undraw()
        rect.undraw()
        return "Player Lost"
    else:
        hitButton.deactivate()
        standButton.deactivate()
        push = Text(Point(600, 500), "Push")
        push.setSize(36)
        push.setFill("LightGoldenRod2")
        push.draw(win)

        for i in range(15):
            t(0.07)
            push.setFill("black")
            t(0.07)
            push.setFill("LightGoldenRod2")
        push.undraw()
        return "Push"

#Setup the GUI and start the music
def setupGUI():
    global win, hitButton, standButton, quitButton, player_label, dealer_label\
           , againButton
    
    win = GraphWin("Black Jack", 1200, 650)
    win.setCoords(0, 0, 1200, 650)
    winsound.PlaySound("Welcome_Music.wav", 1)

    #Welcome Screen
    welcome = Image(Point(600, 325), "blackjackwelcome.png")
    welcome.draw(win)
    t(0.5)
    welcome_label = Text(Point(150, 50), "Click anywhere to begin")
    welcome_label.setSize(16)
    welcome_label.setFill("yellow")
    welcome_label.draw(win)

    win.getMouse()

    winsound.PlaySound("Casino_Ambiance_Music.wav", 1)
    background = Image(Point(600, 325), "Table.png")
    background.draw(win)

    player_label = Text(Point(250, 475), "Player")
    player_label.setSize(36)
    dealer_label = Text(Point(950, 475), "Dealer")
    dealer_label.setSize(36)
    player_label.draw(win)
    dealer_label.draw(win)

    hitButton = Button(win, Point(450, 100), 75, 35, "Hit")
    standButton = Button(win, Point(750, 100), 75, 35, "Stand")
    quitButton = Button(win, Point(1100, 25), 75, 35, "Quit")
    againButton = Button(win, Point(1100, 75), 85, 35, "Play Again")
    quitButton.activate()

    
#Draws four cards
def setupGame():

    global dealer_card, cards, card_values, card1, card2, dcard1, dcard2, rect,\
           rect_lost, cover

    rect_win = Rectangle(Point(25, 400), Point(1175, 150))
    rect_win.setFill("chartreuse1")
    rect_win.draw(win)
    
    rect_lost = Rectangle(Point(25, 400), Point(1175, 150))
    rect_lost.setFill("firebrick4")
    rect_lost.draw(win)
    
    rect = Rectangle(Point(25, 400), Point(1175, 150))
    rect.setFill("DarkSeaGreen4")
    rect.draw(win)

    deck = Image(Point(600, 275), "stock.png")
    t(0.2)
    deck.draw(win)
    t(0.5)
    
    p_score = []
    d_score = []

    cards, card_values = init_cards()

    card_num = random.randint(0, len(cards)-1) 
    card1 = Image(Point(175, 275), cards[card_num])
    card1.draw(win)

    p_score.append(card_values[card_num])
    del cards[card_num]
    del card_values[card_num]

    card_num = random.randint(0, len(cards)-1) 
    card2 = Image(Point(325, 275), cards[card_num])
    card2.draw(win)

    p_score.append(card_values[card_num])
    del cards[card_num]
    del card_values[card_num]

    card_num = random.randint(0, len(cards)-1) 
    dcard1 = Image(Point(875, 275), cards[card_num])
    dcard1.draw(win)
    d_score.append(card_values[card_num])
    del cards[card_num]
    del card_values[card_num]

    cover = Image(Point(1025, 275), "stock.png")
    cover.draw(win)

    card_num = random.randint(0, len(cards)-1) 
    dcard2 = Image(Point(1025, 275), cards[card_num])
    d_score.append(card_values[card_num])
    del cards[card_num]
    del card_values[card_num]

    hitButton.activate()
    standButton.activate()

    return p_score, d_score

#Check to see if there are any aces in the hand
def check_ace(plist):
    print(plist)
    for i in range(len(plist)):
        if plist[i] == 11:
            return True, i
    return False, i

    
#############################################
# Main awesome program                      #
#############################################


setupGUI()
player_score, dealer_score = setupGame()

count = 0
dcount = 0
distance = 350
reset = False


pt = win.getMouse()

while not quitButton.clicked(pt):


    #Check to see if hit button has been clicked
    if hitButton.clicked(pt):
        count += 1
        hitButton.deactivate()#Make it seem like it has actually been clicked

        #Slide the first two cards over
        if count == 1:
            for i in range(70):
                card1.move(-1, 0)
            for i in range(175):
                card2.move(-1, 0)
        #Select random cards from a list and slide them over when hit is clicked        
        card_num = random.randint(0, len(cards)-1) 
        play_card = Image(Point(550, 275), cards[card_num])
        play_card.draw(win)
        player_score.append(card_values[card_num])
        del cards[card_num]
        del card_values[card_num]
        for i in range(distance):
            play_card.move(-1, 0)
        hitButton.activate()
        distance -= 50
        print(player_score)
        if sum(player_score) > 21:
            print(player_score)
            ace_stat, index = check_ace(player_score)
            #Check if there is an ace in the hand and make it the best hand
            if not ace_stat:
                reset = True
                bust()
            
            else:
                player_score[index] = 1

        #Check for blackjack
        elif sum(player_score) == 21:
            reset = True
            dcard2.draw(win)
            checkWin(player_score, dealer_score)
            
    #Check if stand button has been clicked
    if standButton.clicked(pt):
        reset = True
        distance = 400
        standButton.deactivate()
        hitButton.deactivate()
        dcard2.draw(win)
        cover.undraw()

        #Generate cards until total score hits 17 or higher
        while not sum(dealer_score) >= 17 and player_score != 21: 
            dcount +=1
            if dcount == 1:
                for i in range(70):
                    dcard2.move(1, 0)
                for i in range(175):
                    dcard1.move(1, 0)

                dcard1.undraw()
                dcard1.draw(win)
                
                    
            card_num = random.randint(0, len(cards)-1) 
            deal_card = Image(Point(600, 275), cards[card_num])
            deal_card.draw(win)
            dealer_score.append(card_values[card_num])
            del cards[card_num]
            del card_values[card_num]
            for i in range(distance):
                deal_card.move(1, 0)
            
            distance -= 50
            print(dealer_score)
            if sum(dealer_score) > 21:
                print(dealer_score)
                ace_stat, index = check_ace(dealer_score)  
                if not ace_stat:
                    reset = True 
                
                else:
                    dealer_score[index] = 1
                    print(dealer_score)

                
        print(player_score)
        print(dealer_score)
        print(sum(player_score))
        print(sum(dealer_score))
        
        
        result = checkWin(player_score, dealer_score)
        print(result)
        
    #Check to see if round has ended
    if reset == True:
        againButton.activate()
        #Check to see if play again button has been clicked
        if againButton.clicked(pt):
            reset = False
            count = 0
            dcount = 0
            distance = 350
            dcard2.undraw()
            winsound.PlaySound("Casino_Ambiance_Music.wav", 1)
            player_score, dealer_score = setupGame()
            
            againButton.deactivate()

        

            
            
    pt = win.getMouse()


#End the music and close the window    
winsound.PlaySound(None, 1)
win.close()


