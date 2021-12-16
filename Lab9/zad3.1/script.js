// Video: https://www.youtube.com/watch?v=vLkPBj9ZaU0
class DecrementSpan extends HTMLElement{
    constructor(){
        super();
        this.shadowDOM = this.attachShadow({mode: 'open'});
    }

    connectedCallback() {
        this.render();
    }

    get value() {
        return this.getAttribute("value");
    }

    set value(val) {
        this.setAttribute("value", val);
    }

    static get observedAttributes() {
        return ["value"]
    }

    attributeChangedCallback(prop, oldVal, newVal) {
        if (prop == "value"){this.render()};
    }

    render(){
        this.shadowDOM.innerHTML = `<span>${this.value}</span>`
    }
}
customElements.define("decr-span", DecrementSpan)

function decrements(){
    let current = parseInt(document.getElementById('countdown').value);
    if (current <= 0) {return 0;}

    let spans = document.getElementsByTagName('decr-span');
    for (let i = 0; i < spans.length; i++){
        spans[i].setAttribute("value", current - 1);
    }
    document.getElementById('countdown').value = current - 1;
}

setInterval(decrements, 1000);