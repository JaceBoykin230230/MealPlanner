# Meal Planner Application

This is a Meal Planner application designed to showcase backend knowledge using a PostgreSQL database. The application allows users to generate meal plans based on their goals, whether they are trying to lose weight or gain weight.

## Features

- **User Management**: Users can enter their information, including their age, gender, height, weight, and goals (lose weight or gain weight).
- **Meal and Ingredient Management**: The application contains premade meals and ingredients stored in the PostgreSQL database.
- **Meal Plan Generation**: Depending on the user's goals, the application generates meal plans with different types of meals. For users trying to gain weight, high-calorie and high-protein meals are recommended, while for users trying to lose weight, low-calorie meals are suggested.
- **Query Operations**: The application performs various types of queries, including joins, subqueries, filtering, and sorting, to retrieve and manipulate data from the database.
- **User-specific Meal Plans**: Each user can view their personalized meal plan, which is created based on their goals and preferences.

## Table Design in PostgreSQL

The PostgreSQL database consists of the following tables:

1. **Users table**: Contains user information such as User ID, Name, Age, Gender, Height, Weight, and Goals.
2. **Meals table**: Stores information about meals, including Meal ID, Meal Name, Calories, Protein, Carbs, Fat, Meal Type, and Ingredients.
3. **Ingredients table**: Contains details about ingredients, including Ingredient ID, Ingredient Name, Calories, Protein, Carbs, and Fat.
4. **Meal Plan table**: Tracks meal plans generated for users, including Meal Plan ID, User ID, Meal ID, Date, and totals for Calories, Protein, Carbs, and Fat.

## Application Process

1. **User Input**: Users enter their information, including personal details and goals.
2. **Viewing Meals and Ingredients**: Users can view premade meals or individual ingredients.
3. **Meal Plan Generation**: The application generates a personalized meal plan for each user based on their goals and preferences.


