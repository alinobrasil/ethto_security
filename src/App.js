// import logo from './logo.svg';
import './App.css';
// import { useState } from 'react';


function App() {

  // const [contractAddress, setContractAddress] = useState('');

  const handleClick = () => {
    // logic to handle click, using contract address
    let inputVal = document.getElementById('inputbox').value;
    console.log(inputVal);


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

      <div className='bgtag'>
        Bg Photo by Scott Webb on Unsplash
      </div>

    </div>
  );
}

export default App;
