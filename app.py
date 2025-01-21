from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    print(f"Registered user: {username}, Email: {email}")

    return render_template('success.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
