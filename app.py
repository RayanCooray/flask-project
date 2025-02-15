from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('form.html')


@app.route('/details',methods=['POST'])
def customer_Details():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    return render_template('details.html', name=name, email=email, phone=phone)


if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80, debug=True)