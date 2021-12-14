const iterations = 50;
const multiplier = 1000000000;

function calculatePrimes(iterations, multiplier) {
  var primes = [];
  for (var i = 0; i < iterations; i++) {
    var candidate = i * (multiplier * Math.random());
    var isPrime = true;
    for (var c = 2; c <= Math.sqrt(candidate); ++c) {
      if (candidate % c === 0) {
          // not prime
          isPrime = false;
          break;
       }
    }
    if (isPrime) {
      primes.push(candidate);
    }
  }
  return primes;
}

let SetIntervalTime = []
let SetTimeoutTime = []

let N = 10000;

let setIntId;
let setTimId;

document.getElementById('start').onclick = function () {
    let M = parseInt(document.getElementById('delay').value);
    setIntId = setInterval(doTimeConsumingCallculationsWithSetInterval, M);
    setTimId = setTimeout(doTimeConsumingCallculationsWithSetTimeout, M);
    requestAnimationFrame(drawChart);
}

document.getElementById('stop').onclick = function () {
    console.log('stop');
    clearInterval(setIntId);
    clearTimeout(setTimId);
}

function doTimeConsumingCallculationsWithSetInterval(){
    SetIntervalTime.push(performance.now());
    if (SetIntervalTime.length > N) {SetIntervalTime.shift();}
    calculatePrimes(1000, 100000000);
}

function doTimeConsumingCallculationsWithSetTimeout(){
    SetTimeoutTime.push(performance.now());
    if (SetTimeoutTime.length > N) {SetTimeoutTime.shift();}
    calculatePrimes(1000, 100000000);
    let M = parseInt(document.getElementById('delay').value);
    setTimId = setTimeout(doTimeConsumingCallculationsWithSetTimeout, M);
}

function drawChart(){
    let tmpInt = [];
    let tmpTim = [];
    for (let i = 1 ; i < SetIntervalTime.length; i++){
        tmpInt.push({x: i, y: SetIntervalTime[i] - SetIntervalTime[i - 1]});
    }
    for (let i = 1 ; i < SetTimeoutTime.length; i++){
        tmpTim.push({x: i, y: SetTimeoutTime[i] - SetTimeoutTime[i - 1]});
    }
    var chart = new CanvasJS.Chart("chartContainer",{
        title:{
        text: "Output time"
        },
        data: [
        {
            type: "line",
            dataPoints: tmpInt
        },
        {
            type: "line",
            dataPoints: tmpTim
        }
    ]
    });
    chart.render();
    requestAnimationFrame(drawChart);
}



