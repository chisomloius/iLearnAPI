# ---EXAMPLES OF ORDINARY INSTANCE OF FLASK APP---
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World API"

# if __name__ == '__main__':
#     app.run()


from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

recipes = [ 
                { 'id': 1, 
                    'name': 'Egg Salad', 
                    'description': 'This is a lovely egg salad recipe.' 
                }, 

                {  'id': 2, 
                    'name': 'Tomato Pasta', 
                    'description': 'This is a lovely tomato pasta recipe.'   
                },
                {  'id': 3, 
                    'name': 'Ewagoyin', 
                    'description': 'This is a savouring type of beans.'   
                },
                {  'id': 4, 
                    'name': 'Afang', 
                    'description': 'This is a lovely soup made of vegetables'   
                },
                {  'id': 5, 
                    'name': 'Oil Sauce', 
                    'description': 'This is a oil soup without actual oil.'   
                }
            ]


# --- ADD THE ALL GET RECIPES FUNCTION AND ROUTE---
@app.route('/recipes/', methods=['GET']) # GET method is a default method
def get_recipes():

    return jsonify({'data': recipes})


# --- ADD A GET RECIPE FUNCTION AND ROUTE --
@app.route('/recipes/<int:recipe_id>', methods=['GET']) 
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    
    if recipe:
        return jsonify(recipe)

    return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND


# --- ADD A CREATE_RECIPE FUNCTION AND ROUTE---
@app.route('/recipes', methods=['POST'])
def create_recipe():
    mydata = request.get_json()

    name = mydata.get('name')
    description = mydata.get('description')

    recipe = {
                'id': len(recipes) + 1,
                'name': name,
                'description': description
    }
    recipes.append(recipe)
    # when succesful it will return the below
    return jsonify(recipe), HTTPStatus.CREATED


# --- ADD AN UPDATE_RECIPE FUCNTION AND ROUTE ---
@app.route('/recipes/<int:recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)

    if not recipe:
        return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
    mydata = request.get_json()

    recipe.update(
                    {
                        'name': mydata.get('name'),
                        'description': mydata.get('description')
                    }
                )
    return jsonify(recipe)

# ---START FLASK APP ---
if __name__ == '__main__':
        app.run()