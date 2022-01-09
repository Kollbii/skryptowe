const http = require('http');
const fs = require('fs');
const path = require('path');

async function writeDataFromFile(res, abs_path){
    console.log(abs_path);

    fs.stat(abs_path, (err, stats) => {
        if (err){
            res.write('Could not find this file/dir. Optionally got error.');
            res.end();
        } else if (stats.isFile()){
            fs.readFile(abs_path, (err, data) => {
                if (err) throw err;
                console.log('Reading file.', data);
                res.write("It is a file name. File content:\n" + data);
                res.end();
            });
        } else if (stats.isDirectory()){
            res.write('It is a directory.');
            res.end();
        }
    });
}

http.createServer((req, res) => {
    let url = new URL(req.url, `http://${req.headers.host}`); // Create the URL object
    if (url.pathname == '/submit') {
        console.log(url);
        let name_search = url.searchParams.get('name');
        console.log("Searching for " + name_search);

        console.log("Creating a response header");
        res.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
        console.log("Creating a response body");

        if (req.method == 'GET'){
            writeDataFromFile(res, path.resolve(name_search));
        }else{
            res.write(`This application does not support the ${req.method} method`);
            console.log("Sending the response");
            res.end();
        }
    }
    else {
        console.log("Creating a response header")
        res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
        console.log("Creating a response body");
        res.write(`<form method="GET" action="/submit">
                            <label for="name">Name of file or directory</label>
                            <input name="name">
                            <br>
                            <input type="submit">
                            <input type="reset">
                        </form>`);
        console.log("Sending the response");
        res.end();
    }
}).listen(8080)