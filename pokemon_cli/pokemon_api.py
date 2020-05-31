
import json
from urllib.request import Request, urlopen
from urllib.parse import urlparse, quote
from urllib.error import HTTPError
from pprint import pprint as pp

pokemon_url = 'https://pokeapi.co/api/v2/'

_generate_url = lambda pokemon :pokemon_url + 'pokemon/' + pokemon

_get = lambda url : urlopen(Request(url,headers={'User-Agent':'Code Club'}))

def getPokemon(pokemonName):
    """ Given a pokemon name, return it's type from pokeapi

    Arguments:
        pokemonName str -- The name of a pokemon
    Returns:
        tuple
    """
    _url = _generate_url(pokemonName)
    _url =  _url[:6] + quote(_url[6:])
    try:
         with _get(_url) as response:
            data= response.read() 
            data= json.loads(data)
            types= [t['type']['name'] for t in data['types']]
            return pokemonName, types

    except HTTPError as ex:
         codes ={
             404 : lambda x : ValueError(f"{pokemonName} is not a valid Pokemon")
         }
         execption = codes.get(ex.getcode())
         pp(execption)
         if(execption):
             raise execption
         raise ex    

