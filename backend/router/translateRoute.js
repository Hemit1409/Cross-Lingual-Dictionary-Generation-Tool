const express = require("express")
const path = require('path')
const fs = require('fs')
const router= express.Router()
let {PythonShell} = require('python-shell')
// const translate = require('translate')
const utf8 = require('utf8');

// translateString = async (str , translateInfo) => {
//   translate.engine = 'libre'
//   const translated_string = await translate(str,translateInfo)
//   console.log('ts',translated_string)
// } 

router.route('/word').post(async(req,res)=>{

    var gujWord = req.body.gujWord
    var lvl = req.body.lvl

    console.log('gj',gujWord)
    // console.log(utf8.decode('àª¸à«àª¤à«'))
    // translateString('gujWord','gu')
    // let pyFile = path.join(__dirname,'../mainsrc/algorithm.py')
    // let options= {
    //   scriptPath:'E:\\Sem6\\gui3\\backend\\mainsrc',
    //   args:['gujWord',lvl]
    // }
    // var scriptPath = path.join(__dirname,'../mainsrc')

    try{
        PythonShell.run('E:\\Sem6\\gui3\\backend\\mainsrc\\algorithm.py',null,(e)=>{
          if(e) console.log('e',e)
          console.log('passed')
        })

        const content = gujWord+lvl
        fs.writeFileSync('E:\\Sem6\\gui3\\backend\\data\\ipWord.txt', content)

        let opFilePath = path.join(__dirname, '../data/opList.txt');
  
        // console.log('pathh',gujPath)

        var textHindi = fs.readFileSync(opFilePath,'utf-8')
        var opHindi = textHindi.split('\n')
        // console.log(textByLineGj)
        
        res.status(201).json(opHindi)

    }catch(e){
        console.log("error",e)
    }
})

// router.route('/word').post(async(req,res)=>{

//     var gujWord = req.body.gujWord
//     var lvl = req.body.lvl

//     // console.log('gj',gujWord)
//     var largeDataSet = []

//     // let pyFile = path.join(__dirname,'../mainsrc/algorithm.py')
//     let options= {
//       scriptPath:path.join(__dirname,'../mainsrc'),
//       args:[gujWord,lvl]
//     }
//     // console.log(gujWord,'and',lvl)
//     PythonShell.run('algorithm.py',options,(e,r)=>{
//       // console.log('r',r)
//       console.log('finished')
//     })

//   // let opFilePath = path.join(__dirname, '../data/opList.txt');

//   // // console.log('pathh',gujPath)
//   // try{
//   //     var textHindi = fs.readFileSync(opFilePath,'utf-8')
//   //     var opHindi = textHindi.split('\n')
//   //     // console.log(textByLineGj)

//   // }catch(e){
//   //     console.log("error",e)
//   // }
//   // res.status(201).json(opHindi)
// })

module.exports = router;
