import re

from app.models.pokemon import Pokemon, PokemonDetail, Form

from weboob.browser.pages import HTMLPage
from weboob.capabilities.base import BaseObject, Field, StringField, IntField
from weboob.browser.elements import TableElement, ItemElement, method
from weboob.browser.filters.standard import CleanText, CleanDecimal, TableCell, Type
from weboob.browser.filters.html import Attr


class PokemonPage(HTMLPage):
    @method
    class get_pokemons(TableElement):
        item_xpath = '//table[contains(@class, "table")]//tr[td]'
        head_xpath = '//table[contains(@class, "table")]//th'

        col_id = re.compile('#')
        col_name = re.compile('Nom')
        col_type = re.compile('Type')
        col_num = re.compile('Numéro')

        class item(ItemElement):
            klass = Pokemon

            obj_id = CleanDecimal('td[1]')
            obj_pokedex_id = obj_id
            
            def obj_type(self):
                types = []

                for type in TableCell('type')(self)[0].xpath('./div'):
                    types.append(Attr('.//img', 'alt')(type))

                return types
            
            def obj_name(self):
                return CleanText(TableCell('name')(self)[0].xpath('./strong/a/text()'))(self)
        
    @method
    class get_form(ItemElement):
        klass = Form

        obj_title = CleanText('//*[@id="pokemon-search"]/div[1]/div[1]/div/label/text()')
        
        def obj_types(self):
            types =  self.page.doc.xpath('//*[@id="pokemon-search"]/div[1]/div[2]/div/label')
            
            # a = types[1].xpath('./img/@alt')[0]
            # b = types[1].xpath('./input/@id')[0].replace('type-', '')
            # id_types = self.page.doc.xpath('//*[@id="pokemon-search"]/div[1]/div[2]/div/label/input/@id')
            
            return [ { "name" : elm.xpath('./img/@alt')[0], "id" : elm.xpath('./input/@id')[0].replace('type-', '') } for elm in types ]


class DetailPage(HTMLPage):
    @method
    class get_pokemon(ItemElement):
        klass = PokemonDetail

        obj_name = CleanText('//*[@id="content"]/div[3]/h1/text()')
        obj_img = CleanText('//*[@id="content"]/div[4]/div[1]/div/img/@src')

