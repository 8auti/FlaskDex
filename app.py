from flask import Flask, render_template

import api

# Crear aplicacion
app = Flask(__name__)

lista_pokemon = api.loadPokemon(15,0)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html', lista_pokemon=lista_pokemon)

# Ruta con variable dinamica
@app.route('/pokemon/<nombre>')
def pokemon(nombre):
    pokemon = api.getPokemonData(nombre)
    return render_template('detail.html', pokemon=pokemon)

# Manejar errores
@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template('404.html'), 404

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)