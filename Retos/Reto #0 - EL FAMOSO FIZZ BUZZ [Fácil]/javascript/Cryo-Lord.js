//const prompt = require("prompt-sync")({sigint: true});
function first_loop() 
{
    console.log("---- Starting printing ----")
    var text = "";
    for (let i = 1; i < 101; i++) 
        {
            if (!(i % 3))
                {
                    text += "fizz"
                }
            if (!(i % 5))
                {
                    text += "buzz"
                }
            if (text != "")
                {
                    console.log("----  "+ i + " " + text +"  ----")
                }    
            else 
                {
                    console.log("----    "+ i + "    ----")
                }
            text = "";
        }
};
first_loop();