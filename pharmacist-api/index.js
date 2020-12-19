const serverless = require('serverless-http');
const express = require('express');
const app = express();
const pGenerator = require('./pharmacist-generator.js')

app.get('/', function (req, res) {
    res.send(pGenerator.generate());
})

module.exports.handler = serverless(app);