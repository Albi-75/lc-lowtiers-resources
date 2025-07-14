# dumb function to help create the VR post
# the input is the list of pokemon that you can copy, ordered by viability, from the google doc once votes have concluded
# the output is just a list like
# :crabrawler: Crabrawler
# :meowth-galar: Meowth-Galar
# and so on, which you can copy into the VR post so you don't lose your mind doing it manually
# it does NOT tell you which pokemon are in which tier, so you still have to do that manually, but it's easier copy-pasting

mons = ['Crabrawler',
'Meowth-Galar',
'Voltorb',
'Doduo',
'Bramblin',
'Numel',
'Sandshrew',
'Wattrel',
'Tentacool',
'Dewpider',
'Grimer-Alola',
'Koffing',
'Meowth',
'Croagunk',
'Axew',
'Buizel',
'Drilbur',
'Larvitar',
'Nymble',
'Cottonee',
'Pikipek',
'Rhyhorn',
'Riolu',
'Golett',
'Magnemite',
'Trapinch',
'Corphish',
'Gible',
'Salandit',
'Cetoddle',
'Litten',
'Bagon',
'Greavard',
'Squirtle',
'Varoom',
'Bulbasaur',
'Hippopotas',
'Poltchageist',
'Zorua',
'Chespin',
'Cranidos',
'Cufant',
'Gimmighoul-Roaming',
'Quaxly',
'Sandygast',
'Slowpoke',
'Slowpoke-Galar',
'Ekans',
'Grimer',
'Skiddo',
'Barboach',
'Cacnea',
'Charmander',
'Ducklett',
'Finizen',
'Meowth-Alola',
'Munchlax',
'Pineco',
'Skrelp',]

# a function that for every pokemon prints ":<lowercase pokemon name>: pokemon name", keeping hyphens
def format_pokemon_name(pokemon):
    formatted_name = pokemon.lower().replace('-', '-')
    return f":{formatted_name}: {pokemon}"

# Print the formatted names for each pokemon
for mon in mons:
    print(format_pokemon_name(mon))