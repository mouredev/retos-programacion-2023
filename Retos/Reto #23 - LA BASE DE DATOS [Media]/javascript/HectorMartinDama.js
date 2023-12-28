const mysql= require('mysql');

const connection= mysql.createConnection({
    host: 'mysql-5707.dinaserver.com',
    port: '3306',
    user: 'mouredev_read',
    password: 'mouredev_pass',
    database: 'moure_test'
});

connection.connect();

connection.query('SELECT * FROM challenges', (error, rows) =>{
    if (error) throw error;
    let results = Object.values(JSON.parse(JSON.stringify(rows)));
    results.forEach(challenge => {console.log(challenge.id, challenge.name, challenge.difficulty, challenge.date)});
});

connection.end();