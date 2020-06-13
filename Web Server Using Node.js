var http = require('http');
var server = http.createServer(
        function(req,res) {
                res.writeHead(200,{'Content-Type': 'text/plain'});
                res.end('Hello from the BeagleBone Black\n');
                res.end('Sample Web Server using BeagleBone\n');
                res.end('Made by Sagar B Patel.........');
        });
server.listen(5050);

console.log('BBB Web Server running at http://192.168.7.2:5050/');
