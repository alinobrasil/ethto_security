import './App.css';
import React, { useState, useEffect } from "react";

function App() {

  const [contractAddress, setContractAddress] = useState({
    Name : "", 
    Age : "",
    Date : "", 
    programming : ""}
    );

  const handleClick = () => {
    let inputVal = document.getElementById('inputbox').value;
    fetch("/result", {
      method:"POST",
      cache: "no-cache",
      headers:{
          "content_type":"application/json",
      },
      body:JSON.stringify(inputVal)
      }
    ).then(response => {
    return response.json()
    })
    fetch("/${inputVal}").then((res) =>
            res.json().then((contractAddress) => {
                setContractAddress({
                    name: data.Name,
                    age: data.Age,
                    date: data.Date,
                    programming: data.programming,
                });
            })
        
    .then(json => {
      this.setState({result: json})
    })
    );
  }
  return (
    <div className="App">

      <div className='title'>
        <h1>Smart Contract Security Check</h1>

      </div>


      <div className='main'>

        <input

          id='inputbox'
          type="text"
          placeholder='address of contract to check'
        />

        <button className='button-7' onClick={handleClick}>
          Run check
        </button>
      </div>

      <div id="output">
          {this.state.json}
      </div>

      <div className='bgtag'>
        Bg Photo by Scott Webb on Unsplash
      </div>

    </div>
  );
}

export default App;
