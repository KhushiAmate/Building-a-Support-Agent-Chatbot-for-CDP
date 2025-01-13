Support Agent Chatbot for CDP

This project is a Flask-based web application designed to serve as a support agent chatbot for Customer Data Platforms (CDPs). Users can ask questions related to a specific CDP, and the chatbot provides relevant answers.

Features

User-Friendly Interface: A simple web interface for users to input the CDP name and their questions.

Dynamic Responses: Uses a chatbot model to generate responses to user queries.

Error Handling: Provides meaningful feedback when inputs are missing or if the chatbot cannot process a query.

Project Structure

chatbot/
|-- app.py                # Main Flask application
|-- templates/
|   |-- index.html        # HTML template for the application
|-- models/
|   |-- chatbot.py        # Chatbot model implementation
|-- static/               # Static files (CSS, JS, Images)
|-- README.md   


Requirements

Python 3.8+

Flask

Install Dependencies

Run the following command to install the required Python libraries:
pip install flask

How to Run the Application

Clone the Repository:

git clone <repository-url>
cd <repository-directory>

Run the Application:

python app.py

Access the Application:
Open your web browser and navigate to http://127.0.0.1:5000/.

How It Works

Users enter the CDP name and their question in the form provided on the homepage.

Upon submission, the application:

Validates the inputs.

Passes the CDP name and question to the chatbot model via get_answer() in models/chatbot.py.

The chatbot model processes the inputs and returns an answer.

The answer is displayed on the webpage.

Error Handling

If the CDP name or question is missing, the application prompts the user to provide the required fields.

If the chatbot cannot generate an appropriate response, it displays an error message such as:

"Error: Unable to process the query."

"Sorry, I don't have enough information to answer that."

Example Usage

Input: CDP Name: Salesforce CDP, Question: How to integrate Salesforce with other platforms?

Output: "Salesforce CDP can be integrated using APIs and prebuilt connectors. Refer to the documentation for more details."

