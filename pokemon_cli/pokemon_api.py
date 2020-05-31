
import json
from pprint import pprint as pp
from urllib.error import HTTPError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen

POKEMON_URL = 'https://pokeapi.co/api/v2/'


def _generate_url(pokemon): return POKEMON_URL + 'pokemon/' + pokemon


def _get(url): return urlopen(
    Request(url, headers={'User-Agent': 'Code Club'}))


def getPokemon(pokemonName):
    """ Given a pokemon name, return it's type from pokeapi

    Arguments:
        pokemonName str -- The name of a pokemon
    Returns:
        tuple (pokemon, types)
    Raises:
        ValueError: If Pokemon is not found within API.
    """

    url = _generate_url(pokemonName)
    # This is a little bit of a hack that will preserve the protocol section of the url when quoting.
    url = url[:6] + quote(url[6:])

    try:
        with _get(url) as response:
            data = response.read()
            data = json.loads(data)
            types = [t['type']['name'] for t in data['types']]
            return pokemonName, types

    except HTTPError as ex:
        # Dictionary below is useful for simplifying branching.
        codes = {
            404: ValueError(f"{pokemonName} is not a valid Pokemon"),
        }

        code = ex.getcode()
        exception_object = codes.get(code)

        # If http status code is not registed with codes, throw the initial exeption.
        if(exception_object is None):
            raise ex
        else:
            raise exception_object
