
from pokemon_api import getPokemon

__generateBorder = lambda x, symbol='*' : symbol * (x+14)
__frameString = lambda str, symbol='*': f"{__generateBorder(len(str),symbol)}\n\t{str}\n{__generateBorder(len(str),symbol)}"

bannerMessage= 'Who is that Pokemon!?'
banner = __frameString(bannerMessage)
print(banner)

while True:
    name = input('=> ')
    pokemon,types = getPokemon(name)
    typeString = '/'.join(types)
    card =  __frameString(f"It's {name}! Type: {typeString}",'-')
    print(card)
