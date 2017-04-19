"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/', methods=["POST"])
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet', methods=["POST"])
def greet_person():
    """Greet user with compliment."""

    player = request.form.get("person")

    compliment = sample(AWESOMENESS, 3)

    compliment_string = "%s, %s, and %s" % (compliment[0], compliment[1], compliment[2])


    return render_template("compliment.html",
                           person=player,
                           compliment=compliment_string)


@app.route('/game', methods=["POST"])
def show_madlib_form():
    response = request.form.get("response")

    if response == 'no':
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib', methods=["POST"])
def show_madlib():
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")
    person = request.form.get("person")
    color = request.form.get("color")
    city = request.form.get("city")

    food_list = [request.form.get("ice-cream"), request.form.get("chocolate"),
                    request.form.get("cookies")]

    new_food_list = [food for food in food_list if food]
    if len(new_food_list) == 3:
        food_string = "%s, %s, and %s" % (new_food_list[0], new_food_list[1], new_food_list[2])
    elif len(new_food_list) == 2:
        food_string = "%s and %s" % (new_food_list[0], new_food_list[1])
    elif len(new_food_list) == 1:
        food_string = new_food_list[0]
    else:
        food_string = "nothing"

    return render_template(choice(["madlib.html", "madlib2.html"]), city=city, noun=noun,
        adjective=adjective, person=person, color=color, food_list=food_string)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
