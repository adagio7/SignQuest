import React, { useState } from "react";
import { Link } from 'react-router-dom';
import CustomWebcam from "../components/CustomWebcam";
import "./global.css"; // Import a CSS file for styling

function PracticePage() {

  console.log("PracticePage");
  
  const [randomLetter, setRandomLetter] = useState(generateRandomLetter());

  function generateRandomLetter() {
    const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const randomIndex = Math.floor(Math.random() * alphabet.length);
    return alphabet[randomIndex];
  }

  function handleSkipButtonClick() {
    setRandomLetter(generateRandomLetter());
  }

  return (
    <div className="home-container">
      <Link to="/home">
      <div className="home-button"><span style={{ color: '#6FA5FF' }}>Sign</span><span style={{ color: '#FFEB3B' }}>Quest</span></div>
      </Link>
      <div className="random-letter">
        <h1>Current Letter: {randomLetter}</h1>
        <div className="app-container">
          <CustomWebcam />
        </div>
        <button onClick={handleSkipButtonClick}>Skip</button>
      </div>
    </div>
  );
}

export default PracticePage;

