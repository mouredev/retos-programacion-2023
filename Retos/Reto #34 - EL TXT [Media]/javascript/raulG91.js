const fs = require('fs');

const prompt = require("prompt-sync")(); 

let text = "This is a new line";

let exist = false;
let input ="";


if(fs.existsSync("C:\\Users\\RaulGarciaPedrosa\\test_file.txt")){
    exist = true

}

if(exist){

    console.log("File already exist, which action you would like to perform");
    console.log("Enter A for append at the en of the file " + "\n " + " Enter D for deleting the file");
    input = prompt()
    input = input.toUpperCase();

    if(input == 'D'){

        fs.unlink("C:\\Users\\RaulGarciaPedrosa\\test_file.txt")
    }
}

try{
    fs.writeFile("C:\\Users\\RaulGarciaPedrosa\\test_file.txt",text,(err)=>{

        if(err){
            throw err;
        } 
    
    
    } )

}catch(err){

    console.log("There is an error:  " + err.text)


}

fs.readFile