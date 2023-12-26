from flask import Flask, render_template
from dict import recipes

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    # return 'Hello World!'
    return render_template('index.html')

@app.route('/recipes/<int:recipe_number>')
def recipe_list(recipe_number):
    return render_template('index.html', recipe_id = recipes[recipe_number], recipe_number = recipe_number)