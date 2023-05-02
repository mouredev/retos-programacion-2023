const https = require('https');


function get_data() {

    let data = [];
    //Set request options
    let options = {
      headers : {
        "User-Agent":"raulg91"
      }
    };

    const req = https.get( "https://api.github.com/repos/mouredev/retos-programacion-2023/commits",options,(res)=>{
        res.on('data', (chunk) => {
            data.push(chunk);
          });

        res.on('end',()=>{
            const commits = JSON.parse(Buffer.concat(data).toString());

            for(let i=0;i<10;i++){
                let message = commits[i].commit.message;
                message = message.toString().replace(/\n/g,"");
                let date = new Date(commits[i].commit.author.date);
                let date_string = `${date.getDate()}/${date.getMonth()+1}/${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}`;
                console.log(`Commit ${i+1} | ${commits[i].sha} | ${commits[i].commit.author.name} | ${message} | ${date_string}`);
            }

        });
     
      

    }).on("error",(error)=>{
      console.log("Error: " + error.message);
    })

    req.end();

}

get_data();