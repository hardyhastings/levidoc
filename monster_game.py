import random 
import time 
#For this Project i will import the time data module and time data module 

class Hero:
    def __init__(self,name,health_status): 
        self.name = name 
        self.health = health_status
  
#Define Class For The Hero 

print('\n       Welcome to the Monster And Hero Game\n')
print('______________________________________________________________')
#Welcome The User To The Plattform 

class Monster: 
    def __init__(self,type,health_status): 
        self.type = type
        self.health = health_status 
#Define Class For The Monster 

monster_list = ['Bogeyman 🤡','Vampire 🧛','Dybbuk 👻📦',
                'Banshee 👻🚨','Pontianak 👻','Zombie 🧟',
                'Hydra 🐍🐍🐍','Chimera 🦁🐐🐍','Yeti, Sasquatch, and Bigfoot 🦍👣',
                'Dragon 🐉','Unicorn 🦄','Basilisk 🐔🐍',
                'Phoenix 🔥🦅🔥','Griffin 🦅🦁','Loch Ness Monster 🏴󠁧󠁢󠁳󠁣󠁴󠁿🌊 🦕',
                'Werewolf 👨🌕🐺','Satyrs and Fauns 👨🐐','Centaurs 👨🐎',
                'Minotaur 🐮👨','Aqrabuamelu 👨🦂','Mermaid 🧜‍♀',
                'Gorgon 😵🐍🐍🐍','Goblin 👺','Gnomes 👿🛠️🏠',
                'Ogre 🤢','Cyclops 👁️','Oni 👹']

monster_description = ['The bogeyman can take many forms, but their purpose remains constant: to scare the living daylights out of children and coerce them into good behavior. A bogeyman might be an actual human (in one of the tales of Struwwelpeter, a tailor cuts off a boy\'s thumbs because he sucks them too much), but in most cases, it’s a supernatural force of some type.',
                       'Though their portrayals will vary across culture — from brooding sexy ones in Twilight and Anne Rice novels to terrifying monstrous Count Orlok in Nosferatu — there are a few things that remain the same: vampires feed on the living to remain immortal, they avoid sunlight, and their hearts are vulnerable to sharp objects — you know, just like you and me. Often a metaphor for the dangers of sexual desire, vampires have remained firmly in the cultural consciousness for over a hundred and fifty years.',
                       'Jewish folklore has more than its fair share of creatures that will send chills down your spine. Perhaps none more than the dybbuk, the dislocated soul of someone deceased who has taken over a host body to complete unfinished business. Though one was featured in the opening scene of The Coen Brothers\' A Serious Man, Dybbuks have recently re-entered popular imagination as the unlikely antagonist of rapper Post Malone.',
                       'A female spirit whose haunting howls herald a coming death. Banshees are a part of Irish mythology best known for their ubiquity in modern metaphor (“screams like a banshee”) and their tendency to support Siouxsie Sioux in concert.',
                       'Perhaps the best known of the evil spirits in Indonesia and Malaysia, Pontianak is said to be the souls of women who died whilst pregnant. Noted for their pale skin, long, lank hair and white dress (think the girl from The Ring), they’ve been known to lure and kill unsuspecting men. Be warned, if you smell their signature scent of frangipani, run away!',
                       'While its name derives from Haitian folklore, the zombies we’re most accustomed to originate from the mid-20th century. In particular, we’re talking about the creatures in I am Legend by Richard Matheson and the classic films of George Romero (Night of the Living Dead, Dawn of the Dead). Divorced from all semblance of their former selves and highly infectious, these shambling corpses have only one desire: to consume human flesh.',
                       'Cut off one head, and two more will take its place. This was the challenge that faced Heracles when he was commanded to slay the Hydra of Lerna, a many-headed beast, during the second of his labors.',
                       'Part lion, part goat, part snake. It seems entirely plausible that the chimera owes its existence to someone viewing three adjacent animals from far away — but who knows? The term chimera is now used to describe anything puzzlingly composed of more than one pre-existing thing.',
                       'Apologies to Bigfeet aficionados, but we’re grouping these giant ape-men together. Known for their ability to remain out of focus in photographs, they remain a point of fascination for real-world true believers. As recently as February 2019, retired baseball player Jose Canseco was selling tour packages to join him on Bigfoot hunts.',
                       'Despite (to our knowledge) having never existed, the dragon features in the mythology of numerous civilisations around the world — and is often used as a symbol of royal power. Perhaps the single most common mythological creature found in fantasy fiction, they continue to capture readers’ imaginations with their various depictions on page and screen.',
                       '“Hi, I’m a unicorn. You may recognize me from such places as Every Child’s Birthday Party and 90% of All Items in a Gift Store.” At some point in the past, unicorns were retconned to fart rainbows, which perfectly encapsulates their anything-goes mythology. In picture books for under-fives, the unicorn remains a popular central figure.',
                       'What’s scarier than a serpent? One that’s been cross-bred with a rooster and can kill with a single stare! Not content with just one power, certain myths also suggest basilisks have the ability to turn silver into gold. The return on investment isn’t as good as what Rumplestiltskin offered, but it’s still not bad. The legend of the Warsaw Basilisk saw the creature defeated by a cunning local doctor who created a suit made of feathers and mirrors. Fun!',
                       'A universal symbol of resurrection, whether representing a character’s spiritual resurgence or their literal return from the grave. Also featured heavily in royal heraldry, the mythological creature is said to stem from Greek and Roman mythology.',
                       'With the body of a lion and the head, wings, and front feet of an eagle, the Griffin seems almost tailor-made for riding — were they not such temperamental creatures. Some versions of the griffin are known for jealously guarding gold (much like their dragon cousins). As a symbol, this majestic being can be seen in heraldry as well as in logos like that of Vauxhall Motors.',
                       'The creature known to locals as ‘Nessie’ is another creation of the 20th century and a common subject of spurious photography. Despite, you know, logic, various professional expeditions have taken place using expensive equipment to seek out this urban myth. If you grew up in Scotland, you’ll be more than familiar with the Nessie merchandise that populates every gift shop in the land. That and you probably remember this cartoon.',
                       'An enduring motif in mythology across Europe, werewolves (or lycanthropes, to give them their SAT name) served a similar function to witches, as men were commonly hunted and executed in the belief that they transformed into ravenous creatures called werewolves. In more recent times, they have become the subject of classic horror films, and even the object of affection in certain corners of paranormal romance.',
                       'With the bottom half of a goat and the top half of a human, Satyrs and Fauns are somewhat similar. That is, with the exception that Satyrs are a lot more interested in chasing women, while a faun is much more likely to invite you in for a lovely cup of cocoa.',
                       'With the top half of a human and the full body of a horse, Centaurs have long served as antagonists in Greek mythology, falling victim to classical heroes like Heracles and Theseus. These days, Centaurs can mostly be found filling up the darker corners of the user-contributed fan site, DeviantArt. (Warning: do NOT run that search).',
                       'With the head of a bull and the body of a man, you can’t blame the top-heavy minotaur for being an angry fellow. Trapped at the center of a labyrinth built by cruel King Minos of Crete (who lends his name to the creature), the legendary Minotaur was finally slain by the Athenian Theseus.',
                       'These scorpion-men of ancient Mesopotamia are best known for guarding the gates of the sun god in the Epic of Gilgamesh. They’re sort of like a desert Centaur with the added talent of being able to sting you with their tail.',
                       'Not all Mermaids want to be where the people are, and walk on those — what do you call them? — feet. Presumably invented in the parched, sun-baked minds of ancient sailors, Mermaids are the human/fish hybrids that rule the underwater kingdom. Their mythos has since been informed by Greek sirens, and they are seen as both menaces and potential lovers to those who travel by sea.',
                       'A fantastical creature or a product of ancient misogyny? You be the judge! According to Ovid’s telling in Metamorphoses, Medusa was a beautiful maiden who was transformed by Athena in a jealous rage. Where once she had a lovely mane of hair and a gorgeous face, there were now only snakes for locks and a visage that turned men instantly to stone. Thankfully, the great hero Perseus was on hand to cut off her head and take it as a trophy. She really was too good for this world.',
                       'With powers similar to fairies, Goblins are best characterized by their greed, short temper, and penchant for mischief. They also tend to be a whole lot uglier than their tiny cousins — needless to say, you don’t want to get them mixed up.',
                       'Where fairies tend to be elemental (in that they’re part of nature), gnomes are their domestic cousins, known for living in walls and underground. In Cologne, the legend of the Heinzelmännchen tells of house gnomes who did the town’s work at night, so that the citizens could just laze about all day. But that changed when a tailor’s wife had the bright idea to scatter peas on the ground to make them slip up and leave town.',
                       'Huge, monstrous creatures with an appetite for human flesh — that of children, in particular. Ogres have turned up in a variety of fairy tales and myths including those of The Odyssey, Beowulf, Gilgamesh, and Puss in Boots. The animated film Shrek would have you believe that ogres are secretly gentle beings with layers of emotion, but don’t let your guard down around them!',
                       'They’re giants, but with only one eye — which makes them a bit less formidable than their two-eyed cousins. In The Odyssey, Odysseus is trapped in the cave home of Polyphemus the Cyclops. Odysseus tells the giant that his name is ‘Nobody’ and blinds him with a sharpened spike. When Polyphemus calls for help, he screams that he has been “hurt by Nobody,” which confuses the other cyclopses long enough for Odysseus to escape. Silly cyclops.',
                       'If you ever wondered what that red-faced monster emoji was (see above) then here’s the answer! Giant ogre-like monsters of Japanese mythology, the Oni are man-eaters often depicted carrying heavy iron clubs. During the Japanese spring festival, it’s not unusual to witness a custom in which dried beans are tossed around to ward off Oni.',]


total_monster_count = len(monster_list)
#Get The Total Number Of Monsters in The Lists Provided 
#Instantiate The Hero And Monster Characters 
status = True 

while (status == True): 
    monster_index = random.randrange(1, total_monster_count)
    #Use the Random Module to create a random integer that would be used to select the monsters at random 
     
    selected_random_monster = monster_list[monster_index]
    selected_monster_description = monster_description[monster_index]
    
    username_hero = input('Enter Your Hero\'s Name :  ').strip()

    print("\nMonster Challenger would be :" + selected_random_monster+'\n')
    print('\nMonster BIO:\n'+selected_monster_description+'\n')
    #The Monster Has Been Selected 

    input("Press Enter To Start Fight...")

    random_health = random.randrange(100,500)
    monster_data = Monster(selected_random_monster,random_health) 
    #Create The Monster Character 

    hero_data = Hero(username_hero,random.randrange(100,500))
    #Create The Hero Character 

    print('\nStarting Fighting Session\n')
    print('Hero: ',hero_data.name,'  HP:',hero_data.health,' | Monster: ',monster_data.type,'  HP:',monster_data.health)
    next_play = random.choice([True, False])

    while ((hero_data.health>=0) and (monster_data.health>=0)):

        time.sleep(1)
        hero_attack_damage = random.randrange(20,50)
        monster_attack_damage = random.randrange(20,50)

        if (next_play == True):
            monster_data.health += -monster_attack_damage
            next_play = random.choice([True, False])
            print(hero_data.name,' attacks ',monster_data.type,' for '+str(monster_attack_damage)+' damage\n')
        else: 
            hero_data.health += -hero_attack_damage 
            next_play = random.choice([True, False])
            print(monster_data.type,' attacks ',hero_data.name,' for '+str(hero_attack_damage)+' damage\n')

        print('Hero: ',hero_data.name,'  HP:',hero_data.health,' | Monster: ',monster_data.type,'  HP:',monster_data.health)
    
    if (monster_data.health>hero_data.health):
        print("\n","\nMonster has defeated Hero\n")
    else: 
        print("\n","\nHero has defeated the Monster\n")
        
    continue_session = input("Do you wish to start the game again: Yes/No\n").strip().lower()
    if (continue_session == 'no'):
        status = False 
        print('\nGame ended, Thank you for using this project\n')
    else: 
        status = True 


#I DID IT FOR HARAMBE 