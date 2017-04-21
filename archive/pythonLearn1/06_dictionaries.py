## Dictionaries (or Maps)

super_villains = {'Fiddler' : 'Isaac Bowin',
'Captain Cold' : 'Leonard Snart',
'Weather Wizard' : 'Mark Mardon',
'Mirror Master' : 'Sam Scudder',
'Pied Piper' : 'Thomas Peterson',}

print(super_villains)

print(super_villains['Captain Cold'])

del super_villains['Fiddler']

super_villains['Pied Piper'] = 'Hartley Rathaway'

print(len(super_villains))

print(super_villains)

print(super_villains.get('Pied Piper'))

print(super_villains.keys())

print(super_villains.values())
