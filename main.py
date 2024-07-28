from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# @app.get("/main")
# def main():
#     return render_template("index.html")

# @app.get("/menu")
# def menu():
#     return render_template("menu.html")

@app.get("/register")
def register_get():
    return render_template("register.html")

@app.post("/register")
def register_post():
    nickname = request.form.get('nickname')
    psd = request.form.get('password')
    return f"nickname:{nickname}, password:{psd}"

@app.get("/authorization")
def authorization_get():
    return render_template("authorization.html")

@app.post("/authorization")
def authorization_post():
    message = ''
    email = request.form.get('email')
    psd = request.form.get('psd')
    repeat_psd = request.form.get('repeat_psd')
    print(psd,repeat_psd)
    if psd == repeat_psd:
        message = f"email:{email}, password:{psd}"
    return message

if __name__ == '__main__':
    app.run(
        host="0.0.0.1",
            port=8080, 
            debug=True,
            )