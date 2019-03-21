const express = require('express')
var bodyParser = require('body-parser');
const path = require('path');
var fs = require('fs');
var http = require('http');
const { spawn, exec } = require('child_process');
const WebSocket = require('ws');

const app = express();
var server = http.createServer(app);
const port = process.env.PORT || 4000;

app.use(bodyParser.json()); // for parsing application/json

// Websockets
const wss = new WebSocket.Server({ server });
let client = undefined;
let hi = JSON.parse(fs.readFileSync('./json/hi_blue.json'));

wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
  });
  client = ws;
  client.send(JSON.stringify(hi));
});

// Endpoints
const scripts = ['vitality', 'temperature', 'customizable'];
let activeProcesses = [];

/**
 * Customize colors (i.e. customizeColorsRequest.json).
 */
app.post('/customize/colors', function (req, res) {
  if(client) {
      const body = JSON.stringify(req.body);
      // TODO : Validate array
      client.send(body);
  }
  res.send('OK');
});

/**
 * Check the server status.
 */
app.get('/status', function (req, res) {
  res.send('OK');
});

/**
 * Run the given script.
 */
app.get('/run/:script', function(req, res) {
  let search = scripts.find(script => script === req.params.script);
  if(search.length > 0) {
    activeProcesses.push(spawn("python", ["./py/" + req.params.script + ".py"]));
  }
  res.send('Running...');
});

/**
 * Stop active process.
 */
app.get('/stop', function(req, res) {
  if(activeProcesses.length > 0) {
    activeProcesses.forEach(activeProcess => activeProcess.kill('SIGINT'));
  }
  res.send('Stopping...');
});

/**
 * Sleep 2s before shutdown to let the server respond.
 */
app.get('/shutdown', function(req, res) {
  child = exec("sleep 2s && shutdown -h now");
  res.send('Shutdown...');
});

server.listen(port, function () {
  console.log('Pi Light listening on port ' + port + '!')
});
