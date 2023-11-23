CREATE TABLE IF NOT EXISTS prefectures (
    prefecture_id SERIAL PRIMARY KEY,
    prefecture_name VARCHAR(50),
    region VARCHAR(50)
);

-- Eastern Japan Prefectures
INSERT INTO prefectures (prefecture_name, region) VALUES ('Hokkaido', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Aomori-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Iwate-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Miyagi-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Akita-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Yamagata-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Fukushima-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Ibaraki-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Tochigi-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Gunma-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Saitama-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Chiba-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Tokyo-To', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Kanagawa-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Niigata-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Toyama-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Ishikawa-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Fukui-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Yamanashi-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Nagano-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Gifu-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Shizuoka-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Aichi-Ken', 'Eastern');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Mie-Ken', 'Eastern');

-- Western Japan Prefectures
INSERT INTO prefectures (prefecture_name, region) VALUES ('Shiga-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Kyoto-Fu', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Osaka-Fu', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Hyogo-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Nara-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Wakayama-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Tottori-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Shimane-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Okayama-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Hiroshima-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Yamaguchi-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Tokushima-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Kagawa-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Ehime-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Kochi-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Fukuoka-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Saga-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Nagasaki-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Kumamoto-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Oita-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Miyazaki-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Kagoshima-Ken', 'Western');
INSERT INTO prefectures (prefecture_name, region) VALUES ('Okinawa-Ken', 'Western');
