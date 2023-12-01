const  giveaway = (competitors) => {   
    let competitorsUpdated = [];
    competitorsUpdated = competitors;

    let action = parseInt(prompt("Selecciona que acción vas a realizar de entre la lista: \n 1. Añadir participante. \n 2. Borrar participante. \n 3. Mostrar participante. \n 4. Realizar sorteo. \n 5. Salir." ));

    if(action === 1){
        let newName = prompt("Inscríbete con tu nombre completo");
        
        if(competitorsUpdated.length === 0){
            competitorsUpdated.push(newName);
        } else {
            for(let i = 0 ; i < competitorsUpdated.length ; i++){
                    if(competitorsUpdated[i] === newName){
                            alert("Nombre ya registrado");
                            return giveaway(competitorsUpdated);                
                        };
                };
            competitorsUpdated.push(newName);
            };

        alert(newName + " ha sido inscrito correctamente.");
        
        return giveaway(competitorsUpdated);
    } else if (action === 2) { 
        
        if (competitorsUpdated.length === 0){
            alert("Todavía no existen participantes que eliminar.");
        } else if (competitorsUpdated.length > 0) {
            let deleteName = prompt("Escribe el nombre completo que quieras eliminar de entre quienes participan.");
            
            for(let i = 0 ; i < competitorsUpdated.length ; i++){
                if(competitorsUpdated[i] === deleteName){
                    competitorsUpdated.splice(i, 1);
                    alert(deleteName + " ya no esta participando en el sorteo.");
                } else {
                    alert("Ups, participante no encontrado");
                    };
                };
            };
        return giveaway(competitorsUpdated)

    } else if (action === 3) {
        if(competitorsUpdated.length === 0){
            alert("Todavía no hay participantes");
        } else {
                alert("Participantes en el sorteo. \n" + competitorsUpdated);
        };

        return giveaway(competitorsUpdated);
    } else if (action === 4) { 
        let random = Math.floor((Math.random() * (competitorsUpdated.length)));
        let winner = competitorsUpdated[random];

        competitorsUpdated.splice(random, 1);

        alert(winner + " won the price.");
        giveaway(competitorsUpdated);
        };
    };
            
    let competitors = ["w","a","s","d"];
    // let competitors = [];
    
    giveaway(competitors);