from locust import HttpUser, task


class HomePage(HttpUser):
    @task
    def home_page(self):
        self.client.get("/")
