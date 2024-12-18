''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import necessary packages
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer


# Initiate the flask app
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        # If there's no text provided, return the error message
        return render_template('index.html', error="Please provide some text to analyze.")

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

    # Check if the label is None, indicating an error or invalid input
    if label is None:
        print("Invalid input! Try again.")  # Print error in the console
        return "Invalid input! Try again."  # Return error message to the client
    # Return a formatted string with the sentiment label and score
    return f"The given text has been identified as {label.upper()} " \
       f"with a score of {score}."

@app.route("/")
def render_index_page():
    '''This function renders the main application page (index.html).'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
