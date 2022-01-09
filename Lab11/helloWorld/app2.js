// Application using the 'Pug' template system
var express = require('express'),
    logger = require('morgan');
var fs = require('fs');
var app = express();
var x = 1;
var y = 5;

function sum(x, y){return x + y};

// Configuring the application
app.set('views', __dirname + '\\views\\'); // Files with views can be found in the 'views' directory
app.set('view engine', 'pug');          // Use the 'Pug' template system

// Determining the contents of the middleware stack
app.use(logger('dev'));                         // Add an HTTP request recorder to the stack — every request will be logged in the console in the 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// Route definitions
app.get('/', function (req, res) {      // The first route
    res.send(`<h1>Summing numbers hardcoded inside!</h1><p> ${x} + ${y} = ${sum(x, y)}</p>`);
});

app.get('/json/:name', (req, res) => {
    let data = JSON.parse(fs.readFileSync(req.params.name + '.json'));
    
    repr = '';
    repr += `
    <table class='table'>
    <tr>
        <th>x</th>
        <th>Operation</th>
        <th>y</th>
        <th>Result</th>
    </tr>
    `
    data.forEach(element => {
        repr += '<tr>'
        repr += `<td>${element.x}</td>`;
        repr += `<td>${element.o}</td>`;
        repr += `<td>${element.y}</td>`;
        result = eval(element.x + element.o + element.y); // Make operation happen
        repr += `<td>${result}</td>`;
        repr += "</tr>";
    });
    repr += `</table>`
    res.send(`<h1>${repr}</h1>`);
});
// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});

// To run: npm run app2