from game import Game


try:

    game=Game()
    game.run()

except Exception as e:

    print("ERROR:",e)
    