from trackingapp import app

"""
This file runs the server at a given port
"""

FLASK_PORT = 5000

if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT, host='0.0.0.0')
