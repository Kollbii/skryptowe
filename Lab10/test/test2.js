var assert = require('assert');
var { isDir } = require('../zad2/module_zad2');
var path = require('path');

/** This won't work. */
let testDir = '..\\zad2\\testDir';
let testFile = '..\\zad2\\testFile.txt';

/** If you want to pass paths as args it is needed to be absolute. */
let dirAbs = path.resolve('zad2', 'testDir');
let fileAbs = path.resolve('zad2', 'testFile.txt');

describe('The isDir() method', function () {
  it('Inform it is directory', function () {
    assert.strictEqual(isDir(dirAbs), 'dir')
  });
  it('Inform it is a file', function () {
    assert.strictEqual(isDir(fileAbs), 'file')
  });
  it('Call non existing file/directory', function () {
    assert.strictEqual(isDir('C:\\WINDOWS\\Some\\random\\path.txt'), 'error')
  });
});

// To call:
// npx mocha