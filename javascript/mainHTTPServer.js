var http = require('http');
console.log('Starting server');
http.createServer(function (request, result) {
result.writeHead(200, {'Content-Type': 'text/plain'});
result.end('Hello World\n');
}).listen(9000, '127.0.0.1');
console.log('Server running at http://127.0.0.1:9000/');
