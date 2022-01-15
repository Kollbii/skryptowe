let http = require("http");
let fs = require("fs");
let url = require('url');
let { parse } = require('querystring');
const file = 'form.html';

http.createServer(function (request, response) {
  console.log("--------------------------------------");
  console.log("The relative URL of the current request: " + request.url + "\n");
  url_params = url.parse(request.url, true);
  switch (url_params.pathname) {
    case '/':
      fs.stat(file, function (err, stats) {
        if (err == null) { // If the file exists
          fs.readFile(file, function (err, data) { // Read it content
            response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
            response.write(data);   // Send the content to the web browser
            response.end();
          });
        }
        else { // If the file does not exists
          response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
          response.write(`The '${file}'file does not exist`);
          response.end();
        } //else
      }); //fs.stat
      break;

    case '/submit':
      var welcomeText = `Witaj ${url_params.query.imie}`;
      console.log(`Witaj ${url_params.query.imie}`);
      if (typeof welcomeText !== 'undefined') {
        response.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
        response.write(welcomeText); // Data (response) that we want to send to the web browser
        response.end(); // Sending the response
        console.log("The server sent the '" + welcomeText + "' text to the browser");
        break;
      }
    
    case '/post':
      let body = '';
      request.on('data', (chunk) => {
        body += chunk.toString();
      });
      request.on('end', () => {
        body = parse(body);
        response.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
        let welcomeText = `Witaj  ${body.imie}`;
        response.write(welcomeText);
        response.end();
        console.log("The server sent the '" + welcomeText + "' text to the browser");
      });

  } //switch
}).listen(8080);
console.log("The server was started on port 8080");
console.log("To stop the server, press 'CTRL + C'");