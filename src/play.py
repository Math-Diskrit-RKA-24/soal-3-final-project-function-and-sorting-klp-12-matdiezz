import game

game.initPlayers()
p1=game.createNewPlayer("lala", damage=18, defensePower=4)
p2=game.createNewPlayer("lulu", damage=12, defensePower=7)
p3=game.createNewPlayer("lolo", damage=15, defensePower=8)
p4=game.createNewPlayer("lili", damage=21, defensePower=11)
p5=game.createNewPlayer("abdul", damage=16, defensePower=13)

game.addPlayer(p1)
game.addPlayer(p2)
game.addPlayer(p3)
game.addPlayer(p4)
game.addPlayer(p5)

print("REGISTRANT:", [player['name'] for player in game.PlayerList])
print("Lolo has a stomach ache, so he can't come to the match")

game.removePlayer("lolo")

print("\nPlayer that entered the game:", game.PlayerList)

print("\nGAMEEEE STAAAAARTT")
print("lala attack lili")
game.attackPlayer(p1, p4) #LILI GA NYALAIN DEFENSENYA JADI DRECIEVE=18, HEALTH LILI=82 SCORE LALA=18

print("lili attack abdul, but he has activated his defense first")
game.setPlayer(p5, "defense", True)
game.attackPlayer(p4,p5) #DRECEIVE ABDUL= 21-13=8, HEALTH ABDUL=100-8=92, SCORE LILI= 8 

print("abdul attack lulu")
game.attackPlayer(p5, p2) #DRECEIVE LULU=16, HEALTHNYA LULU=100-16=84, SCORE ABDUL= 16

print("lulu attack lala, but lala already activated her defense")
game.setPlayer(p1, "defense", True)
game.attackPlayer(p2,p1) #DRECEIVE LALA= 12-4=8, HEALTH LALA=100-8=92, SCORE LULU=8

game.displayMatchResult()

highest_score=max(game.PlayerList, key=lambda p: p["score"])
print("\nCONGRATS TO", highest_score["name"], "FOR ACHIEVING FIRST PLACE IN THIS GAME")
