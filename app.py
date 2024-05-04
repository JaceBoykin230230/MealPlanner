from flask import Flask, render_template, request
import sqlite3
import random

app = Flask(__name__)

# generate random number for port to  use
portnum = random.randint(5000, 65535)

# Define routes

def get_db_connection():
    conn = sqlite3.connect('mealplanner.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    # home page shows all meals and ingredients
    conn = get_db_connection()
    cur = conn.cursor()
    # order by meal type
    cur.execute('SELECT * FROM Meals ORDER BY meal_type ASC')
    meals = cur.fetchall()
    # order by calories
    cur.execute('SELECT * FROM Ingredients ORDER BY calories DESC')
    ingredients = cur.fetchall()
    conn.close()
    # html will show both of these queries in tables on screen.
    return render_template('home.html', meals=meals, ingredients=ingredients)

# Route for adding a user
@app.route('/add-user')
def add_user():
    return render_template('add-user.html')

# route for submitting form to add user
@app.route('/add-user-submit', methods=['POST'])
def add_user_submit():
    conn = get_db_connection()
    cur = conn.cursor()
    data = request.form
    cur.execute('INSERT INTO Users (name, age, gender, height, weight, goals) VALUES (?, ?, ?, ?, ?, ?)',
                (data['name'], data['age'], data['gender'], data['height'], data['weight'], data['goals']))
    conn.commit()
    conn.close()
    return 'User added'

# Route for showing each user their meal plan based on their goals
# asks for their name, looks them up in database (if they exist) and then returns three meals that fit their goal (lose weight, gain weight)
# get user by name
# get their goal (lose weight/gain weight), based on this, retrieve three meals for their needs
# meal plan  = breakfast, lunch, dinner (over 500 calories per meal for gaining weight, under 500 calories per meal for losing weight)
# redesign the table to allow for storing breakfast, lunch and dinner entries one at a time, non null values

@app.route('/user-meal-plan')
def user_meal_plan():

    return render_template('user-meal-plan.html')

@app.route('/user-meal-plan-submit', methods=['POST'])
def user_meal_plan_submit():
    conn = get_db_connection()
    cur = conn.cursor()
    # get data from form
    data = request.form
    # get user by name
    cur.execute('SELECT * FROM Users WHERE name = ?', (data['name'],))
    user = cur.fetchone()
    # get their goal
    cur.execute('SELECT goals FROM Users WHERE name = ?', (data['name'],))
    goal = cur.fetchone()

    # get three meals for their needs
    if goal == 'lose weight':
        cur.execute('SELECT * FROM Meals WHERE calories < 500 ORDER BY RANDOM() LIMIT 3')
        # for each meal, depending on whether its meal type is breakfast, lunch or dinner, store it in the Meal_Plan
        # table
        meals = cur.fetchall()
        for meal in meals:
            if meal['meal_type'] == 'breakfast':
                cur.execute('INSERT INTO Meal_Plan (user_id, meal_id, breakfast) VALUES (?, ?, ?)', (user['id'], meal['meal_id'], meal['meal_type']))
            elif meal['meal_type'] == 'lunch':
                cur.execute('INSERT INTO Meal_Plan (user_id, meal_id, lunch) VALUES (?, ?, ?)', (user['id'], meal['meal_id'], meal['meal_type']))
            elif meal['meal_type'] == 'dinner':
                cur.execute('INSERT INTO Meal_Plan (user_id, meal_id, dinner) VALUES (?, ?, ?)', (user['id'], meal['meal_id'], meal['meal_type']))
    elif goal == 'gain weight':
        cur.execute('SELECT * FROM Meals WHERE calories > 500 ORDER BY RANDOM() LIMIT 3')
        meals = cur.fetchall()
        for meal in meals:
            if meal['meal_type'] == 'breakfast':
                cur.execute('INSERT INTO Meal_Plan (user_id, meal_id, breakfast) VALUES (?, ?, ?)', (user['id'], meal['meal_id'], meal['meal_type']))
                conn.commit()
            elif meal['meal_type'] == 'lunch':
                cur.execute('INSERT INTO Meal_Plan (user_id, meal_id, lunch) VALUES (?, ?, ?)', (user['id'], meal['meal_id'], meal['meal_type']))
                conn.commit()
            elif meal['meal_type'] == 'dinner':
                cur.execute('INSERT INTO Meal_Plan (user_id, meal_id, dinner) VALUES (?, ?, ?)', (user['id'], meal['meal_id'], meal['meal_type']))
                conn.commit()

    conn.close()
    return "Meal plan added"
    

if __name__ == '__main__':
    app.run(debug = True, host = "10.80.23.119"  , port=portnum)

