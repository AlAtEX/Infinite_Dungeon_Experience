import os
def Save(alive,Armor,Weapon,Gold,hp,mhp,quest,level,xp):
    with open('Saves/save.sav','w') as save:
        save.write(str([alive,Armor,Weapon,Gold,hp,mhp,quest,level,xp]))
def preLoad():
    try:
        with open('Saves/save.sav','r') as save:
            raw = save.read()
            raw = raw[1:len(raw)- 1]
            values = raw.split(', ')
            if values[0] == 'True':
                values[0] = True
            else:
                values[0] = False
            return values[0]
    except:
        return False
def load(alive):
    with open('Saves/save.sav','r') as save:
        raw = save.read()
        raw = raw[1:len(raw)- 1]
        values = raw.split(', ')
        for num in range(0,len(values)):
            if num == 0:
                values[0] = alive
            elif num == 6:
                if values[6] != 'False':
                    values[6] = float(values[6])
                else:
                    values[6] = False
            else:
                values[num] = int(values[num])
        return values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8]

