from flask import Flask, request, jsonify , Response
from flask_cors import CORS
import json
from repo_analyzer import get_github_repo_name , start_analysis

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from frontend

@app.route('/analyze-repo', methods=['POST'])
def analyze_repo():
    
        data = request.get_json()
        repo_url = data.get("url")

        print(repo_url)
        
        if not repo_url:
            return jsonify({"error": "Repository URL is required"}), 400
        

        data = start_analysis(repo_url)
        
        return jsonify(data)

        
   
            
        
    
    




if __name__ == '__main__':
    app.run(debug=True)
