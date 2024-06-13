from time import sleep
from locust import HttpUser, task, between


class QuickStartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/about")

    @task(3)
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            sleep(1)

    def on_start(self):
        self.client.post(
            "/login", json={"username": "steven", "password": "supersecret"}
        )
