# mlproject/lib.py

def try_me():

    lst = ['ronaldo', 'cristiano', 'cristiano ronaldo']
    while True:
        best_player = input('Who is the GOAT of football? ')
        if best_player.lower() not in lst:
            print('Nope! Try again. (tip: it\'s portuguese and try to write only one name)')
        else:
            return 'SIIIIIIIIIIIIIIIIII'