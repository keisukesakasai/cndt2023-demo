from locust import HttpUser, task, constant
import random

class MyUser(HttpUser):
    wait_time = constant(3)

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

    # Random weights for each prefecture
    weights = [10, 8, 7, 9, 6, 5, 8, 7, 6, 5, 9, 8, 10, 9, 7, 
               6, 5, 4, 3, 7, 8, 9, 10, 6, 5, 4, 10, 9, 8, 7, 
               3, 4, 5, 6, 7, 8, 4, 3, 2, 9, 8, 7, 6, 5, 4, 
               3, 2]

    @task
    def post_data(self):
        headers = {'Content-Type': 'application/json'}
        # Select a prefecture based on weights
        data = random.choices(self.prefectures, weights=self.weights, k=1)[0]
        self.client.post("/get", data=data, headers=headers)
