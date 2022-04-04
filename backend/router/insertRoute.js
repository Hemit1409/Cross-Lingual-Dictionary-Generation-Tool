const express = require("express")
const router= express.Router()
const mysql = require("mysql")

var con = mysql.createConnection({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PSWD,
});

con.connect(function(err) {
    if(err){console.log(err)}
    console.log("Connected!");
});

router.route('/data').post(async(req,res)=>{
    try{
        const dbquery = 'CREATE DATABASE IF NOT EXISTS wordbank'

        con.query(dbquery,(e,r)=>{
            if(e) {console.log("error is: ",e)};
            console.log("WordBank database is created",r)
        })

        const dbq = "USE wordbank"

        // con.query(dbq,(e,r)=>{
        //     const dbquery1 = `CREATE TABLE wordInfo(
        //         gujword varchar(200),
        //         hindiword varchar(200)
        //     )`
            
        //     con.query(dbquery1,(e,r)=>{
        //         if(e) {console.log("error is: ",e)};
        //         console.log("wordInfo table is created",r)
        //     })
        //     if(e) {console.log("error is: ",e)};
        // })
        
        con.query(dbq,'INSERT INTO wordInfo (gujword,hindiword) values (?,?)',[req.body.gujWord,req.body.hindiWord],(e,resp)=>{
            if(!e){
                res.send("record has been inserted succesfully")
                console.log("Data inserted suucessfully")
            }else{
                throw e;
            }
        })

        res.json({message:"ok"})
    }catch(e){
        console.log('error ',e)
    }
})

module.exports = router; 