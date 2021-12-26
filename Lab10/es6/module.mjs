class Operation{
    constructor(x, y){
        this.x = x;
        this.y = y;
    }

    sum(){
        return parseInt(this.x) + parseInt(this.y);
    }
}

export { Operation }