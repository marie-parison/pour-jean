from weboob.browser import PagesBrowser, URL
from .pages.pokemon import PokemonPage, DetailPage


class MyBrowser(PagesBrowser):
    BASEURL = 'https://www.pokebip.com'

    """
    Pages definition
    """

    pokemon = URL(r'/pokedex/pokemon/(?P<pagename>)', DetailPage)
    pokemons_with_query = URL(r'/pokedex/pokemon(?P<query>.*)', PokemonPage)
    pokemons = URL(r'/pokedex/pokemon$', PokemonPage)

    def get_form(self):
        self.pokemons.go()

        return self.page.get_form()

    def get_pokemons(self, query=None):

        if query != None :
            req = "?types="
            for q in query :
                req += q + "%2C"
            req = req[0:-3]
            self.pokemons_with_query.go(query = req)
        else :
            self.pokemons.go()

        pokemons = []

        for pokemon in self.page.get_pokemons():
           pokemons.append({"id" : pokemon.id, "name" : pokemon.name, "pokedex_id" : pokemon.pokedex_id, "type" : pokemon.type})

        return pokemons
    
    def get_pokemon(self, pokemon_name):
        self.pokemon.go(pagename = pokemon_name)

        return self.page.get_pokemon()
    
    



        
