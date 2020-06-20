#!/usr/bin/env node
"use strict";
var port = 9090,
        http = require('http'),
        url=require('url'),
        fs=require('fs'),
        b=require('bonescript'),
        gpio = 'P9_42';

var htmlStart = "\
<!DOCTYPE html>\
<html>\
<body>\
\
<h1>" + gpio + " </h1>\
data = ";

var htmlEnd = "\
</body>\
<html>";

var server = http.createServer(servePage);
b.pinMode(gpio,b.INPUT,7,'pullup');

server.listen(port);
console.log("Created by Sagar B Patel.....");
console.log("Listening on "+port);

function servePage(req,res)
{
        var path=url.parse(req.url).pathname;
        console.log("path: "+path);
        if(path =='/gpio')
        {
                var data = b.digitalRead(gpio);
                if(data=='0')
                {
                        data = '1';
           }
                else 
                {
                        data='0';
                }
                res.write(htmlStart+data+htmlEnd,'utf8');
                res.end();
        }
        else
        {
                fs.readFile(__dirname+path,function(err,data){
                        if(err){
                                return send404(res);
                        }
                        res.write(data,'utf8');
                        res.end();
                });
        }
}

function send404(res)
{
        res.writeHead(404);
        res.write('404 - page not found....');
        res.end();
}

