from common_deck import common_deck
from high_deck import high_deck
import random

common_deck_len = len(common_deck)
high_deck_len = len(high_deck)

class Drawing:
    def __init__(self,reading_num):
        self.reading_num = reading_num
        self.drawings = {
            1:{'reading': 'This card tells of history. Knowledge of the ancient will help you better understand your enemy.', 'name': 'The Tome of  Strahd'},
            2:{'reading': 'This card tells of a powerful force for good and protection, a holy symbol of great hope.','name': 'The Holy Symbol of   Ravenkind'},
            3:{'reading': 'This is a card of power and strength. It tells of a weapon of vengeance: a sword of sunlight.','name':'The Sunsword'},
            4:{'reading': 'This card sheds light on one who will help you greatly in the battle against darkness.','name': 'Strahd\'s Enemy'},
            5:{'reading':'Your enemy is a creature of darkness, whose powers are beyond mortality. This card will lead you to him!','name':'Strahd\'s Ravenloft Location'}}

        if self.reading_num < 4:
            random_drawing = random.randrange(1,common_deck_len+1,1)
            self.card = common_deck[random_drawing]
        else:
            random_drawing = random.randrange(1,high_deck_len+1,1)
            self.card = high_deck[random_drawing] 

    def reading(self):
        return self.drawings[self.reading_num]['reading']
    
    def represents(self):
        return 'The {} represents: {}'.format(self.card['name'], self.card['represents'])

    def player_prediction(self):
        if self.reading_num < 4:
            return self.card['pred_location']
        elif self.reading_num == 4:
            return self.card['enemy_pred']
        else:
            return self.card['castle_location_pred']
    def dm_info(self):
        if self.reading_num < 4:
            return self.card['dm_location']
        elif self.reading_num == 4:
            return self.card['enemy_dm']
        else:
            return self.card['castle_location_dm']

drawing_1 = Drawing(1)
drawing_2 = Drawing(2) 
drawing_3 = Drawing(3) 
drawing_4 = Drawing(4) 
drawing_5 = Drawing(5)

drawings = [drawing_1,drawing_2,drawing_3,drawing_4,drawing_5]

def fortune_telling():
    for drawing in drawings:
        print(drawing.reading(),'\n')
        print(drawing.represents(),'\n')
        print(drawing.player_prediction())
        print('-----')


def initiate_reading():
    print('\nMagic flames cast a reddish glow over the interior of this tent, revealing a low table covered in a black velvet cloth. Glints of light seem to flash from a crystal ball on the table as a hunched figure peers into its depths. As the crone speaks, her voice crackles like dry weeds. "At last you have arrived!" Cackling laughter bursts like mad lightning from her withered lips.\n')

    print('I am Madame Eva, and I sense your threads of your destinies. Tell me, outsiders...Would you like me to divine your futures?\n')
    print('Y or N')
    answer = input()
    if answer == 'Y':
        fortune_telling()
    else:
        print('Then I hope your travels in Barovia will not cause you much suffering. Farewell')


initiate_reading()