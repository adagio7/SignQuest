import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';

import Start from './pages/Start.jsx';
import Home from './pages/Home.jsx';
import Practice from './pages/Practice.jsx';
import Competitive from './pages/Competitive.jsx';
import Leaderboard from './pages/Leaderboard.jsx';
import NotFound from './components/NotFound.jsx';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Start />} />
        <Route path="/home" element={<Home />} />
        <Route path="/practice" element={<Practice />} />
        <Route path="/competitive" element={<Competitive />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="*" element={<NotFound />} /> {/* Use "*" to match any path for NotFound */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
