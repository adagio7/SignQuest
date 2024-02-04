// Home.jsx

import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import './global.css';

function Home() {
  const [userName, setUserName] = useState('');
  const [isNameEntered, setIsNameEntered] = useState(false);

  useEffect(() => {
    const storedName = localStorage.getItem('name');
    if (storedName) {
      setUserName(storedName);
      setIsNameEntered(true);
    }
  }, []);

  const handleNameSubmit = (e) => {
    e.preventDefault();
    setIsNameEntered(true);
    localStorage.setItem('name', userName);
  };

  return (
    <div className="home-container">
      {isNameEntered && (
        <Link to="/home">
          <div className="home-button"><span style={{ color: '#6FA5FF' }}>Sign</span><span style={{ color: '#FFEB3B' }}>Quest</span></div>
        </Link>
      )}
      {!isNameEntered ? (
        <form onSubmit={handleNameSubmit} style={{ fontFamily: 'inherit' }}>
        <h1>
          Hello{' '}
          <input
            type="text"
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
            placeholder='your name...'
            style={{
              background: 'transparent',  // Set the background to clear
              border: 'none',            // Remove border
              borderBottom: '1px solid #000', // Add a bottom border for visibility
              outline: 'none',           // Remove outline
              color: 'inherit',          // Inherit text color
              fontFamily: 'inherit',     // Inherit font family
              fontSize: 'inherit',       // Inherit font size
              // Add any additional styles as needed
            }}
          />
        </h1>
        <button type="submit">Enter</button>
      </form>
      
      ) : (
        <>
        <h2 style={{ fontSize: '32px' }}>Hello, {userName}!</h2>
        <div className="button-container" style={{ fontSize: '24px', textAlign: 'center' }}>
            <Link to="/practice">
            <button style={{ fontSize: '24px' }}>Practice</button>
            </Link>
            <Link to="/competitive">
            <button style={{ fontSize: '24px' }}>Competitive</button>
            </Link>
            <Link to="/leaderboard">
            <button style={{ fontSize: '24px' }}>Leaderboard</button>
            </Link>
        </div>
        </>
      )}
    </div>
  );
}

export default Home;


