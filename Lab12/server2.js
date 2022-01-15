let url = require('url');
let fs = require('fs');
const remote = 'remote.html';
const local = 'local.html';

function onRequest_8080(request, response) {
    console.log("The relative URL of the current request [8080]: " + request.url + "\n");
    url_parm = url.parse(request.url, true);
    switch (url_parm.pathname){
        case '/':
            fs.stat(remote, (err, stats) => {
                if (err == null){
                    fs.readFile(remote, (err, data) => {
                        response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
                        response.write(data);
                        response.end();
                    })
                } else {
                    response.writeHead(200, {"Content-Type": "text/plain"})
                    response.write(`Problem with finding ${remote} file.`);
                    response.end();
                }
            });
        break;
    }
}

function onRequest_8081(request, response) {
    console.log("The relative URL of the current request [8081]: " + request.url + "\n");
    url_parm = url.parse(request.url, true);
    switch (url_parm.pathname){
        case '/':
            fs.stat(local, (err, stats) => {
                if (err == null){
                    fs.readFile(local, (err, data) => {
                        response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
                        response.write(data);
                        response.end();
                    })
                } else {
                    response.writeHead(200, {"Content-Type": "text/plain"})
                    response.write(`Problem with finding ${local} file.`);
                    response.end();
                }
            });
        break;
    }
}
  
/* ************************************************** */
/* Main block
/* ************************************************** */
var http = require('http');

http.createServer(onRequest_8080).listen(8080);
http.createServer(onRequest_8081).listen(8081);
console.log("The server was started on port 8080 and 8081");
console.log("To stop the server, press 'CTRL + C'");