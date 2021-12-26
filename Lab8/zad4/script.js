// Tasks: Adding/ Removing grades, show all marks of student

let ctr=1;
let out = document.getElementById('output');

function add(data){
    console.log(window.localStorage);
    window.localStorage.setItem(ctr, [data[1],data[2],data[3]]);
    out.innerHTML = 'Added user: name=' + data[1] + ',surname=' + data[2]+ ',grade='+data[3];
    ctr++;
}

function remove(data){
    window.localStorage.removeItem(data[1]);
    out.innerHTML = 'Removed user with id' + data[1];
}

function change(data){
    current = window.localStorage.getItem(data[1])
    window.localStorage.setItem(data[1],[current[0],current[1], data[2]])
    out.innerHTML = 'Succesfully updated grade for ' + current[0] + " " + current[1]
}

function show(data){
    if (data[1] == 'all'){
        out.innerHTML = '';
        for (let i = 0; i < parseInt(window.localStorage.length); i++){
            console.log(window.localStorage.getItem(i));
            item = window.localStorage.getItem(i);
                out.innerHTML += item + '<br>';
        }
        out.innerHTML = window.localStorage.getItem(data[1])
    } else {
        if (window.localStorage.getItem(data[1]) == null){
            out.innerHTML = 'User does not exists'
        }else {
            out.innerHTML = window.localStorage.getItem(data[1])
        }
    }  
}

document.getElementById('submitBtn').onclick = function() {
    let stg = document.getElementById('storageData').checked;
    if (stg == true){
        let data = document.getElementById('textData').value;
        data = data.split(';');
        if (data[0] == 'add'){
            add(data);
        }
        if (data[0] == 'remove'){
            remove(data);
        }
        if (data[0] == 'change'){
            change(data);
        }
        if (data[0] == 'show'){
            show(data);
        }
    }
}


// describe('Testing window.localStorage', function(){
//     it('adding user', function(){
//         expect(numbers('')).to.equal(0);
//     })
//     it('Blank for chars()', function(){
//         expect(chars('')).to.equal(0);
//     })
//     it('Blank for sum()', function(){
//         expect(sum('')).to.equal(0);
//     })
// })