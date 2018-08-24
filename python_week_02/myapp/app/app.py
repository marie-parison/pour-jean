from flask import Flask, render_template, request
from data.module import MyModule

app = Flask(__name__, template_folder='views')

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemons():
    
    if request.method == 'POST' :
        query = request.form.getlist("Types")
    else :
        query = None

    return render_template('pokemons.html', form = MyModule().BROWSER.get_form(), pokemons = MyModule().BROWSER.get_pokemons(query))

@app.route('/pokemon/<pokemon_name>')
def pokemon(pokemon_name):
    return render_template('pokemon.html', pokemon = MyModule().BROWSER.get_pokemon(pokemon_name))