common_deck = {
    'Warrior': ['Strength and force personified—violence—those who use force to accomplish their goals'],
    'Avenger':['Justice and revenge for great wrongs—those on a quest to rid the world of great evil'],
    'Paladin':['Just and noble warriors—those who live by a code of honor and integrity'],
    'Soldier':['War and sacrifice—the stamina to endure great hardship'],
    'Mercenary':['Inner strength and fortitude—those who fight for power or wealth'],
    'Myrmidion':['Great heroes—a sudden reversal of fate—the triumph of the underdog over a mighty enemy'],
    'Berserker':['The brutal and barbaric side of warfare—bloodlust—those with a bestial nature'],
    'Hooded One':['Bigotry, intolerance, and xenophobia—a mysterious presence or newcomer'],
    'Dictator':['All that is wrong with government and leadership—those who rule through fear and violence'],
    'Torturer':['The coming of suffering or merciless cruelty—one who is irredeemably evil or sadistic'],
    'Wizard':['Mystery and riddles—the unknown—those who crave magical power and great knowledge'],
    'Transmuter':['A new discovery—the coming of unexpected things—unforeseen consequences and chaos'],
    'Diviner':['The pursuit of knowledge tempered by wisdom—truth and honesty—sages and prophecy'],
    'Enchanter':['Inner turmoil that comes from confusion, fear of failure, or false information'],
    'Abjurer':['Those guided by logic and reasoning—warns of an overlooked clue or piece of information'],
    'Elementalist':['The triumph of nature over civilization—natural disasters and bountiful harvests'],
    'Evoker':['Magical or supernatural power that can\'t be controlled—magic for destructive ends'],
    'Illusionist':['Lies and deceit—grand conspiracies—secret societies—the presence of a dupe or a saboteur'],
    'Necromancer':['Unnatural events and unhealthy obsessions—those who follow a destructive path'],
    'Conjurer':['The coming of an unexpected supernatural threat—those who think of themselves as gods'],
    'Rogue':['Anyone for whom money is important—those who believe money is the key to their success'],
    'Swashbuckler':['Those who like money yet give it up freely—likable rogues and rapscallions'],
    'Philanthropist':['Charity and giving on a grand scale—those who use wealth to fight evil and sickness'],
    'Trader':['Commerce—smuggling and black markets—fair and equitable trades'],
    'Merchant':['A rare commodity or business opportunity—deceitful or dangerous business transactions'],
    'Guild Member':['Like-minded individuals joined together in a common goal—pride in one\'s work'],
    'Beggar':['Sudden change in economic status or fortune'],
    'Thief':['Those who steal or burgle—a loss of property, beauty, innocence, friendship, or reputation'],
    'Tax Collector':['Corruption—honesty in an otherwise corrupt government or organization'],
    'Miser':['Hoarded wealth—those who are irreversibly unhappy or who think money is meaningless'],
    'Priest':['Enlightenment—those who follow a deity, a system of values, or a higher purpose'],
    'Monk':['Serenity—inner strength and self-reliance—supreme confidence bereft of arrogance'],
    'Missionary':['Those who spread wisdom and faith to others—warnings of the spread of fear and ignorance'],
    'Healer':['Healing—a contagious illness, disease, or curse—those who practice the healing arts'],
    'Shepherd':['Those who protect others—one who bears a burden far too great to be shouldered alone'],
    'Druid':['The ambivalence and cruelty of nature and those who feel drawn to it—inner turmoil'],
    'Anarchist':['A fundamental change brought on by one whose beliefs are being put to the test'],
    'Charlatan':['Liars—those who profess to believe one thing but actually believe another'],
    'Bishop':['Strict adherence to a code or a belief—those who plot, plan, and scheme'],
    'Traitor':['Betrayal by someone close and trusted—a weakening or loss of faith']
    }

high_deck = {}
# {
#     'Artifact':'The importance of some physical object that must be obtained, protected, or destroyed at all costs'}

drawings= {
    1:['This card tells of history. Knowledge of the ancient will help you better understand your enemy.','The Tome of Strahd', common_deck],
    2:['This card tells of a powerful force for good and protection, a holy symbol of great hope.','The Holy Symbol of Ravenkind', common_deck],
    3:['This is a card of power and strength. It tells of a weapon of vengeance: a sword of sunlight.','The Sunsword', common_deck],
    4:['This card sheds light on one who will help you greatly in the battle against darkness.','Strahd\'s Enemy', high_deck],
    5:['Your enemy is a creature of darkness, whose powers are beyond mortality. This card will lead you to him!','Strahd\'s Ravenloft Location', high_deck]}

# testing the output of the player-side explainations of each card in the reading.
for i in range(1,6):
    print(drawings[i][0])

