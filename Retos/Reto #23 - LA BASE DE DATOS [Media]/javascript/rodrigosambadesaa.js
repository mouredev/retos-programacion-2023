'use strict';

const CONFIG = {
  host: 'mysql-5707.dinaserver.com',
  port: 3306,
  user: 'mouredev_read',
  password: 'mouredev_pass',
  database: 'moure_test'
};

async function queryChallenges(connection) {
  const [rows] = await connection.execute('SELECT * FROM `challenges`');
  return rows;
}

async function connectAndQuery() {
  const mysql = require('mysql2/promise');
  const connection = await mysql.createConnection(CONFIG);
  try {
    return await queryChallenges(connection);
  } finally {
    await connection.end();
  }
}

module.exports = { CONFIG, queryChallenges, connectAndQuery };

if (require.main === module) connectAndQuery().then(console.table).catch(console.error);
