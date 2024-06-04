// // get tournament code and name from tournament_login.html and send to api '/checkTournamentCode/{tournamentCode}/{tournamentName}'
// // if tournament code and name are correct, redirect to match_creation.html
// // if not, show error message

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('tournament_login').addEventListener('submit', function(event){
        event.preventDefault();
        const tournamentCode = document.getElementById('tournament_code').value;
        const tournamentName = document.getElementById('tournament_name').value;
        checkTournamentCode(tournamentCode, tournamentName);

    }); 
}
);

// async function checkTournamentCode(tournamentCode, tournamentName){
//     try{
//         // Get player data
//         const response = await fetch(`/checkTournamentCode/${tournamentCode}/${tournamentName}`);
//         const data = await response.json();
//         if (data.success){
//             window.location.href = "/match_creation.html";
//         }
//         else{
//             document.getElementById("error").innerHTML = "Invalid tournament code or name";
//         }
//     }
//     catch(error){
//         console.log("Error in finding tournament");
//     }
// }
        
function submitForm(e) {
    e.preventDefault();
   
   var myform =    document.getElementById("myform");
    
    var formData = new FormData(myform);
  
    fetch("https://show.ratufa.io/json", {
      method: "POST",
      body: formData,
    })
      .then(response => {
      if (!response.ok) {
        throw new Error('network returns error');
      }
      return response.json();
    })
      .then((resp) => {
        let respdiv = document.createElement("pre");
        respdiv.innerHTML = JSON.stringify(resp, null, 2);
        myform.replaceWith(respdiv);
        console.log("resp from server ", resp);
      })
      .catch((error) => {
        // Handle error
        console.log("error ", error);
      });
  }
  
  var myform = document.getElementById("myform");
  
  myform.addEventListener("submit", submitForm);