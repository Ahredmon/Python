
from pokemon_api import getPokemon

generate_border = lambda x, symbol='*': symbol * (x+14)
frame_string = lambda str, symbol='*': f"{generate_border(len(str),symbol)}\n\t{str}\n{generate_border(len(str),symbol)}"


def sanitize(s): return s.replace(' ', '-').replace('.', '').lower()


generate_border = lambda x, symbol='*': symbol * (x+14)


BANNER_MESSAGE = 'Who is that Pokemon!?'
BANNER = frame_string(BANNER_MESSAGE)
HELP_BLOCK = frame_string('type q! to exit.', '~')

print(BANNER)
print(HELP_BLOCK)

while True:
    QUIT_CHARACTER = 'q!'
    name = input('=> ')
    # Allow the user to terminate the program
    if name == QUIT_CHARACTER:
        quit()
    display_name = name.strip()
    sanitized_name = sanitize(display_name)
    try:
        pokemon, types = getPokemon(sanitized_name)
        type_string = '/'.join(types)
        card = frame_string(f"It's {display_name}! Type: {type_string}", '-')
        print(card)
    except ValueError as ex:
        print('Error:', ex)
