require('dotenv').config()
const express = require('express')
const dataRoute = require('./router/dataRoute')
const translateRoute = require('./router/translateRoute')
const insertRoute = require('./router/insertRoute')
const cors = require('cors')

const fs = require('fs');
const path = require('path')

const app = express()
app.use(express.urlencoded({extended:true}))
app.use(cors())
app.use(express.json())

app.use('/getraw',dataRoute)
app.use('/translate',translateRoute)
app.use('/insert',insertRoute)

app.listen(process.env.PORT,()=>{
    console.log(`Server started at port ${process.env.PORT}`)
})