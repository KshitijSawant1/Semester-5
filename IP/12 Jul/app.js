var express = require ("express"); // npm i express
var app = express();

app.get("/home",(req,res)=>{
    res.send("hello World")
})
app.get("/sqr",(req,res)=>{
    console.log(res,query.num);
    res.send("hello World")
})
app.listen(8989,() =>{
console.log("Listening on port ")
})