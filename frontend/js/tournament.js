async function getTournament(tournamentCode){
    try{
        // Get tournament data
        const response = await fetch(`/api/tournaments/${tournamentCode}`);
        const tournament = await response.json();
        
        // print table
        const table = document.querySelector('.table');
        table.innerHTML = '';
        tournament.players.forEach(player => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${player.name}</td>
                <td>${player.score}</td>
            `;
            table.appendChild(row);
        });

}
}