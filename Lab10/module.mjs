class Operation {
    /**
     * Constructor for Operation(x, y). Consists of value x and y.
     * @constructor
     */
    constructor(x, y){
        this.x = x;
        this.y = y;
    }

    sum() {
        return parseInt(this.x) + parseInt(this.y);
    }
}

export { Operation }