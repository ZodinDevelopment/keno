HELP = {
    'BET': "Increase the current wager by 1 Credit.",
    'WIPE': "Reset the board and numbers and you have picked.",
    'QUICK': """
        Usage:
        QUICK [amount]

        Randomly picks [amount] numbers, 
        if [amount] arg is not provided, defaults to 10 numbers.
    """,
    'PICK': """
        Usage:
        PICK [number]

        Toggles selection of [number] in picks.
    """,
    'START': 'Begin round of play, wagering current BET amount.',
    'SPEED': 'Adjust the game\'s current speed.',
    'SAVE': """
        Usage:
        SAVE [save name]

        Saves current game data to .pkl file.
    """,
    'LOAD': """
        Usage:
        LOAD [save name]

        Loads [save name] save file to current game.
    """,
    'QUIT': 'Exit the game.'              
}
