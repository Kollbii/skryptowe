const fs = require('fs');

exports.isDir = (name) => {
    /**Throws error if unexpected name is given */
    try {
        let file = fs.lstatSync(name)
        if (file.isDirectory()){
            console.log('Given path is directory.');
            return 'dir';
        }
        if (file.isFile()){
            console.log('Given path is file.')
            try {        
                data = fs.readFileSync(name, 'utf8')
                console.log(data)
            } catch (err){console.log(err); return 'error'}
            return 'file';
        } else {
            return 'error';
        }
    } catch (err){console.log(err); return 'error'}
}