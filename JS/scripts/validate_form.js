const form = document.querySelector("form");
const form_title = document.getElementsByClassName('panel-title')[0].innerHTML;
console.log("form title: "+form_title);

    form.addEventListener("submit", (event) => {
        console.log("submit ....");
        if (!validateForm(form_title)){
            event.preventDefault(); // stop the form processing
        }
        event.preventDefault(); // stop the form processing
    });
    
// }

function compareDates(FROM, TO) {
    console.log("from CompareDates...");
    if (FROM > TO) {
        document.getElementById('message').innerHTML="Error Date Range";
    }else{
        document.getElementById('message').innerHTML = "Valid Date Range";
    }
    return (FROM > TO);
}

function showError() {
    const from_dateError = document.querySelector("#from_date + span.error");
    
    // console.log("from showError ...");
    from_dateError.textContent = "Error Date Range"
    // Set the styling appropriately
    from_dateError.className = "error active";
}


function validateForm(form_title) {
    switch(forn_title) {
        case "Add Courses Per Cycle":
            let FROM = document.forms["myForm"]["from_date"].value;
            let TO = document.forms["myForm"]["to_date"].value;
            if (compareDates(FROM, TO)){
                showError()
                return false;       // stop sending the form
            } else {
                return true;        // validation OK
            }
            break;
        // case y:
            // code block
            // break;
        // default:
            // code block
    }
    
}
  
