from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder="web")

@app.route("/")
def home():
    try:
    
        r = requests.get(f"https://boozeapi.com/api/v1/cocktails", timeout=5)
        r.raise_for_status() 
        data = r.json()
        drinks = data.get("data", [])
    except Exception as e:
        print(f"Chyba: {e}")
        drinks = []
    


    return render_template("index.html", cocktails=drinks)

if __name__ == "__main__":
    app.run(debug=True)
