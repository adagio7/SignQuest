// Start.jsx
import React from 'react';
import { Link } from 'react-router-dom';
import "./global.css";

function Start() {
    return (
        <div className='content-container'>
            <div className="starry-background"></div>
            <div className="moon"></div>
            <h1>Welcome to <span style={{ color: '#6FA5FF' }}>Sign</span><span style={{ color: '#FFEB3B' }}>Quest</span>!</h1>
            <div className='slogan-container'>
                <p>SignQuest is the ultimate way to learn American Sign Language (ASL).You can practice signing letters and words, and even compete with others to test your skills!</p>
            </div>
            <div>
                <Link to="/Home">
                    <button>Get Started</button>
                </Link>
            </div>
        </div>
    );
}

export default Start;
