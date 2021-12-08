window.onload = function(){
    console.log('Tekst 1');
    window.alert('Tekst 2')
}

document.getElementById('btnClick').onclick = function() {
    let vars = document.forms[0].elements;
    document.getElementById('output').innerHTML = "<b>Input1:</b> " + vars[0].value + "<br><b>Input2:</b> " + vars[1].value;
    console.log(typeof(vars[0].value))
    console.log(typeof(vars[1].value))
    // Zawsze zwraca string
}

// console.log(typeof(window.prompt("Podaj wartość 1","PlaceholderDlaWartości"))); //1,2,3 -> string | 4 -> object
