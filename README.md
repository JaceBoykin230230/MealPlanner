# Meal Planner Application

This is a Meal Planner application designed to show backend knowledge using a PostgreSQL database. The application allows users to generate meal plans based on their goals, whether they are trying to lose weight or gain weight.

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


