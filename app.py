from flask import Flask, render_template

app = Flask(__name__)

# Update the route to match your Nginx 'location /calendar'
@app.route('/calendar')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Keep the port at 8000 as configured in Nginx
    app.run(host='0.0.0.0', port=8000)