const express = require('express');
const { Pool } = require('pg');
const app = express();
const port = 3000;

// PostgreSQLへの接続設定
const pool = new Pool({
    host: '127.0.0.1',
    user: 'postgres',
    password: 'password',
    database: 'postgres',
    port: 5432
});    

app.get('/', async (req, res) => {
    try {
        const client = await pool.connect();
        const queryText = 'SELECT region FROM prefectures WHERE prefecture_name = $1';
        const values = ['Chiba-Ken'];
        const result = await client.query(queryText, values);
        res.send(result.rows);
        client.release();
    } catch (err) {
        console.error(err);
        res.send("Error " + err);
    }
    });

// サーバーの起動
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});
