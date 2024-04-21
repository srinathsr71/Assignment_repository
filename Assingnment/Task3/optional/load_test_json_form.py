from locust import HttpUser, task
class UserBehavior(HttpUser):
    @task
    def submit_json(self):
        payload = {"name": "John Doe", "email": "john@example.com"}
        self.client.post("/submit-json", json=payload)
    @task
    def submit_form_data(self):
        payload = {"name": "Jane Doe", "email": "jane@example.com"}
        self.client.post("/submit-json", data=payload)
