from flask import Flask,jsonify,request
import ipl
app = Flask(__name__)

@app.route('/')
def home():
    return "Ipl match Analysis API"

@app.route('/api/teams')
def teams():
    teams = ipl.teamsApi()
    return jsonify(teams)

@app.route('/api/teamVteam')
def teamVteam():
    app.json.sort_keys = False 
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = ipl.teamVteam(team1,team2)
    app.json.sort_keys = False 
    return jsonify(response)

app.run(debug=True)