// get tournament code and name from tournament_login.html and send to api '/checkTournamentCode/{tournamentCode}/{tournamentName}'
// if tournament code and name are correct, redirect to match_creation.html
// if not, show error message

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('tournament_login').addEventListener('submit', function(event){
        event.preventDefault();
        const tournamentCode = document.getElementById('tournamentCode').value;
        const tournamentName = document.getElementById('tournamentName').value;
        checkTournamentCode(tournamentCode, tournamentName);

    }); 
}
);

async function checkTournamentCode(tournamentCode, tournamentName){
    try{
        // Get player data
        const response = await fetch(`/checkTournamentCode/${tournamentCode}/${tournamentName}`);
        const data = await response.json();
        if (data.success){
            window.location.href = "/match_creation.html";
        }
        else{
            document.getElementById("error").innerHTML = "Invalid tournament code or name";
        }
    }
    catch(error){
        console.log("Error in finding tournament");
    }
}
        