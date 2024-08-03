from flask import Flask, render_template


app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html", menu=MENU)

@app.get("/menu")
def menu():
    return render_template("menu.html", menu=MENU)

MENU = {
    index.__name__,
    menu.__name__,
}

if __name__ == '__main__':
    app.run(
        host="0.0.0.1",
            port=8080, 
            debug=True,
            )
    
