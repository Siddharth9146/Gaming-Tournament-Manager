document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('findPlayer').addEventListener('submit', function(event){
        event.preventDefault();
        const username = document.getElementById('username').value;
        getPlayer(username);
    });
});


async function getPlayer(username){
    try{
        // Get player data
        const response = await fetch(`/findPlayer/${username}`);
        const data = await response.json();

        // Display player data in table
        var table = document.getElementById("playerdata");//empty table
      //display tournamentHistory and matchHistory from data
        var tournamentHistory = data.tournamentHistory;
        var matchHistory = data.matchHistory;
        var row = table.insertRow();
        var cell1 = row.insertCell();
        cell1.innerHTML = "Tournament History";
        var cell2 = row.insertCell();
        cell2.innerHTML = "Match History";
        for (var i = 0; i < tournamentHistory.length; i++) {
            var row = table.insertRow();
            var cell1 = row.insertCell();
            cell1.innerHTML = tournamentHistory[i];
            var cell2 = row.insertCell();
            cell2.innerHTML = matchHistory[i];
        }


}
    catch(error){
        console.log("Error in finding player");
    }
}