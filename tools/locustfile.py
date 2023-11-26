from locust import HttpUser, task, constant
import random

class MyUser(HttpUser):
    wait_time = constant(3)  # Each task's execution interval set to 10 seconds

    # List of prefectures
    prefectures = ['Hokkaido', 'Aomori-Ken', 'Iwate-Ken', 'Miyagi-Ken', 'Akita-Ken', 
                   'Yamagata-Ken', 'Fukushima-Ken', 'Ibaraki-Ken', 'Tochigi-Ken', 'Gunma-Ken', 
                   'Saitama-Ken', 'Chiba-Ken', 'Tokyo-To', 'Kanagawa-Ken', 'Niigata-Ken', 
                   'Toyama-Ken', 'Ishikawa-Ken', 'Fukui-Ken', 'Yamanashi-Ken', 'Nagano-Ken', 
                   'Gifu-Ken', 'Shizuoka-Ken', 'Aichi-Ken', 'Mie-Ken', 'Shiga-Ken', 'Kyoto-Fu', 
                   'Osaka-Fu', 'Hyogo-Ken', 'Nara-Ken', 'Wakayama-Ken', 'Tottori-Ken', 
                   'Shimane-Ken', 'Okayama-Ken', 'Hiroshima-Ken', 'Yamaguchi-Ken', 'Tokushima-Ken', 
                   'Kagawa-Ken', 'Ehime-Ken', 'Kochi-Ken', 'Fukuoka-Ken', 'Saga-Ken', 
                   'Nagasaki-Ken', 'Kumamoto-Ken', 'Oita-Ken', 'Miyazaki-Ken', 'Kagoshima-Ken', 
                   'Okinawa-Ken']

    @task
    def post_data(self):
        headers = {'Content-Type': 'application/json'}
        # Select a random prefecture
        data = random.choice(self.prefectures)
        self.client.post("/get", data=data, headers=headers)