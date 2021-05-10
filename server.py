from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Can't see my file" # set a secret key for security purposes

@app.route('/')
def user():
    if 'count' not in session:
        session['count'] = 0
    session['count']+=1
    return render_template('index.html')

@app.route('/visits)')
def num_user():
    
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.