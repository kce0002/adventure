class Character:
    hitpoints = 0
    skillpoints = 0
    name = ""
    description = ""
    characterId = -1

    def __init__(self, characterId):
        self.characterId = characterId
        self.skillpoints = 25

        # Ron Swanson
        if characterId == 1:
            self.name = 'Ron Swanson'
            self.hitpoints = 100
            self.description = 'Ron Swanson is a thick and impressive being. '
            self.description += 'He is an excellent woodworker, he has '
            self.description += 'incredible alcohol tolerance, and he can grow '
            self.description += 'facial hair faster than weeds grow. However '
            self.description += 'he has a few glaring weaknesses. He is deathly '
            self.description += 'afraid of taxes, women named Tammy can easily '
            self.description += 'manipulate him, and he is extremely scared of '
            self.description += 'people knowing his personal information. He has '
            self.description += '100 hitpoints thanks to his thick stature, which '
            self.description += 'makes him a valuable asset to any team.'
        # Michael Scott
        elif characterId == 2:
            self.name = 'Michael Scott'
            self.hitpoints = 50
            self.description = 'Michael Scott is a lovable, goofy manager. '
            self.description += 'He has many disguises for dire situations, '
            self.description += 'he is extremely funny (even in bad situations), '
            self.description += 'and he is known as the world\'s best boss. '
            self.description += 'He does have some pretty serious weaknesses, '
            self.description += 'though. He has a hard time making difficult '
            self.description += 'decisions, he has had three vasectomies (ouch!), '
            self.descritpion += 'and being around Toby makes him angry and causes '
            self.description += 'him to make bad decisions. As an average man in '
            self.description += 'stature, he has 50 hitpoints. He is extremely '
            self.description += 'lovable and having him on your team will certainly '
            self.description += 'boost morale.'
        # Joey Tribbiani
        elif characterId == 3:
            self.name = 'Joey Tribbiani'
            self.hitpoints = 70
            self.description = 'Joey Tribbiani is a food-loving goober. He has many '
            self.description += 'skills. These skills include eating amazing amounts '
            self.description += 'of food, acting (primarily as a doctor), and attracting '
            self.description += 'ladies. He unfortunately has quite a few weaknesses too. '
            self.description += 'He is awful at sharing food, he is actually pretty dumb, '
            self.description += 'and he has a bad track record with personal finances. He '
            self.description += 'is somewhat thick, which gives him a hitpoint value of 70. '
            self.description += 'His loving and hungry nature will make him a joy to have on '
            self.description += 'any team.'
        # Sheldon Cooper
        elif characterId == 4:
            self.name = 'Sheldon Cooper'
            self.hitpoints = 35
            self.description = 'Sheldon Cooper is an arrogant genius. He has a vast number '
            self.description += 'of strengths. He knows a lot of random facts, he is a genius, '
            self.description += 'and he is an intense, but excellent video gamer. Although his '
            self.description += 'strengths are quite valuable, his weaknesses are very '
            self.description += 'apparent. He lacks basic social skills, he has zero '
            self.description += 'athleticism, and he is extremely arrogant, which makes him a '
            self.description += 'pain to argue with. Being a stereotypical nerd, he is paper-thin '
            self.description += 'in stature, giving him a mere 35 hitpoints. Although his '
            self.description += 'weaknesses are worrisome, he can easily take his team to victory '
            self.description += 'because he is unbelievably smart.'
        # El
        elif characterId == 5:
            self.name = 'El'
            self.hitpoints = 30
            self.description = 'El is an incredible specimen. She is extremely protective, she '
            self.description += 'can see things in other dimensions and locate people who '
            self.description += 'seemingly cannot be found, and she has telekinetic ability. '
            self.description += 'She spent the majority of her young life in a lab being '
            self.description += 'experimented on by evil scientists, so she lacks a lot of '
            self.description += 'common sense. She is obsessed with eggo waffles, so she can be '
            self.description += 'lured into traps easily. She also has tunnel vision, which '
            self.description += 'limits her ability to see the bigger picture when making decisions. '
            self.description += 'being a young female, she only has 30 hitpoints. Don\'t let her low '
            self.description += 'low hitpoints or weaknesses scare you. She has supernatural powers, '
            self.description += 'making her a strong member of any team.'
        # Hermione Granger
        elif characterId == 6:
            self.name = 'Hermione Granger'
            self.hitpoints = 40
            self.description = 'Hermione Granger is a wizard. She is extremely hard-working, '
            self.description += 'she has magic (wizard, duh), she has an absurd amount of '
            self.description += 'common sense, and she is the most responsible character in '
            self.description += 'the game. However, she has a grave fear of failure, she '
            self.description += 'has a habit of following rules instead of instinct, and '
            self.description += 'she tends to let her pride get in the way. Being an average-'
            self.description += 'sized woman, she has 40 hitpoints. She is a major asset to any '
            self.description += 'team.'            
        # Robin Scherbatsky
        elif characterId == 7:
            self.name = 'Robin Scherbatsky'
            self.hitpoints = 50
            self.description = 'Robin Scherbatsky is an average woman. She possesses excellent '
            self.description += 'gun skills, she has a talent for singing pop songs, and she is '
            self.description += 'outstanding at telling the news. Unfortunately, she has some '
            self.description += 'weaknesses. She can\'t seem to get anyone to watch her news '
            self.description += 'on TV, she is horrible with children, and she is Canadian. '
            self.description += 'She holds an average number of hitpoints (50). Since she is '
            self.description += 'an outstanding markswoman, she will make a great addition to '
            self.description += 'any team.'
        # Homer Simpson
        elif characterId == 8:
            self.name = 'Homer Simpson'
            self.hitpoints = 65
            self.description = 'Homer Simpson is a laughable character. He is an expert beer '
            self.description += 'drinker, he is constantly kissing the butts of his bosses, and '
            self.description += 'no one can watch TV like him. He can sit at the TV for hours, '
            self.description += 'pounding beers left and right. He is extremely stupid, '
            self.description += 'amazingly lazy, and he has a horrible habit of not paying '
            self.description += 'attention when people are speaking to him. He does have '
            self.description += 'an absurdly large beer gut, which gives him 65 total hitpoints. '
            self.description += 'He would make a hilarious team member.'
        # Spongebob Squarepants
        elif characterId == 9:
            self.name = 'Spongebob Squarepants'
            self.hitpoints = 30
            self.description = 'Spongebob Squarepants is an adorable sponge, who lives in a '
            self.description += 'pineapple under the sea. He works as a cook at the Krusty '
            self.description += 'Krab. His skills are jellyfishing, cooking (specifically '
            self.description += 'making krabby patties), and he is always ready. His weaknesses '
            self.description += 'are his habit of ripping his pants, he is a horrible driver, and '
            self.description += 'and he always seems to lose his name tag. Being a small sponge, '
            self.description += 'he only has 30 hitpoints, but his energy and excitement make '
            self.description += 'him a joy to have on any team.'            
        # Jackie Burkhart
        elif characterId == 10:
            self.name = 'Jackie Burkhart'
            self.hitpoints = 25
            self.description = 'Jackie Burkhart is a beautiful young woman. She is extremely '
            self.description += 'fashionable, she has very wealthy parents, and as previously '
            self.description += 'stated, she is very attractive. Unfortunately, she is also '
            self.description += 'as dumb as a brick, she is blinded by her love of Michael Kelso, '
            self.description += 'and she is very self-centered. She is a scrawny female, so she only '
            self.description += 'has 25 hitpoints. Although she has such glaring weaknesses, she '
            self.description += 'can still be a strong asset to any team because of her skills.'
        # Shrek
        elif characterId == 11:
            self.name = 'Shrek'
            self.hitpoints = 120
            self.description = 'Shrek is a beast of an ogre. He has a huge stature, he is '
            self.description += 'unbelievably strong, he can speak to animals (primarily a donkey), '
            self.description += 'and nothing can upset his stomach. However, he gets angry very '
            self.description += 'very easily, he prefers to be alone, and fairytale creatures cause '
            self.description += 'him to lose his mind. He has a remarkable 120 hitpoints thanks to '
            self.description += 'his large size and leather-like skin. He would make a powerful asset '
            self.description += 'to any team.'