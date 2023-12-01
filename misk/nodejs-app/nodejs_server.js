const express = require('express');
const app = express();
const port = 3000;

app.get('/', async (req, res) => {
    res.send('Hello, NodeJS App!');
});

// サーバーの起動
app.listen(port, () => {
    console.log(`Server running on port ${port}`);
});