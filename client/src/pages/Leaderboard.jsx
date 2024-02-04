// Leaderboard.jsx

import React from 'react';
import { Link } from 'react-router-dom';
import "./global.css";

function Leaderboard() {
    // Mock data for leaderboard (replace this with actual data)
    const leaderboardData = [
        { name: 'Player 1', score: 150 },
        { name: 'Player 2', score: 130 },
        { name: 'Player 3', score: 120 },
        { name: 'Player 4', score: 110 },
        { name: 'Player 5', score: 100 },
        { name: 'Player 6', score: 90 },
        { name: 'Player 7', score: 80 },
        { name: 'Player 8', score: 70 },
        { name: 'Player 9', score: 60 },
        { name: 'Player 10', score: 50 },
        { name: 'Player 11', score: 40 },
        { name: 'Player 12', score: 30 },
        { name: 'Player 13', score: 20 },
        { name: 'Player 14', score: 10 },
        { name: 'Player 15', score: 5 },
    ];

    return (
        <div className="home-container">
            <Link to="/home">
            <div className="home-button"><span style={{ color: '#6FA5FF' }}>Sign</span><span style={{ color: '#FFEB3B' }}>Quest</span></div>
            </Link>
            <div className='content-container'>
                <h1>Leaderboard</h1>
                <div className='scrollable-leadersboard'>
                    <ol>
                        {leaderboardData.map((player, index) => (
                            <li key={index}>
                                <span>{player.name} </span>
                                <span>{player.score} points</span>
                            </li>
                        ))}
                    </ol>
                </div>
            </div>
        </div>
    );
}

export default Leaderboard;
