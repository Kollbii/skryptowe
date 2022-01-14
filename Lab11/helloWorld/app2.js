// Application using the 'Pug' template system
var express = require('express'),
    logger = require('morgan');
var fs = require('fs');
var app = express();


const mongoose = require('mongoose');
const { Schema } = mongoose;
mongoose.connect('mongodb://localhost:12312/lab');
const Table = new Schema({
    o: String,
    x: Number,
    y: Number
});
const Equation = mongoose.model('Equation', Table);

var x = 1;
var y = 5;

function sum(x, y){return x + y};

// Configuring the application
app.set('views', __dirname + '\\views\\');
app.set('view engine', 'pug');

// Determining the contents of the middleware stack
app.use(logger('dev'));

// Route definitions
app.get('/', function (req, res) {
    res.render('index', {sum: `${x} + ${y} = ${sum(x, y)}`});
});

app.get('/json/:name', (req, res) => {
    res.render('index', {represent_table: JSON.parse(fs.readFileSync(req.params.name + '.json'))});
});

app.get('/calculate/:operation/:x/:y',  (req, res) =>{
    // IN URL WRITE %2F FOR '/' SIGN
    if (['+', '-', '*', '/'].includes(req.params.operation)){
        let tmp = new Equation({o: req.params.operation, x: req.params.x, y: req.params.y});
        console.log(tmp);
        tmp.save();
        repr = `${req.params.x} ${req.params.operation} ${req.params.y} = ${eval(req.params.x + req.params.operation + req.params.y)}`;
        res.render('index', {sum: repr});
    } else {
        throw Error("Invalid operation");
    }
});

app.get('/results', (req, res) => {
    let data = Equation.find(); // Get everything
    console.log(data);
    res.render('index', {represent_table: data});
});

// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});

// To run: npm run app2