CREATE DATABASE IF NOT EXISTS western;
USE western;

CREATE TABLE IF NOT EXISTS population (
    prefecture_id INT AUTO_INCREMENT PRIMARY KEY,
    prefecture VARCHAR(255),
    population INT
);

INSERT INTO population (prefecture, population) VALUES
('Shiga-Ken', 1413000),
('Kyoto-Fu', 2610000),
('Osaka-Fu', 8830000),
('Hyogo-Ken', 5530000),
('Nara-Ken', 1364000),
('Wakayama-Ken', 944000),
('Tottori-Ken', 573000),
('Shimane-Ken', 694000),
('Okayama-Ken', 1909000),
('Hiroshima-Ken', 2847000),
('Yamaguchi-Ken', 1404000),
('Tokushima-Ken', 755000),
('Kagawa-Ken', 976000),
('Ehime-Ken', 1385000),
('Kochi-Ken', 728000),
('Fukuoka-Ken', 5104000),
('Saga-Ken', 832000),
('Nagasaki-Ken', 1378000),
('Kumamoto-Ken', 1786000),
('Oita-Ken', 1166000),
('Miyazaki-Ken', 1104000),
('Kagoshima-Ken', 1648000),
('Okinawa-Ken', 1434000);