var myArgs = process.argv.slice(2);
var LED3_PATH = "/sys/class/leds/beaglebone:green:usr3"

function writeLED(filename,value,path){
        var fs = require('fs');
        try{
                fs.writeFileSync(path+filename,value);
        }
        catch(err){
                console.log("The Write Failed to the File: " +path+filename);
        }
}
function removeTrigger(){
        writeLED("/trigger","none","LED3_PATH");
}
console.log("Starting the LED Node.js Program");
if (myArgs[0]==null) {
        console.log("There is an incorrect number of arguments.");
        console.log("  Usage is: nodejs nodjsLED.js command");
        console.log(" where command is one of: on, off, flash or status.");
        process.exit(2);
}
switch (myArgs[0]){
        case 'on':
                console.log("Turning the LED On");
                removeTrigger();
                writeLED("/brightness","1",LED3_PATH);
                break;
        case 'off':
                console.log("Turning the LED Off");
                removeTrigger();
                writeLED("/brightness","0",LED3_PATH);
                break;
        case 'flash':
                console.log("Making the LED Flash");
                writeLED("/trigger","timer",LED3_PATH);
                writeLED("/delay_on","50",LED3_PATH);
                writeLED("/delay_off","50",LED3_PATH);
                break;
        case 'status':
                console.log("Getting the LED Status");
                fs = require('fs');
                fs.readFile(LED3_PATH+"/trigger",'utf8',function(err,data) {
                        if(err) {
                                return console.log(err);
                        }
                        console.log(data);
                });
                break;
        default:
                console.log("Invalid Command");
}
console.log("End of Node.js Script");
console.log("Made by Sagar B Patel");



