import random
'''
with open('Configfiles/.txt', 'r') as x:
    raw = x.read()
    entries = raw.split('|')
     = entries
'''
def openConfigs():
    with open('Configfiles/intro.txt', 'r') as x:
        raw = x.read()
        entries = raw.split('|')
        intro = random.choice(entries)
    with open('Configfiles/colours.txt', 'r') as x:
        raw = x.read()
        entries = raw.split('|')
        colours = entries
    with open('Configfiles/ename.txt','r') as x:
        raw = x.read()
        entries = raw.split('|')
        enames = entries
    with open('Configfiles/encounter.txt','r') as x:
        raw = x.read()
        entries = raw.split('|')
        encounters = entries
    with open('Configfiles/deathtexts.txt', 'r') as x:
        raw = x.read()
        entries = raw.split('|')
        deathtexts = entries
    with open('Configfiles/edeathtexts.txt', 'r') as x:
        raw = x.read()
        entries = raw.split('|')
        edeathtexts = entries
    with open('Configfiles/enterTexts.txt', 'r') as x:
        raw = x.read()
        entries = raw.split('|')
        enterTexts = entries
    with open('Configfiles/exitTexts.txt', 'r') as x:
        raw = x.read()
        entries = raw.split('|')
        exitTexts = entries
    return intro, colours, enames, encounters, deathtexts, edeathtexts, enterTexts, exitTexts
def itemConfigs():
    with open('Configfiles/Items/weapons.txt', 'r') as x:
        raw = x.read()
        entries = raw.split('|')
        weapons = entries
    with open('Configfiles/Items/armor.txt', 'r') as x:
        raw = x.read()
        entries = raw.split('|')
        armor = entries
    with open('Configfiles/Items/weaponMats.txt', 'r') as x:
        raw = x.read()
        entries = raw.split('|')
        weaponMats = entries
        for material in weaponMats:
            num = weaponMats.index(material)
            material = material.split(':')
            try:
                material[0] = int(material[0])
            except:
                pass
            weaponMats[num] = material
    with open('Configfiles/Items/armorMats.txt', 'r') as x:
        raw = x.read()
        entries = raw.split('|')
        armorMats = entries
        for material in armorMats:
            num = armorMats.index(material)
            material = material.split(':')
            try:
                material[0] = int(material[0])
            except:
                pass
            armorMats[num] = material
    with open('Configfiles/Items/potionSizes.txt', 'r') as x:
        raw = x.read()
        entries = raw.split('|')
        potionSizes = entries
        for material in potionSizes:
            num = potionSizes.index(material)
            material = material.split(':')
            try:
                material[0] = int(material[0])
            except:
                pass
            potionSizes[num] = material
    return weapons, armor, weaponMats, armorMats, potionSizes
itemConfigs()
