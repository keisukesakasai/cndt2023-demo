from locust import HttpUser, task, constant

class MyUser(HttpUser):
    wait_time = constant(10)  # 各タスクの実行間隔を1秒に設定

    @task
    def post_data(self):
        headers = {'Content-Type': 'application/json'}
        data = 'Tokyo-To'
        self.client.post("/get", data=data, headers=headers)