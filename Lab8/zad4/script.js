let ctr=0;
document.getElementById('submitBtn').onclick = function() {
    let myArr = new Array();
    console.log(myArr);
    let stg = document.getElementById('storageData').checked;
    
    if (stg == true){
        let data = document.getElementById('textData').value;
        data = data.split(';');
        console.log("SessionStorage/LocalStorage");
        window.localStorage.setItem(ctr, data);
        console.log(window.localStorage);
        ctr++;
    } else { 
        let data = document.getElementById('textData').value;
        data = data.split(';');
        console.log("Map/Set");
        myArr += myArr.push(data);
        console.log(myArr);
    }
}

// Tasks: Adding/ Removing grades, show all marks of student
// WebStorage checked -> Map/Set Unchecked: 
// niezalenie od wsyzsktiego ma byc arr