# This is some backstory.
print('You are a Mandolorian on a mission for a bounty.\nYou are looking for a predecessor to Jabba the Hutt.\nYou have been offered a lot of credits, so failure is not an option.\nYou have landed on Tatooine and you are sneaking around a criminal base, looking for clues on where to go next.\nYou have a tracking device that usually works; however, in a recent kerfuffle it got damaged and is faulty.')

# Scenario 1
left_right = input('\nYou are approaching a fork in the tunnels of the base. It is dark and you think there is someone approaching from the left side of the tunnel.\nYour tracker begins to beep louder when you point it to the left.\nDo you trust the tracker and go LEFT? Or do you go to the RIGHT? (Keep in mind, you also have a GUN to use at any moment.) ')
if left_right.upper() == 'LEFT':
    print('\nYou feel that the left is the right way to go. Upon following the tracker, you run into the person approaching. They begin to ask what your business is. Your adrenaline begins to pump.')
    # Scenario 2
    truth_lie = input('Do you tell them the TRUTH? Or do you LIE? (GUN?) ')
    if truth_lie.upper() == 'TRUTH':
        print('\nYou explain how you are looking for the predecessor to Jabba the Hutt. He appreciates your honesty and leads you to him. After following for a bit, you walk into the room with the predecessor! You explain to him that you have been sent to kill him. He wants to reason with you.')
        # Scenario 3
        reason_shoot = input('Do you REASON? Or do you SHOOT? (GUN?) ')
        if reason_shoot.upper() == 'REASON':
            print('\nYou hear him out, he offers you a sum of credits more than the bounty you accepted. You follow your Mandolorian creed and kill him anyways. You take his head and escape. You got your credits.\nYou win!')
        elif reason_shoot.upper() == 'SHOOT':
            print('\nYou look up to see a chandelier above the predecessor, you take your gun and shoot the chain. An instant death. You take his head and escape. You get your full amount of credits.\nYou win!')
        elif reason_shoot.upper() == 'GUN':
            print('\nYour gun gets jammed as you try to shoot. The predecessor pulls a chain and you fall into a rancor pit. You get eaten like a piece of steak, rare and filthy.\nYou lose.')
        else:
            print('\nYou are looking like a clown with a red nose and all. The predecessor gets bored and pulls the chain. You become rancor scrap.\nYou lose.')
    # Scenario 2
    elif truth_lie.upper() == 'LIE':
        print('\nYou explain how you got lost and need to use the restroom. He told you the wrong directions. You found this out because you walked into the rancor pit.')
        # Scenario 3
        blast_jetpack = input('Do you BLAST the door to leave? Or do you JETPACK? (GUN?) ')
        if blast_jetpack.upper() == 'BLAST':
            print('\nYou blast the door to leave. It will not move. The rancor eats you like the prime rib you are.\nYou lose.')
        elif blast_jetpack.upper() == 'JETPACK':
            print('\nYou start revving up your trusty old jetpack! You fly out of the rancor pit and meet the predecessor to Jabba the Hutt. You shoot him dead. You take his head back, get the bounty, and buy a new Razorcrest.\nYou win!')
        elif blast_jetpack.upper() == 'GUN':
            print('\nYou shoot that dumb rancor dead! You feel so bad doing it that you have a meltdown and live the rest of your days in the rancor pit.\nYou lose.')
        else:
            print('\nAs a little bit of urine trickles down your sweetly toned thighs, the rancor smells you and exterminates you from existence. Not even your toned muscles could have saved you.\nYou lose.')
    # Scenario 2
    elif truth_lie.upper() == 'GUN':
        print('\nYou pull out your gun and you shoot him dead. In a panic, you decide to start running where they came from giving up on the stealth part. You run and find the predecessor to Jabba the Hutt! He looks at you with surpise.')
        # Scenario 3
        dance_massacre = input('Do you keep the surpise going and breakout into a spontaneous DANCE? Or do you barbarically MASSACRE everyone in the room? (GUN?) ')
        if dance_massacre.upper() == 'DANCE':
            print('\nTo you, dancing seemed like a really good idea at the time. In a slightly pathetic manner, you were gunned down. At least you went out doing what you loved.\nYou lose.')
        elif dance_massacre.upper() == 'MASSACRE':
            print('\nThe idea of dance really stuck with you for some reason. Instead of slaughtering everyone in the room with your darksaber, you dropped it like it was hot and everyone began to dance until they literally dropped. Congrats, you got the head of the predecessor and returned for your bounty.\nYou win!')
        elif dance_massacre.upper() == 'GUN':
            print('\nYou have a high noon quick-draw with the predecessor to Jabba the Hutt. You definitely shot first. The duel was won! You take his head clean off and return for your bounty.\nYou win!')
        else:
            print('\nThe predecessor to Jabba the Hutt gets bored of you and decides to make you one of his scandalously dressed servants. Good luck.\nYou lose.')
    else:
        print('\nYou sit there and look like an idiot. He pulls out a blaster and shoots you dead. Congrats, you choked.\nYou lose.')
elif left_right.upper() == 'RIGHT':
    print('\nAs you begin to go towards the right tunnel, the beeping of your tracker fades. Was this the right way to go? You start questioning yourself.')
    # Scenario 2
    back_continue = input('Do you turn BACK? Or do you CONTINUE? (GUN?) ')
    if back_continue.upper() == 'BACK':
        print('\nYou decide to turn back! You are once again staring at the same fork in the road.')
        # Scenario 3
        again_right_left= input('Do you, once again, want to go to your RIGHT or LEFT? (GUN?) ')
        if again_right_left.upper() == 'RIGHT':
            print('\nSeriously? You just came from here. Well, you walk down the hallway again and trip. You break your neck and die. How tragic.\nYou lose.')
        elif again_right_left.upper() == 'LEFT':
            print('\nYou run into the predecessor to Jabba the Hutt! You should have trusted your tracker. Now that you are here, you absolutely body that slug. You take your proof, get the bounty reward, and got your adventure.\nYou win!')
        elif again_right_left.upper() == 'GUN':
            print('\nAfter flipping a coin, you start firing your blaster down the left hallway. You end up shooting the predecessor to Jabba the Hutt. You get to his body, take his head, and leave.\nYou win!')
        else:
            print('\nYou are in a massive pile of confusion. Because of this, you grow ill and forgot why you are here.\nYou lose.')
    # Scenario 2
    elif back_continue.upper() == 'CONTINUE':
        print('\nYou press on! You do not seem to find anything exciting at all. Unfortunate! That is part of adventuring. When all of a sudden, a man in a trench coat swiftly swoops behind you. It looks like he is wearing a trench coat.')
        # Scenario 3
        business_cower= input('Do you ask what his BUSINESS is? Or do you CURL into a ball and cower? (GUN?) ')
        if business_cower.upper() == 'BUSINESS':
            print('\nHe tells you that he sells watches and pulls one out from his trench coat. You do end up buying one but did not find the predecessor to Jabba the Hutt.\nYou lose.')
        elif business_cower.upper() == 'CURL':
            print('\nYou begin to grovel, cower, and beg for your life. He decides to spare you but on one condition: If you buy one of the watches he is selling.\nYou do so and live but never found what you came for.\nYou win and lose.')
        elif business_cower.upper() == 'GUN':
            print('\nYou blast the poor fella. He never saw it coming. As his body falls, you notice the 100s of watches falling from his corpse.\nYou take all the watches and leave. You sell them all which is more profitable than the bounty. You retired.\nYou win!')
        else:
            print('\nYou awkwardly sit there and rethink your life. You join this trench coat man on his watch selling adventure. You did not get your bounty but your new business is profitable.\nYou win!')
    # Scenario 2
    elif back_continue.upper() == 'GUN':
        print('\nYou are not quite sure how your gun could be useful in this moment; however, you still get creative. You have a sudden thought that you need to shoot your toe.')
        # Scenario 3
        toe_not= input('So, do you shoot your TOE? Or do you NOT shoot your toe? (GUN?) ')
        if toe_not.upper() == 'TOE':
            print('\nYou shoot your toe and pass out in pain. Little did you know there was a giant carbon monoxide leak and because you passed out, you died.\nYou lose.')
        elif toe_not.upper() == 'NOT':
            print('\nYou do not really want to shoot your toe. Upon pondering why that thought existed, a carbon monoxide alarm goes off in the base.\nYou escape with your life. Upon evacuating, you run into the predecessor to Jabba the Hutt. You kill him and get the bounty.\nYou win!')
        elif toe_not.upper() == 'GUN':
            print('\nYou shoot in a random direction. The laser begins to bounce dramatically until it reaches your neck. You bleed out and die. How sad.\nYou lose.')
        else:
            print('\nA carbon monoxide alarm goes off in the building. Due to your poor decision making skills, you begin laughing hysterically until you pass out and die.\nYou lose. ')
    else:
        print('\nYou sit there pondering for a little too long. You grow old and fade away out of existence.\nYou lose.')
elif left_right.upper() == 'GUN':
    print('\nWith a quick draw and not a question in mind you blast that person to the left approaching you. Your gun is not a silent one and as the blaster smokes, an alarm begins to ring.\nYou can run through guns-a-blazing or try sneaking your way through the facility as the criminals scramble to find you.')
    # Scenario 2
    loud_sneak = input('Do you go LOUD and proud? Or do you SNEAK with the distraction? (GUN?) ')
    if loud_sneak.upper() == 'LOUD':
        print('\nWith your gun smoking, hot, and ready to go. You get moving down the hallway with the body you just dropped to the floor.\nYou bust open a door and meet the predecessor; however, it is an awkward circumstance. He is in the restroom.')
        # Scenario 3
        privacy_dignity= input('Do you give him PRIVACY? Or do you kill him with no DIGNITY? (GUN?) ')
        if privacy_dignity.upper() == 'PRIVACY':
            print('\nYou have some serious class. As a gentleman, you have succeeded. The predecessor really appreciates you waiting before killing him.\nHe lets you do so kindly. You get the bounty and walk out.\nYou win.')
        elif privacy_dignity.upper() == 'DIGNITY':
            print('\nYou were raised better than that; however, in your excitment, you slaughtered him. You take his head and obtain your bounty!\nYou got lots of credits and decide to spend them all on a dress for the pretty lady down the street.\nYou win!')
        elif privacy_dignity.upper() == 'GUN':
            print('\nIn the spirit of ultimate disrespect, you shoot with your eyes closed and even spin 360 degrees before shooting. You miss everytime.\nIn doing so, the predecessor pulls out his personal blaster and kills you.Extra points for style though. Was it worth the trickshot?\nYou lose.')
        else:
            print('\nIn the spirit of awkward, you stand there in the doorway not sure what you are witnessing. Something you wish you had never seen. You shoot your eyes out and never see again.\nYou lose.')
    # Scenario 2
    elif loud_sneak.upper() == 'SNEAK':
        print('\nYou are going in sneaky-beaky like. You were trained to be quick and quiet. Amongst the commotion, you sneak by gaurds easily.\nYou open the door to your left and find security cameras with turrets. One of which is on your target: The predecessor to Jabba the Hutt.')
        # Scenario 3
        turret_closer= input('Do you use the TURRET to kill? Or do you keep stealthing CLOSER? (GUN?) ')
        if turret_closer.upper() == 'TURRET':
            print('\nYou are a little tech-wizard. By Dungeons and Dragons standards, you casted fireball on your target. You rolled a 20 on the 20-sided dice (which is a critical success).\nYou doubled your damage for a perfect kill. You incenerated him a little too good. You have no proof but your employer takes your word for it.\nYou win!')
        elif turret_closer.upper() == 'CLOSER':
            print('\nYou are going very rogue. By not taking a kill that was too easy, you are risking yourself; however, you manage to sneak all the way to your bounty.\nYou take your darksaber and slice his head clean off. You return for your bounty.\nYou win!')
        elif turret_closer.upper() == 'GUN':
            print('\nYou shoot all the security cameras and the gaurds in there look at you very confused. You are also confused as to why you did that. You are taken into custody for the following: breaking and entering, murder, and vandalism.\nYou lose.')
        else:
            print('\nYou are sitting in the security room, believe it or not, there are security officers here. You are taken into bondage and sold as a servant.\nYou lose.')
    # Scenario 2
    elif loud_sneak.upper() == 'GUN':
        print('\nThe gun is hot, why not make it hotter? Your eyes begin to swell red with rage. You are not you, at this moment.\nThe heat of the moment has got you excited. You kill everything in sight, except one creature. You find a cute little Grogu!')
        # Scenario 3
        grogu_ignore= input('With rage fuming in your countenance, do you let GROGU calm you down? Or do you IGNORE him and continue your killing spree? (GUN?) ')
        if grogu_ignore.upper() == 'GROGU':
            print('\nGrogu appreciates your willingness to let him change you. He sticks his hands forward and calms you down. You feel the force and it is with you. You are led to your goal and obtain the bounty.\nYou win!')
        elif grogu_ignore.upper() == 'IGNORE':
            print('\nTalk about having no heart. Grogu waddles away and cries. You are the cause of a little heart breaking. You do not care, you are a barbarian.\nYou find the predecessor to Jabba the Hutt and end his life and obtain the bounty you came for; but, at what cost?\nYou win!')
        elif grogu_ignore.upper() == 'GUN':
            print('\nYou did not seriously just choose to shoot Grogu. You are a monster.\nYou lose x1000.')
        else:
            print('\nYou just sit there, menacingly. Grogu then puts googly eyes on you. You are then put on a shelf in a knick-knacks shop.\nTo make matters worse, you are not expensive knick-knack either, Oof.\nYou lose.')
    else:
        print('\nWith alarms going off around you, and everyone freaking out, you bend on your knees and stare at the person you killed. It gets quiet for this is all you can think about.\nThis person probably had a wife and kids. They will never see him again. Way to go.\nYou lose.')
else:
    print('\nYou have been hit with analysis paralysis and took too long. The person sees you and captures you. You will now be fed to the rancor and ultimately die.\nYou lose.')