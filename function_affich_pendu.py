def afficher_pendu(nb_essais):
    # Afficher le visuel du pendu en fonction des essais restants
    pendu = [
        '''
           +---+
               |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           O   |
               |
               |
               |
        =========
        ''',
        '''
           +---+
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           +---+
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           +---+
           O   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           +---+
           O   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           +---+
           O   |
          /|\\  |
          / \\  |
               |
        =========
        '''
    ]
    print(pendu[nb_essais])