from locust import HttpUser, between, task

class JSONPostUser(HttpUser):
    wait_time = between(1, 3)  

    @task
    def post_request(self):
        # Define JSON payload
        payload = {
            "name": "John Doe",
            "job":"SDET"
        }

        # Send POST request with JSON payload
        response = self.client.post("/api/users", json=payload)

        if response.status_code == 201:
            self.environment.events.request.fire(
                request_type="POST",
                name="/api/users",
                response_time=response.elapsed.total_seconds() * 1000,
                response_length=len(response.content),
            )
        else:
            self.environment.events.request.fire(
                request_type="POST",
                name="/api/users",
                response_time=response.elapsed.total_seconds() * 1000,
                exception=None,
            )
