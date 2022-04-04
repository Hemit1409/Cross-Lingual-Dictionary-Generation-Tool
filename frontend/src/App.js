import './App.css';
import {BiSearchAlt2} from 'react-icons/bi'
import { useEffect } from 'react';
import axios from 'axios'
import { useState } from 'react';

function App() {

  const [gujData,setGujData] = useState([])
  const [hindiData,setHindiData] = useState([])
//   const [hindiData,setHindiData] = useState()
  const [lvl,setLvl] = useState("1")

  const [gujWord,setGujWord] = useState('select')
  const [hindiWord,setHindiWord] = useState('select')

  const [showConfirm,setShowConfirm] = useState(false)
 
  const getData = async () => {
    // console.log("hi")
    // console.log("gData",gujData)
    await axios.get("http://localhost:5000/getraw/gujdata")
    .then((res)=>{

        // console.log("gujData",gujData)
        setGujData(res.data)
    })
    .catch((e)=>{
        console.log("error",e)
    })

  } 

  useEffect(() => {
    getData()
  })

  const wordClickedGuj = (word) => {
    // console.log(word)
    setGujWord(word)
  }
  const wordClickedHindi = (word) => {
      setHindiWord(word)
  }

  var lvlWord = {
      gujWord,lvl
  }
  const translateClicked = async () => {

    await axios.post("http://localhost:5000/translate/word",lvlWord)
    .then(async(res)=>{
        console.log("res: ",res)
        setShowConfirm(true)
        // try{
        //     await axios.get("http://localhost:5000/getraw/hindidata")
        //     .then((res)=>{

        //         // console.log("gujData",gujData)
        //         setHindiData(res.data)
        //     })
        //     .catch((e)=>{
        //         console.log("error",e)
        //     })
        // }catch(e){
        //     console.log('error ',e)
        // }
    })
    .catch((e)=>{
        console.log("error",e)
    })

  }

  const words = {
      gujWord,
      hindiWord
  }
  
  const submitClicked = async(e) => {
    e.preventDefault()
    console.log('submit clicked')
    // console.log(words)
    await axios.post('http://localhost:5000/insert/data',words)
    .then(async(res)=>{
        if(await res.data.message === 'ok'){
            alert('added in dataset')
        }
    })
  }

  const confirmClicked = async () => {
    try{
        await axios.get("http://localhost:5000/getraw/hindidata")
        .then((res)=>{
            // console.log("gujData",gujData)
            setHindiData(res.data)
            // if(hindiData){
            //     setShowConfirm(false)
            // }
        })
        .catch((e)=>{
            console.log("error",e)
        })
    }catch(e){
        console.log('error ',e)
    }    
  }
  return (
    <section className="mainPage">
        <div className="headingTop">Translator</div>
        <section className="inputArea">
            <div className="leftCol">

                <div className="leftBox">                  
                    <div className="wordList">
                        { 
                            gujData.map((curElem)=>{
                                return(
                                    <div key={curElem} onClick={()=>wordClickedGuj(curElem)}>
                                        <div className="word">{curElem}</div>
                                        <div className="borderLine"></div>
                                    </div>
                                )
                            })
                        }
                    </div>
                </div>
                <div class="searchWord">
                    <input type="text" class="inputSearch" id="typedWord"/> 
                    <span class="searchIcon">
                    <BiSearchAlt2 size={30} />
                    </span>
                </div>

            </div>

            
            <div class="middleCol">
                <div class="lvlHead">Choose Level</div>    
                
                <div class="selectOpthion">
                    <select class="selectLvl"
                    onChange={(e)=>{
                        const lvl = e.target.value
                        setLvl(lvl)
                    }}
                    >
                        <option value="1" >1</option>
                        <option value="1.5" >1.5</option>
                        <option value="2" >2</option>
                        <option value="2.5" >2.5</option>
                    </select>
                </div>
                <div class="ipDisplay">
                    <div class="middleCol">
                        <div class="displayBoxLeft">
                           {gujWord}
                        </div>
                        <div class="textLabel">Gujarati</div>
                    </div>
                    
                    <div>
                        <div class="displayBoxRight">
                            {hindiWord}
                        </div>
                        <div class="textLabel">Hindi</div>
                    </div>
                </div>
            </div>

            <div class="rigthCol">
                <div class="rightBox">      
                {
                    hindiData.map((curElem)=>{
                        return(
                            <div key={curElem} onClick={()=>wordClickedHindi(curElem)}>
                                <div className="word">{curElem}</div>
                                <div className="borderLine"></div>
                            </div>
                        )
                    })
                }
                    {/* <div className="word">{hindiData}</div> */}
                    <div className="borderLine"></div>
                </div>
                <div class="selectStatement">Select Appropriate One</div>
                {
                    showConfirm 
                    ?
                    <div class="askingeBtn" >
                        <div className='fRow'>
                            <span>{gujWord}</span>
                            <span>{lvl}</span>
                        </div>
                        <div className='confirmBtn' onClick={confirmClicked}>Confirm</div>
                    </div>
                    :
                    <div></div>    
                }
            </div>

        </section>
        <section class="btnArea">
            <button class="translateBtn" style={{marginRight:'1rem'}} onClick={translateClicked}>translate</button>
            <button class="translateBtn" onClick={submitClicked}>Submit</button>
        </section>
    </section>
  );
}

export default App;
