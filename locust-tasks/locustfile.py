from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(5, 15)
    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def about(self):
        self.client.get("/find-tasks/list")

    @task(3)
    def map(self):
        self.client.get("/find-tasks/map")