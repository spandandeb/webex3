from flask import Flask, request, render_template

app = Flask(__name__)

# Homepage Route
@app.route('/')
def home():
    name = request.args.get('name', 'Guest')  # Get name from query parameter (default: Guest)
    return f"<h1 style='text-align: center;'>Welcome, {name}!</h1><p style='text-align: center;'><a href='/contact'>Go to Contact Form</a></p>"

# Contact Page Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"<h1 style='text-align: center;'>Thank You!</h1><p style='text-align: center;'>Name: {name}</p><p style='text-align: center;'>Email: {email}</p><p style='text-align: center;'><a href='/'>Go Back</a></p>"
    return '''
    <div style='display: flex; justify-content: center; align-items: center; height: 100vh;'>
        <form action='/contact' method='post' style='text-align: center; padding: 20px; border: 1px solid #ccc; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);'>
            <label>Name:</label>
            <input type='text' name='name' required><br><br>
            <label>Email:</label>
            <input type='email' name='email' required><br><br>
            <button type='submit'>Submit</button>
        </form>
    </div>
    '''

# Thank You Page Route
@app.route('/thank_you')
def thank_you():
    return "<h1 style='text-align: center;'>Thank You for Your Submission!</h1><p style='text-align: center;'><a href='/'>Go Back</a></p>"

if __name__ == '__main__':
    app.run(debug=True)
