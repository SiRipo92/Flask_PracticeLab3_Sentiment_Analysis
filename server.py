''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import necessary packages
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer # Import the sentiment analyzer function


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

    # Pass the text to the sentiment_analyzer function and store the response
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    score = response['score']

    # Return a formatted string with the sentiment label and score
    return "The given text has been identified as {} with a score of {}.".format(label.upper(), score)

@app.route("/")
def render_index_page():
    '''This function renders the main application page (index.html).'''
    return render_template("index.html")

if __name__ == "__main__":
    '''This function runs the Flask app and deploys it locally on port 5000.'''
    app.run(debug=True)
