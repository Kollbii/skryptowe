let timer = new Date();
let points = 0;
let out = document.getElementById('output');
function gameStart(){
    setInterval(generRandomElement, 2000)
}

window.onclick = e => {
    console.log(e.target);
    console.log(e.target.tagName);
    if (e.target.tagName == 'H1'){
        points += 1;
        out.textContent = points;
        e.target.remove()
    }else if (e.target.tagName == 'H2'){
        points += 2;
        out.textContent = points;
        e.target.remove()
        
    }else if (e.target.tagName == 'P'){
        points += 1;
        out.textContent = points;
        e.target.remove()

    }else if (e.target.tagName == 'TH'){
        curenVal = e.target.textContent;
        console.log(curenVal)
        points += parseInt(curenVal);
        out.textContent = points;
        e.target.remove();
    }else {
        points += -1;
        out.textContent = points;
    }
}

let ELEMS = ['h1','h2','p','table']

function generRandomElement(){
    let current = new Date();
    console.log(current - timer)
    if (current - timer >= 30000){
        return 0 ;
    }
    console.log('Creating element')
    let elem = ELEMS[Math.floor(Math.random()*ELEMS.length)];
    if (elem != 'table'){   
        let temp = document.createElement(elem);
        temp.textContent = "Element:" + elem;
        temp.style.display = "inline-block";
        temp.style.position = "absolute";
        temp.style.left = Math.floor(Math.random()*window.innerHeight).toString() + "px";
        temp.style.top = Math.floor(Math.random()*window.innerWidth).toString() + "px";
        document.body.appendChild(temp);
    }else {
        let temp = document.createElement(elem);
        for (let i =1 ; i< 5; i++){
            thh = document.createElement('th');
            thh.textContent = i;
            temp.appendChild(thh);
        }
        temp.style.display = "inline-block";
        temp.style.position = "absolute";
        temp.border = "1px solid black";
        temp.style.left = Math.floor(Math.random()*window.innerHeight - 100).toString() + "px";
        temp.style.top = Math.floor(Math.random()*window.innerWidth - 100).toString() + "px";
        document.body.appendChild(temp);   
    }
}

window.onload = function () {
    setTimeout(gameStart(), 30);
}

