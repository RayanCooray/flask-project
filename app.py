from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    age = request.form.get('age')
    address = request.form.get('address')
    phone = request.form.get('phone')
    return render_template('details.html', name=name, email=email, age=age, address=address, phone=phone)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)