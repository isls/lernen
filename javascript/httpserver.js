var http = require('http')
var server = http.createServer(function(request, response) {
  response.writeHead(200, {'Content-Type': 'text/html'});
  response.write('<!DOCTYPE "html">');
  response.write('<html>');
  response.write('<head>');
  response.write('<title>Lauri\'s Seite</title>');
  response.write('</head>');
  response.write('<body>');
  response.write('Hallo lieber Lauri, wie geht es dir?');
  response.write('</body>');
  response.write('</html>');
  response.end();
});

server.listen(8080);
console.log('Server ist gestartet.');
