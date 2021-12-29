//Source:  https://codeforgeek.com/unit-testing-nodejs-application-using-mocha/
var supertest = require("supertest");

// This agent refers to PORT where program is runninng.
var server = supertest.agent("http://localhost:8080");

// UNIT test begin
describe('GET /submit?name=John', function () {
      it('Respond with error. Could not find file/dir.', function (done) {
            server
                  .get('/submit?name=John')
                  .expect('Content-Type', /text\/plain/)
                  .expect(200, "Could not find this file/dir. Optionally got error.", done);
      });
});

describe('GET /submit?name=testDir', function (){
    it('Respond with "It is a directory."', function (done){
        server
            .get('/submit?name=testDir')
            .expect('Content-Type', /text\/plain/)
            .expect(200, "It is a directory.", done);    
    });
});

describe('GET /submit?name=testFile.txt', function (){
    it('Respond with "It is a file" msg and contnt.', function (done){
        server
            .get('/submit?name=testFile.txt')
            .expect('Content-Type', /text\/plain/)
            .expect(200,    'It is a file name. File content:\n' +
            'Some values in here\r\n' +
            'Line1\r\n' +
            'int main(void){\r\n' +
            '    printf("some code in here for %d times", 34);\r\n' +
            '}\r\n', done);    
    });
});