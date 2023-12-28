const fs = require('fs');

const prompt = require("prompt-sync")();

let text = "";

let exist = false;
let input = "";
let path = "/home/raul/Documentos/text_file.txt";

if (fs.existsSync(path)) {
    exist = true

}

if (exist) {

    console.log("File already exist, which action you would like to perform");
    console.log("Enter A for append at the en of the file ");
    console.log("Enter D for deleting the file");

    input = prompt()
    input = input.toUpperCase();

    if (input == 'D') {
        try {
            fs.unlink(path, (error) => {
                if (error) {
                    throw err;
                }
            })
        } catch (err) {
            console.log("error deleting the file");
        }
        finally{
            console.log("File deleted");
        }
    }
}


try {

    console.log("Adding data to the file press END to finish");

    do{
        input = prompt()

        if(input != "END"){
            text = text + input +"\n" ;
        }
    }while(input !="END")

   fs.appendFile(path, text, (err) => {

        if (err) {
            throw err;
        }


    })

} catch (err) {

    console.log("There is an error:  " + err.text)


}

