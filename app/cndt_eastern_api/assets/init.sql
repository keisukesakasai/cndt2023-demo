CREATE DATABASE IF NOT EXISTS eastern;
USE eastern;

CREATE TABLE IF NOT EXISTS population (
    prefecture_id INT AUTO_INCREMENT PRIMARY KEY,
    prefecture VARCHAR(255),
    population INT
);

INSERT INTO population (prefecture, population) VALUES
('Hokkaido', 5210000),
('Aomori-Ken', 1270000),
('Iwate-Ken', 1250000),
('Miyagi-Ken', 2320000),
('Akita-Ken', 966000),
('Yamagata-Ken', 1095000),
('Fukushima-Ken', 1846000),
('Ibaraki-Ken', 2860000),
('Tochigi-Ken', 1940000),
('Gunma-Ken', 1940000),
('Saitama-Ken', 7190000),
('Chiba-Ken', 6210000),
('Tokyo-To', 13500000),
('Kanagawa-Ken', 9040000),
('Niigata-Ken', 2220000),
('Toyama-Ken', 1044000),
('Ishikawa-Ken', 1137000),
('Fukui-Ken', 771000),
('Yamanashi-Ken', 812000),
('Nagano-Ken', 2050000),
('Gifu-Ken', 2000000),
('Shizuoka-Ken', 705000),
('Aichi-Ken', 7553000),
('Mie-Ken', 1800000);