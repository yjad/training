 function compareDates() {
    var name = prompt("Enter your name:", "John");
    if (name === null || name === "") {
        document.getElementById("msg").innerHTML = "Please enter your name.";
    } else {
        document.getElementById("msg").innerHTML = "You entered: " + name;
}

  
    // const FROM = document.getElementById("from").value;
    // const TO = document.getElementById("to").value;
    // console.log(FROM);
    // console.log(TO);

    // if (FROM > TO){
    //     console.log("Invalidate from/to dates");
    //     windows.alert("Invalidate from/to dates");
    // }else{
    //     console.log("Validate from/to dates");
    // }
    // return FROM < TO;
 }