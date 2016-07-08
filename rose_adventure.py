
username = raw_input('What\'s your name? ')
print 'Well %s, would you like to hear about an adventuresome furry shark?' % (username)

follow_adventure = raw_input('Type Y or N ')

if follow_adventure.lower() == 'n':
    print 'Awww well maybe next time! Bye.'

elif follow_adventure.lower() == 'y':
    print '\n'
    print 'Ohhh this is going to be fun!'

    print '\n'
    print '''%s, I would like to introduce you to my furry shark. We most often call him "Queen", though his given name is Tux Cedo. He enjoys sprawling on his belly outside, from rooftops to under the deck.''' % (username)

    roof_adventure = raw_input('Do you want to hear about his flying adventures? Type Y or N ')
    print '\n'

    if roof_adventure.lower() == 'n':
        print 'I could tell you about his porch adventure instead. He summoned the neighbors with his screams. Remind me later, since we are short on time today!'


    elif roof_adventure.lower() == 'y':
        print 'Put on your climbing shoes, they\'ll be needed.'
        print '''We keep our queen indoors for various environmental, health and safety reasons. But that doesn\'t keep him from enjoying the view and breeze. You see, Tux likes to talk to birds. It is his favorite past time. ALL day long he will sit at his various perches and chatter to them.'''
        print '\n'
        print '''One day, we went out to the grocers and got a call that our house alarm was going off. We rushed home to find that Tux had pushed the window open enough to set off the alarm. He had even managed to bust through the screen! If nothing else, he has size and brute force on his side.'''
        print '\n'
        print '''Soon we heard him crying but were unable to find him. Finally I spotted him peering at me over the roof, wide eyed and attempting to climb down to me. There was no way... I pulled out the ladder and went up for him. He ran into my arms and buried his face into my chest. Just at that moment, a bluebird squawked nearby.'''

        bluebird = raw_input('I will let you guess: did he stay in my arms? Type Y or N ')
        print '\n'

        if bluebird.lower() == 'y':
            print 'Of course not!'

        else:
            print 'You are corect  %s, he did not!' % (username)

        print '\n'
        print 'I have the claw scars to prove it. He took off, sure he would be able to fly after that pesky (another story for another time) jay. Have you seen a cat fly? Well, I sure did on that day. I watched as my furry shark bolted into the air, spinning and dancing in the midst of his attack.'''
        print '\n'
        print '''One problem: he forgot to put on his feathers and down he went! I gasped in fear and ran to the edge of the roof. Guess what! He hadn\'t missed a beat and was already at the base of the tree where the bluejay sat above, squawking and hollaring. Not to cower to a mere house cat, the jay swooped down and rushed Tux head on! The shark shot away in a flurry of fur, feathers and dirt.'''
        print '\n'
        print '''As I climbed down the roof he came bounding back into my arms and held tight until we got inside and both of our heartbeats had calmed.'''
        print 'I think that\'s enough excitement for one day! Come back later for another adventure.'

    else:
        print 'I am following your lead: do not get me lost. Please type Y or N'

else:
    print 'Uhhh I don\'t understand. Please rerun me and type Y or N'





