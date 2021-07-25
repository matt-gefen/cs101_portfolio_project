low_deck = {}

high_deck = {}
# {
#     'Artifact':'The importance of some physical object that must be obtained, protected, or destroyed at all costs'}

drawings= {
    1:['This card tells of history. Knowledge of the ancient will help you better understand your enemy.','The Tome of Strahd', low_deck],
    2:['This card tells of a powerful force for good and protection, a holy symbol of great hope.','The Holy Symbol of Ravenkind', low_deck],
    3:['This is a card of power and strength. It tells of a weapon of vengeance: a sword of sunlight.','The Sunsword', low_deck],
    4:['This card sheds light on one who will help you greatly in the battle against darkness.','Strahd\'s Enemy', high_deck],
    5:['Your enemy is a creature of darkness, whose powers are beyond mortality. This card will lead you to him!','Strahd\'s Ravenloft Location', high_deck]}

# testing the output of the player-side explainations of each card in the reading.
for i in range(1,6):
    print(drawings[i][0])

