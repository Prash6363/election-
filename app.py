from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/constituencies')
def constituencies():
    return render_template('Distribution of Constituencies Over All States.html')

@app.route('/top-parties')
def top_parties():
    return render_template('Top 10 Parties with the Most Constituencies Won.html')

@app.route('/party-dominance')
def party_dominance():
    return render_template('Party Dominance by State.html')

@app.route('/criminal-impact')
def criminal_impact():
    return render_template('Impact of Criminal Background on Election Outcomes.html')

@app.route('/gender-distribution')
def gender_distribution():
    return render_template('Gender Distribution Among Candidates.html')

@app.route('/education')
def education():
    return render_template('Educational Qualifications of Winning Politicians by Party.html')

@app.route('/ml-comparison')
def ml_comparison():
    return render_template('Comparison of ML models.html')

@app.route('/age-distribution')
def age_distribution():
    return render_template('Age Distribution Among Elected Candidates.html')

if __name__ == '__main__':
    app.run(debug=True)
