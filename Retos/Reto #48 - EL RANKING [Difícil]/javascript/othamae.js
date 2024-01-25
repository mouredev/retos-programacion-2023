/*
 * Todo llega a su fin... Este es el último reto de programación 
 * semanal de 2023.
 *
 * Crea un programa que muestre un listado calculado en tiempo real
 * con todos los usuarios que han resuelto algún reto de programación
 * de este año.
 * - El listado debe estar ordenado por el número de ejercicios resueltos
 *   por cada usuario (y mostrar ese contador al lado de su nombre).
 * - También se debe de mostrar el número de usuarios que han participado
 *   y el número de correcciones enviadas.
 *
 * Muchísimas gracias por ayudar a crear este gran recurso
 * para la comunidad... ¡Prepárate para 2024!   
 */


async function contributors(repo) {
    try {
        let page= 1
        let totalContributions = 0
        let contributors = []
       while (true) {
            const response = await fetch(`https://api.github.com/repos/${repo}/contributors?per_page=100&page=${page}`)
            const data = await response.json()
            console.log('User:        Contributions')
            if (data.length === 0) {
                break
            }
            for (let i = 0;i < data.length;i++) {
                contributors.push({
                    user: data[i].login,
                    contributions: data[i].contributions,
                })
    
                console.log(data[i].login + ': ' + data[i].contributions)
                totalContributions += data[i].contributions
        }
       page++
       }
        const totalUsers = contributors.length
        console.log(`Total users: ${totalUsers}`)
        console.log(`Total contributions: ${totalContributions}`)

        return contributors
    } catch (error) {
        return console.log(error)
    }
 
}


const repo = 'mouredev/retos-programacion-2023'

contributors(repo)
