# python-flask-testing-coverage

Flask Performance Testing Project 🚀

This project is a simple Flask web application with 3 routes (/, /about, /contact) and includes:

Locust → for load testing

pytest → for unit testing

coverage → for test coverage reports

📂 Project Structure
Pytest-performance-testing/
│── app.py              # Flask application
│── locustfile.py       # Locust performance test
│── test_app.py         # Unit tests for Flask app
│── requirements.txt    # Python dependencies
│── README.md           # Documentation
│── venv/               # Virtual environment (ignored in git)

⚡ Setup Instructions (Windows)
1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install -r requirements.txt


If you don’t have requirements.txt, install manually:

pip install flask pytest coverage locust

🖥️ Running the Flask App
python app.py


Server will start at 👉 http://127.0.0.1:5000

Routes available:

/ → Homepage

/about → About page

/contact → Contact page

🏋️ Performance Testing with Locust

Keep Flask running (python app.py)

Open a new terminal and run:

locust -f locustfile.py


Open 👉 http://localhost:8089

Enter:

Number of users (e.g., 50)

Spawn rate (e.g., 5)

Host → http://127.0.0.1:5000

Start swarming 🚀

✅ Unit Testing with pytest

Run:

pytest

📊 Test Coverage with coverage

Run tests with coverage:

coverage run -m pytest


Show coverage report in terminal:

coverage report -m


(Optional) Generate HTML report:

coverage html
