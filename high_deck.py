""" 
The tarokka common deck represents the possible predictions for the two key gameplay predictions :
1. Strahd's Enemy
2. Strahd's Endgame Location in Ravenloft

"""


high_deck = {
    1:{
        'name':'Artifact',
        'represents':'The importance of some physical object that must be obtained, protected, or destroyed at all costs',
        'enemy_pred':'Look for an entertaining man with a monkey. This man is more than he seems.',
        'enemy_dm': 'This card refers to Rictavio, who can be found at the Blue Water Inn in Vallaki (chapter 5, area N2). Normally reluctant to accompany the characters, Rictavio changes his tune if the characters tell him about the card reading. He sheds his disguise and introduces himself as Dr. Rudolph van Richten.The characters might think that Gadof Blinsky, the toymaker of Vallaki (area N7), is the figure they seek, because he has a pet monkey. If they speak to him about this possibility, Blinsky jokes that he and the monkey are "old friends," but if the characters ask him to come with them to fight Strahd, he politely declines. If the characters tell him about the tarokka reading, Blinsky admits that he acquired the monkey from a half-elf carnival ringmaster named Rictavio.',
        'castle_location_pred':'He lurks in the darkness where the morning light once shone—a sacred place.',
        'castle_location_dm':'Strahd faces the characters in the chapel (area K15).'
        },
    2:{
        'name':'Beast',
        'represents':'Great rage or passion—something bestial or malevolent hiding in plain sight or lurking just below the surface',
        'enemy_pred':'A werewolf holds a secret hatred for your enemy. Use her hatred to your advantage.',
        'enemy_dm':'This card refers to the werewolf Zuleika Toranescu (see chapter 15, area Z7). She will accompany the characters if they promise to avenge her mate, Emil, by killing the leader of her pack, Kiril Stoyanovich.',
        'castle_location_pred':'The beast sits on his dark throne.',
        'castle_location_dm':'Strahd faces the characters in the audience hall (area K25).'
        },
    3:{
        'name':'Broken One (A)',
        'represents':'Defeat, failure, and despair—the loss of something or someone important, without which one feels incomplete',
        'enemy_pred':'Your greatest ally will be a wizard. His mind is broken, but his spells are strong.',
        'enemy_dm': 'This card refers to the Mad Mage of Mount Baratok (see chapter 2, area M).',
        'castle_location_pred':'He haunts the tomb of the man he envied above all.',
        'castle_location_dm':'Strahd faces the characters in Sergei\'s tomb (area K85).'
        },
    4:{
        'name':'Broken One (B)',
        'represents':'Defeat, failure, and despair—the loss of something or someone important, without which one feels incomplete',
        'enemy_pred':'I see a man of faith whose sanity hangs by a thread. He has lost someone close to him.',
        'enemy_dm': 'This card refers to Donavich, the priest in the village of Barovia (see chapter 3, area E5). He will not accompany the characters until his son, Doru, is dead and buried.',
        'castle_location_pred':'He haunts the tomb of the man he envied above all.',
        'castle_location_dm':'Strahd faces the characters in Sergei\'s tomb (area K85).'
        },
    5:{
        'name':'Darklord',
        'represents':'A single, powerful individual of an evil nature, one whose goals have enormous and far-reaching consequences',
        'enemy_pred':'Ah, the worst of all truths: You must face the evil of this land alone!',
        'enemy_dm':'There is no NPC who can inspire the characters.',
        'castle_location_pred':'He lurks in the depths of darkness, in the one place to which he must return.',
        'castle_location_dm':'Strahd faces the characters in his tomb (area K86).'},
    6:{
        'name':'Donjon (A)',
        'represents':'Isolation and imprisonment—being so conservative in thinking as to be a prisoner of one\'s own beliefs',
        'enemy_pred':'Search for a troubled young man surrounded by wealth and madness. His home is his prison.',
        'enemy_dm':'This card refers to Victor Vallakovich (see chapter 5, area N3t). Realizing that the characters are the key to his salvation, he enthusiastically leaves home and accompanies them to Castle Ravenloft.',
        'castle_location_pred':'He lurks in a hall of bones, in the dark pits of his castle.',
        'castle_location_dm':'Strahd faces the characters in the hall of bones (area K67).'},
    7:{
        'name':'Donjon (B)',
        'represents':'Isolation and imprisonment—being so conservative in thinking as to be a prisoner of one\'s own beliefs',
        'enemy_pred':'Find a girl driven to insanity, locked in the heart of her dead father\'s house. Curing her madness is key to your success.',
        'enemy_dm':'This card refers to Stella Wachter (see chapter 5, area N4n). She grants the party no benefit unless her madness is cured. With her wits restored, Stella is happy to join the party and leave her rotten family behind.',
        'castle_location_pred':'He lurks in a hall of bones, in the dark pits of his castle.',
        'castle_location_dm':'Strahd faces the characters in the hall of bones (area K67).'},
    8:{
        'name':'Ghost (A)',
        'represents':'The looming past—the return of an old enemy or the discovery of a secret buried long ago',
        'enemy_pred':'I see a fallen paladin of a fallen order of knights. He lingers like a ghost in a dead dragon\'s lair.',
        'enemy_dm':'This card refers to the revenant Sir Godfrey Gwilym (see chapter 7, area Q37). Although initially unwilling to accompany the characters, he will do so if the characters convince him that the honor of the Order of the Silver Dragon can be restored with his help. Doing this requires a successful DC 15 Charisma (Persuasion) check.',
        'castle_location_pred':'Look to the father\'s tomb.',
        'castle_location_dm':'Strahd faces the characters in the tomb of King Barov and Queen Ravenovia (area K88).'},
    9:{
        'name':'Ghost (B)',
        'represents':'The looming past—the return of an old enemy or the discovery of a secret buried long ago',
        'enemy_pred':'Stir the spirit of the clumsy knight whose crypt lies deep within the castle.',
        'enemy_dm':'This card refers to Sir Klutz the phantom warrior (see chapter 4, area K84, crypt 33). If Sir Klutz is Strahd\'s enemy, then the phantom warrior disappears not after seven days, but only after he or Strahd is reduced to 0 hit points.',
        'castle_location_pred':'Look to the father\'s tomb.',
        'castle_location_dm':'Strahd faces the characters in the tomb of King Barov and Queen Ravenovia (area K88).'},
    10:{
        'name':'Executioner',
        'represents':'The imminent death of one rightly or wrongly convicted of a crime—false accusations and unjust prosecution',
        'enemy_pred':'Seek out the brother of the devil\'s bride. They call him "the lesser," but he has a powerful soul.',
        'enemy_dm':'This card refers to Ismark Kolyanovich (see chapter 3, area E2). Ismark won\'t accompany the characters to Castle Ravenloft until he knows that his sister, Ireena Kolyana, is safe.',
        'castle_location_pred':'I see a dark figure on a balcony, looking down upon this tortured land with a twisted smile.',
        'castle_location_dm':'Strahd faces the characters at the overlook (area K6).'
        },
    11:{
        'name':'Horseman (A)',
        'represents':'	Death—disaster in the form of the loss of wealth or property, a horrible defeat, or the end of a bloodline',
        'enemy_pred':'I see a dead man of noble birth, guarded by his widow. Return life to the dead man\'s corpse, and he will be your staunch ally.',
        'enemy_dm':'This card refers to Nikolai Wachter the elder, who is dead (see chapter 5, area N4o). If the characters cast a raise dead spell or a resurrection spell on his preserved corpse, Nikolai (LN male human noble) agrees to help the characters once he feels well enough, despite his wife\'s protests. Although his family has long supported Strahd, Nikolai came to realize toward the end of his life that Strahd must be destroyed to save Barovia. If the characters don\'t have the means to raise Nikolai from the dead, Rictavio gives them a spell scroll of raise dead if he learns of their need. If they\'re staying at the Blue Water Inn, he leaves the scroll in one of their rooms.',
        'castle_location_pred':'He lurks in the one place to which he must return—a place of death.',
        'castle_location_dm':'Strahd faces the characters in his tomb (area K86).'
        },
    12:{
        'name':'Horseman (B)',
        'represents':'	Death—disaster in the form of the loss of wealth or property, a horrible defeat, or the end of a bloodline',
        'enemy_pred':'A man of death named Arrigal will forsake his dark lord to serve your cause. Beware! He has a rotten soul.',
        'enemy_dm':'This card refers to the Vistani assassin Arrigal (see chapter 5, area N9c). If the characters mention this card reading to him, he accepts his fate and accompanies them. If the characters succeed in defeating Strahd, Arrigal betrays and attacks them, believing that he is destined to become Barovia\'s new lord.',
        'castle_location_pred':'He lurks in the one place to which he must return—a place of death.',
        'castle_location_dm':'Strahd faces the characters in his tomb (area K86).'
        },
    13:{
        'name':'Innocent (A)',
        'represents':'A being of great importance whose life is in danger (who might be helpless or simply unaware of the peril',
        'enemy_pred':'I see a young man with a kind heart. A mother\'s boy! He is strong in body but weak of mind. Seek him out in the village of Barovia.',
        'enemy_dm':'This card refers to Parriwimple (see chapter 3, area E1). Although he\'s a simpleton, he won\'t travel to Castle Ravenloft without good cause. Characters can manipulate him into going by preying on his good heart. For instance, he might go there to help rescue missing Barovians, or to save the life of Ireena Kolyana, who is very beautiful. The characters must somehow deal with Bildrath, Parriwimple\'s employer, who won\'t let the foolish boy go to the castle for any reason.',
        'castle_location_pred':'He dwells with the one whose blood sealed his doom, a brother of light snuffed out too soon.',
        'castle_location_dm':'Strahd faces the characters in Sergei\'s tomb (area K85).'
        },
    14:{
        'name':'Innocent (B)',
        'represents':'A being of great importance whose life is in danger (who might be helpless or simply unaware of the peril',
        'enemy_pred':'Evil\'s bride is the one you seek!',
        'enemy_dm':'This card refers to Ireena Kolyana (see chapter 3, area E4). Her brother, Ismark, opposes the idea of Ireena\'s being taken to Castle Ravenloft, but she insists on going there once the characters tell her about the card reading. Ireena won\'t accompany the characters, however, until Kolyan Indirovich\'s body is laid to rest in the cemetery.',
        'castle_location_pred':'He dwells with the one whose blood sealed his doom, a brother of light snuffed out too soon.',
        'castle_location_dm':'Strahd faces the characters in Sergei\'s tomb (area K85).'
        },
    15:{
        'name':'Marionette (B)',
        'represents':'The presence of a spy or a minion of some greater power—an encounter with a puppet or an underling',
        'enemy_pred':'Look for a man of music, a man with two heads. He lives in a place of great hunger and sorrow.',
        'enemy_dm':'This card refers to Clovin Belview (see chapter 8, area S17), the two-headed mongrelfolk. Clovin serves the Abbot out of fear and a perverse sense of loyalty. His job is to deliver food to the other mongrelfolk, whom he abhors. If the Abbot still lives, Clovin doesn\'t want to earn his master\'s ire by attempting to leave, and he refuses to accompany the characters. But if the Abbot dies, Clovin doesn\'t have any reason to remain in the abbey, so he\'s willing to come along if he is bribed with wine. Clovin provides no benefit to the party without his viol.',
        'castle_location_pred':'Look to great heights. Find the beating heart of the castle. He waits nearby.',
        'castle_location_dm':'Strahd faces the characters in the north tower peak (area K60).'
        },
    16:{
        'name':'Marionette (A)',
        'represents':'The presence of a spy or a minion of some greater power—an encounter with a puppet or an underling',
        'enemy_pred':'What horror is this? I see a man made by a man. Ageless and alone, it haunts the towers of the castle.',
        'enemy_dm':'This card refers to Pidlwick II (see chapter 4, area K59, as well as appendix D).',
        'castle_location_pred':'Look to great heights. Find the beating heart of the castle. He waits nearby.',
        'castle_location_dm':'Strahd faces the characters in the north tower peak (area K60).'
        },
    17:{
        'name':'Mists',
        'represents':'Something unexpected or mysterious that can\'t be avoided—a great quest or journey that will try one\'s spirit',
        'enemy_pred':'A Vistana wanders this land alone, searching for her mentor. She does not stay in one place for long. Seek her out at Saint Markovia\'s abbey, near the mists.',
        'enemy_dm':'This card refers to Ezmerelda d\'Avenir. She can be found in the Abbey of Saint Markovia (see chapter 8, area S19), as well as several other locations throughout Barovia.',
        'castle_location_pred':'The cards can\'t see where the evil lurks. The mists obscure all!',
        'castle_location_dm':'The card offers no clue about where the final showdown with Strahd will occur. It can happen anywhere you like in Castle Ravenloft. Alternatively, Madam Eva tells the characters to return to her after at least three days, and she will consult the cards again for them, but only to discern the location of their enemy.'
        },
    18:{
        'name':'Raven',
        'represents':'A hidden source of information—a fortunate turn of events—a secret potential for good',
        'enemy_pred':'Find the leader of the feathered ones who live among the vines. Though old, he has one more fight left in him.',
        'enemy_dm':'This card refers to Davian Martikov (see chapter 12, "The Wizard of Wines"). The old wereraven, realizing that he has a chance to end Strahd\'s tyranny, leaves his vineyard and winery in the capable hands of his sons, Adrian and Elvir. But before he travels to Castle Ravenloft to face Strahd, Davian insists on reconciling with his third son, Urwin Martikov (see chapter 5, area N2).',
        'castle_location_pred':'Look to the mother\'s tomb.',
        'castle_location_dm':'Strahd faces the characters in the tomb of King Barov and Queen Ravenovia (area K88).'
        },
    19:{
        'name':'Seer',
        'represents':'Inspiration and keen intellect—a future event, the outcome of which will hinge on a clever mind',
        'enemy_pred':'Look for a dusk elf living among the Vistani. He has suffered a great loss and is haunted by dark dreams. Help him, and he will help you in return.',
        'enemy_dm':'This card refers to Kasimir Velikov (see chapter 5, area N9a). The dusk elf accompanies the characters to Castle Ravenloft only after they lead him to the Amber Temple and help him find the means to resurrect his dead sister, Patrina Velikovna.',
        'castle_location_pred':'He waits for you in a place of wisdom, warmth, and despair. Great secrets are there.',
        'castle_location_dm':'Strahd faces the characters in the study (area K37).'
        },
    20:{
        'name':'Tempter (A)',
        'represents':'One who has been compromised or led astray by temptation or foolishness—one who tempts others for evil ends',
        'enemy_pred':'I see a child—a Vistana. You must hurry, for her fate hangs in the balance. Find her at the lake!',
        'enemy_dm':'This card refers to Arabelle (see chapter 2, area L). She gladly joins the party. But if she returns to her camp (chapter 5, area N9), her father, Luvash, refuses to let her leave.',
        'castle_location_pred':'I see a secret place—a vault of temptation hidden behind a woman of great beauty. The evil waits atop his tower of treasure.',
        'castle_location_dm':'Strahd confronts the characters in the treasury (area K41). "A woman of great beauty" refers to the portrait of Tatyana hanging in the castle\'s study (area K37), which contains a secret door that leads to the treasury.'
        },
    21:{
        'name':'Tempter (B)',
        'represents':'One who has been compromised or led astray by temptation or foolishness—one who tempts others for evil ends',
        'enemy_pred':'I hear a wedding bell, or perhaps a death knell. It calls thee to a mountainside abbey, wherein you will find a woman who is more than the sum of her parts.',
        'enemy_dm':'This card refers to Vasilka the flesh golem (see chapter 8, area S13).',
        'castle_location_pred':'I see a secret place—a vault of temptation hidden behind a woman of great beauty. The evil waits atop his tower of treasure.',
        'castle_location_dm':'Strahd confronts the characters in the treasury (area K41). "A woman of great beauty" refers to the portrait of Tatyana hanging in the castle\'s study (area K37), which contains a secret door that leads to the treasury.'
        }
}
