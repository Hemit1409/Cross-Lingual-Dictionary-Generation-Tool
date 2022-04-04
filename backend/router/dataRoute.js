const express = require("express")
const path = require('path')
const fs = require('fs')
const router= express.Router()

router.route('/gujdata').get(async(req,res)=>{
    let gujPath = path.join(__dirname, '../data/GujaratiOutput.txt');
    
    // console.log('pathh',gujPath)
    try{
        var textGj = fs.readFileSync(gujPath,'utf-8')
        var textByLineGj = textGj.split('\n')
        // console.log(textByLineGj)

    }catch(e){
        console.log("error",e)
    }
    res.status(201).json(textByLineGj)
})

router.route('/hindidata').get(async(req,res)=>{
    let opFilePath = path.join(__dirname, '../data/opList.txt');
  
    // console.log('pathh',gujPath)
    try{
        var textHindi = fs.readFileSync(opFilePath,'utf-8')
        var opHindi = textHindi.split('\n')
        // console.log(textByLineGj)
  
    }catch(e){
        console.log("error",e)
    }
    res.status(201).json(opHindi)
  })
  

module.exports = router;