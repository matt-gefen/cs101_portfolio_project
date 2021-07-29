common_deck = {
    1: {
        'name' : 'Warrior', 
        'represents' : 'Strength and force personified—violence—those who use force to accomplish their goals'},
    2: {
        'name' : 'Avenger',
        'represents' : 'Justice and revenge for great wrongs—those on a quest to rid the world of great evil'},
    3: {
        'name' : 'Paladin',
        'represents' : 'Just and noble warriors—those who live by a code of honor and integrity'},
    4: {
        'name': 'Soldier',
        'represents':'War and sacrifice—the stamina to endure great hardship'},
    5: {
        'name': 'Mercenary',
        'represents': 'Inner strength and fortitude—those who fight for power or wealth'},
    6: {
        'name': 'Myrmidion',
        'represents': 'Great heroes—a sudden reversal of fate—the triumph of the underdog over a mighty enemy'},
    7: {
        'name': 'Berserker',
        'represents': 'The brutal and barbaric side of warfare—bloodlust—those with a bestial nature'},
    8: {
        'name': 'Hooded One',
        'represents': 'Bigotry, intolerance, and xenophobia—a mysterious presence or newcomer'},
    9: {
        'name': 'Dictator',
        'represents': 'All that is wrong with government and leadership—those who rule through fear and violence'},
    10:{
        'name': 'Torturer',
        'represents':'The coming of suffering or merciless cruelty—one who is irredeemably evil or sadistic'},
    11:{
        'name': 'Wizard', 
        'represents':'Mystery and riddles—the unknown—those who crave magical power and great knowledge'},
    12:{
        'name': 'Transmuter', 
        'represents':'A new discovery—the coming of unexpected things—unforeseen consequences and chaos'},
    13:{
        'name': 'Diviner', 
        'represents':'The pursuit of knowledge tempered by wisdom—truth and honesty—sages and prophecy'},
    14:{
        'name': 'Enchanter', 
        'represents':'Inner turmoil that comes from confusion, fear of failure, or false information'},
    15:{
        'name': 'Elementalist', 
        'represents':'The triumph of nature over civilization—natural disasters and bountiful harvests'},
    17:{
        'name': 'Evoker', 
        'represents':'Magical or supernatural power that can\'t be controlled—magic for destructive ends'},
    18:{
        'name': 'Illusionist', 
        'represents':'Lies and deceit—grand conspiracies—secret societies—the presence of a dupe or a saboteur'},
    19:{
        'name': 'Necromancer', 
        'represents':'Unnatural events and unhealthy obsessions—those who follow a destructive path'},
    20:{
        'name': 'Conjurer', 
        'represents':'The coming of an unexpected supernatural threat—those who think of themselves as gods'},
    21:{
        'name': 'Rogue', 
        'represents':'Anyone for whom money is important—those who believe money is the key to their success'},
    22:{
        'name': 'Swashbuckler', 
        'represents':'Those who like money yet give it up freely—likable rogues and rapscallions'},
    23:{
        'name': 'Philanthropist', 
        'represents':'Charity and giving on a grand scale—those who use wealth to fight evil and sickness'},
    24:{
        'name': 'Trader', 
        'represents':'Commerce—smuggling and black markets—fair and equitable trades'},
    25:{
        'name': 'Merchant', 
        'represents':'A rare commodity or business opportunity—deceitful or dangerous business transactions'},
    26:{
        'name': 'Guild Member', 
        'represents':'Like-minded individuals joined together in a common goal—pride in one\'s work'},
    27:{
        'name': 'Beggar', 
        'represents':'Sudden change in economic status or fortune'},
    28:{
        'name': 'Thief', 
        'represents':'Those who steal or burgle—a loss of property, beauty, innocence, friendship, or reputation'},
    29:{
        'name': 'Tax Collector', 
        'represents':'Corruption—honesty in an otherwise corrupt government or organization'},
    30:{
        'name': 'Miser', 
        'represents':'Hoarded wealth—those who are irreversibly unhappy or who think money is meaningless'},
    31:{
        'name': 'Priest', 
        'represents':'Enlightenment—those who follow a deity, a system of values, or a higher purpose'},
    32:{
        'name': 'Monk', 
        'represents':'Serenity—inner strength and self-reliance—supreme confidence bereft of arrogance'},
    33:{
        'name': 'Missionary', 
        'represents':'Those who spread wisdom and faith to others—warnings of the spread of fear and ignorance'},
    34:{
        'name': 'Healer', 
        'represents':'Healing—a contagious illness, disease, or curse—those who practice the healing arts'},
    35:{
        'name': 'Shepherd', 
        'represents':'Those who protect others—one who bears a burden far too great to be shouldered alone'},
    36:{
        'name': 'Druid', 
        'represents':'The ambivalence and cruelty of nature and those who feel drawn to it—inner turmoil'},
    37:{
        'name': 'Anarchist', 
        'represents':'A fundamental change brought on by one whose beliefs are being put to the test'},
    38:{
        'name': 'Charlatan', 
        'represents':'Liars—those who profess to believe one thing but actually believe another'},
    39:{
        'name': 'Bishop', 
        'represents':'Strict adherence to a code or a belief—those who plot, plan, and scheme'},
    40:{
        'name': 'Traitor', 
        'represents':'Betrayal by someone close and trusted—a weakening or loss of faith'}
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

