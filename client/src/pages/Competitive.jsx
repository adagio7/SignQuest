import React, { useState } from "react";
import { Link } from 'react-router-dom';
import CustomWebcam from "../components/CustomWebcam";
import "./global.css"; // Import a CSS file for styling

function PracticePage() {
    const [randomLetter, setRandomLetter] = useState(generateRandomLetter());
    const [correctCount, setCorrectCount] = useState(0);
    const [lives, setLives] = useState(3);

    function generateRandomLetter() {
        const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        const randomIndex = Math.floor(Math.random() * alphabet.length);
        return alphabet[randomIndex];
    }

    function handleSkipButtonClick() {
        setRandomLetter(generateRandomLetter());
    }

    function handleLetterInput(letter) {
        if (letter === randomLetter) {
            setCorrectCount(correctCount + 1);
            setRandomLetter(generateRandomLetter());
        } else {
            setLives(lives - 1);
            if (lives === 1) {
                // Game over logic here
            }
        }
    }

    return (
        <div className="home-container">
        <Link to="/home">
            <div className="home-button"><span style={{ color: '#6FA5FF' }}>Sign</span><span style={{ color: '#FFEB3B' }}>Quest</span></div>
        </Link>
            <div className="random-letter">
                <div className="header-container">
                    <h1>Current Letter: {randomLetter}</h1>
                    <div className="score-container">
                        <h2>Correct Count: {correctCount}</h2>
                        <h2>Lives: {lives}</h2>
                    </div>
                </div>
                <div className="app-container">
                    <CustomWebcam onLetterInput={handleLetterInput} />
                </div>
                <button onClick={handleSkipButtonClick}>Skip</button>
            </div>
        </div>
    );
}

export default PracticePage;