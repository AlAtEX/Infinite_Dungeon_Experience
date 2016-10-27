with open(input('File name without extention:\n')+'.txt', 'w') as x:
    position = 'main'
    currentdepth = 0
    currentnums = {}
    length = {}
    end = False
    x.write(input('Text shown when event starts: ') + '\n')
    #end: tells the computer to end the current tag.
    while True:
        item = input('What happens during {a}, "choice", "fight", "trap", "store", "print", "loot"(tresure), "random"(same as choice but random) or "end": '.format(a = position))
        if item == 'choice':
            x.write('!c|' + input('Text for choice: ') + '|')
            number_of_options = int(input('How many choices?: '))
            for num in range(0,number_of_options):
                x.write(input('Text for option {a}: '.format(a=num + 1)) + '|')
            x.write(str(number_of_options) + '\n')
            currentdepth += 1
            currentnums[str(currentdepth)] = 1
            length[str(currentdepth)] = number_of_options
            position = 'choice{a}'.format(a=currentdepth)
            x.write('!1\n')
        if item == 'random':
            x.write('!r|')
            number_of_options = int(input('How many choices?: '))
            x.write(str(number_of_options) + '\n')
            currentdepth += 1
            currentnums[str(currentdepth)] = 1
            length[str(currentdepth)] = number_of_options
            position = 'choice{a}'.format(a=currentdepth)
            x.write('!1\n')
        if item == 'fight':
            FoR = input('Fixed enemy(In config) or random enemy(like random enemy encounters) "f" or "r": ')
            if FoR == 'f':
                print('All numbers are multiplied by the current player level.')
                emhp = input('Enemy health: ') 
                x.write('!ff|' + emhp + '|' + emhp + '|')
                x.write(input('Enemy attack power: ') + '|')
                x.write(input('Enemy armor: ') + '|')
                x.write(input('Enemy name: ') + '|')
                x.write(input('Encounter text: ') + '|')
                x.write(input('Player death text: ') + '|')
                x.write(input('Enemy death text: ') + '|')
                x.write(input('Gold Dropped: ') + ',')
                weapon = input('Special weapon dropped? ("yes" or "no"): ')
                if weapon == 'yes':
                    x.write(input('Description: ') + '/')
                    x.write(input('Modifier to level: ') + ',')
                else:
                    x.write('False,')
                armor = input('Special armor dropped? ("yes" or "no"): ')
                if armor == 'yes':
                    x.write(input('Description: ') + '/')
                    x.write(input('Modifier to level: '))
                else:
                    x.write('False')
                x.write('|' + input('Xp: '))
            else:
                x.write('!fr')
            x.write('\n')
            
        if item == 'end':
            if currentdepth == 0:
                end = True
                break
            x.write('!e\n')
            for num in range(0,currentdepth):
                if currentdepth > 0:
                    if currentnums[str(currentdepth)] < length[str(currentdepth)]:
                        currentnums[str(currentdepth)] += 1
                        x.write('!{a}\n'.format(a = currentnums[str(currentdepth)]))
                    else:
                        currentdepth -= 1

        if item == 'print':
            x.write('!p|' + input('Text to be printed.: ') + '\n')

        if item == 'store':
            #!sf|entertext|exittext|item1::item2::item3...
            #or
            #!st|entertext|exittext|type
            #or
            #!sr
            #{'desc':'Wooden sword, 5 damage.','price':100,'type':'st','mod':5}
            #!sf|Hi.|Bye.|sword##2##st##2::shield##2##ar##2
            #!st|xp
            #!sr|
            FoToR = input('Fixed store(all items in config) or type store(like weapon shop, health potion shop...)or random store(like stores found normally) "f", "t" or "r": ')
            if FoToR == 'f':
                x.write('!sf|' + input('Store enter text: ') + '|')
                x.write(input('Store exit text: ') + '|')
                items = []
                while True:
                    for thing in items:
                        print(thing)
                    item = input('More items? "y" or "n": ')
                    if item == 'y':
                        thing = input('Item name(include modifier i.e "name: 5 damage"): ')+'##'+input('Item cost(times level): ')+'##'+input('Item type (st, ar, hp, mhp, xp): ')+'##'+input('Item modifier(to level): ')+'::'
                        x.write(thing)
                        items.append(thing)
                    else:
                        x.write('\n')
                        break
            if FoToR == 't':
                x.write('!st|'+input('Store enter text: ')+'|'+input('Store exit text: ')+'|'+input('Type("weapon","armor","healthPotion","healthMax","xp"): ')+'\n')
            if FoToR == 'r':
                x.write('!sr|\n')
        
        if item == 'loot':
            #(Treasure)
            #!tc|1|4
            ###Chest#Minimum items#Maximum items
            CorF = input('Chest(random item(s)) or Fixed item(Wooden Sword)? Enter "c" or "f"')
            if CorF == 'c':
                x.write('!tc|' + input('Minimum num of items in chest: ')+'|'+input('Maximum num of items in chest'))
            if CorF == 'f':
                pass
