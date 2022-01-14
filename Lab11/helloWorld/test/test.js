//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");
var chai = require('chai');
const { assert } = require("chai");
chai.use(require('chai-json'))

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:3000");

// UNIT test begin
describe('GET /', function() {
      it('respond with html', function(done) {
         server
         .get('/')
         .expect('Content-Type', /html/)
         .expect(200, done);
      });
});

describe('GET /', function() {
    it('First test', function(done) {
       server
       .get('/')
       .expect('Content-Type', /html/)
       .expect(200, done);
    });
});

describe('Check GET /json/ex', function(){
   it('Response', function(done){
      server.get('/json/ex').expect('Content-Type', /html/).expect(200, done);
   });

   it('Check /json/ex route content', function(done){
      server.get('/json/ex')
      .expect('Content-Type', /html/)
      .expect(async (res) => {
         chai.expect(res.text, `<table class='table' border="solid 1px black">
         <tr>
             <th width="60px">x</th>
             <th width="60px">Operation</th>
             <th width="60px">y</th>
             <th width="60px">Result</th>
         </tr>
         <tr><td text-align="center">2</td><td text-align="center">+</td><td text-align="center">6</td><td 
     text-align="center">8</td></tr><tr><td text-align="center">1</td><td text-align="center">-</td><td text-align="center">500</td><td text-align="center">-499</td></tr><tr><td text-align="center">4</td><td text-align="center">*</td><td text-align="center">4</td><td text-align="center">16</td></tr><tr><td text-align="center">81</td><td text-align="center">/</td><td text-align="center">9</td><td text-align="center">9</td></tr></table>`).end(done);
      }).end(done);
   });
});

describe('Check basic add operation', function(){
   it('Check / route content', function(done){
      server.get('/')
      .expect('Content-Type', /html/)
      .expect(async (res) => {
         chai.expect(res.text, '<h1>Summing numbers hardcoded inside!</h1><p> 1 + 5 = 6</p>').end(done);
      }).end(done);
   });
});

describe('Check JSON file', function() {
   it('Propper JSON', function(done) {
      // Absolute path(?)
      chai.expect('.\\ex.json').to.be.a.jsonFile();
      chai.expect('.\\package.json').to.be.a.jsonFile();
      done()
   });
   
});

describe('Check values in JSON file', function(){
   it('Contains propper value', function(done){
      chai.expect('.\\ex.json').contain.jsonWithProps({
         "o": "+",
         "x": 2,
         "y": 6
      })
      chai.expect('.\\ex.json').contain.jsonWithProps({
         "o": "/",
         "x": 81,
         "y": 9
      })
      done()
   });
});

describe('Check if calculate/operation/x/y correct', function(){
   it('GET route', function(done){
      server
       .get('/')
       .expect('Content-Type', /html/)
       .expect(200, done);
   });
   it('Get Calculate/-/67/76', function(done){
      server
      .get('/calculate/-/67/76')
      .expect('Content-Type', /html/)
      .expect((res)=>{
         console.log(res.text);
         chai.expect(res.text, `<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"><title>Your first page</title></head><body><h1>Page!</h1><p>1 + 5 = 6</p><script 
         src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"></script></body></html>`)
      });
      done();
   });
});