
const angleInclination = document.getElementById("angle");
const distanceTree = document.getElementById("distance");
const eyeHeight = document.getElementById("viewheight");
const resultBox = document.getElementById("Treeheight Result");

function calculate() {

    var angleFactor = Math.tan(Number(angleInclination.value) * Math.PI / 180);
    var heightOfTree = Number(eyeHeight.value) + (angleFactor * Number(distanceTree.value));

    // Test everything
    /*
    console.log(angleInclination.value)
    console.log(distanceTree.value)
    console.log(eyeHeight.value)
    console.log(angleFactor)
    console.log(heightOfTree)
    */

    resultBox.innerHTML = `The height of the tree is ${heightOfTree.toFixed(1)} metres`;

}

function clearInputs() {
    angleInclination.value = ''
    distanceTree.value = ''
    eyeHeight.value = ''
    resultBox.innerHTML = ''
}
