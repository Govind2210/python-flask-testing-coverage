# Import Locust classes
from locust import HttpUser, task, between

# Each simulated user will behave like this class
class WebsiteUser(HttpUser):
    """
    HttpUser:
        - Represents a single user that makes HTTP requests to your Flask app.
        - Each user runs in parallel (you can simulate 10, 100, 1000+ users).
    """

    # How long a simulated user waits before making the next request
    # Here: between 1 to 2 seconds
    wait_time = between(1, 2)

    @task(3)  
    def load_homepage(self):
        """
        This task hits the homepage ("/").
        The number (3) means: it is 3x more likely to run than tasks with weight 1.
        Example: If a user does 6 requests → 3 will be homepage, 2 about, 1 contact.
        """
        self.client.get("/")  # send GET request to http://127.0.0.1:5000/

    @task(2)
    def load_about(self):
        """
        This task hits the about page ("/about").
        Weight = 2 → called less often than homepage but more than contact.
        """
        self.client.get("/about")  # send GET request to http://127.0.0.1:5000/about

    @task(1)
    def load_contact(self):
        """
        This task hits the contact page ("/contact").
        Weight = 1 → least frequent of the three.
        """
        self.client.get("/contact")  # send GET request to http://127.0.0.1:5000/contact
