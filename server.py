''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import necessary packages
from flask import Flask, render_template, request
from sentiment_analysis import sentiment_analyzer # Import the sentiment analyzer function


# Initiate the flask app
app = Flask(__name__)

@app.route("/sentimentAnalyzer", methods=["POST"])
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    if request.method == "POST":
        text_to_analyze = request.form["text"]  # Get the text from the HTML form
        result = sentiment_analyzer(text_to_analyze)  # Call sentiment analysis function
        
        # Extract sentiment label and score from the result
        sentiment_label = result.get("label", "No Label Found")
        sentiment_score = result.get("score", "No Score Found")
        
        return render_template("index.html", label=sentiment_label, score=sentiment_score)

@app.route("/")
def render_index_page():
    '''This function renders the main application page (index.html).'''
    return render_template("index.html")

if __name__ == "__main__":
    '''This function runs the Flask app and deploys it locally on port 5000.'''
    app.run(debug=True)
