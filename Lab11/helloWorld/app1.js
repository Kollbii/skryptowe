// No use of any template system
var express = require('express'),
    logger = require('morgan');
const path = require('path');
var fs = require('fs')
var app = express();
var x = 1;
var y = 9;

const mongoose = require('mongoose');
const { Schema } = mongoose;
mongoose.connect('mongodb://localhost:12312/lab');
const Table = new Schema({
    o: String,
    x: Number,
    y: Number
});
const Tb = mongoose.model('Tb', Table);

function sum(x, y){return x + y};

// Determining the contents of the middleware stack
app.use(logger('dev'));                         // Place an HTTP request recorder on the stack — each request will be logged in the console in 'dev' format
// app.use(express.static(__dirname + '/public')); // Place the built-in middleware 'express.static' — static content (files .css, .js, .jpg, etc.) will be provided from the 'public' directory

// Route definitions
app.get('/', function (req, res) {     // The first route
    res.send(`<h1>Summing numbers hardcoded inside!</h1><p> ${x} + ${y} = ${sum(x, y)}</p>`);
});

app.get('/json/:name', (req, res) => {
    let data = JSON.parse(fs.readFileSync(req.params.name + '.json'));
    
    repr = '';
    repr += `<table>
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

app.get('/calculate/:operation/:x/:y',  (req, res) =>{
    // IN URL WRITE %2F FOR '/' SIGN
    if (['+', '-', '*', '/'].includes(req.params.operation)){
        let tmp = new Tb({o: req.params.operation, x: req.params.x, y: req.params.y});
        tmp.save();
        repr = `${req.params.x} ${req.params.operation} ${req.params.y} = ${eval(req.params.x + req.params.operation + req.params.y)}`;
        res.send(repr);
    } else {
        throw Error("Invalid operation");
    }
});


// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});

// To run: npm run app1