// Note: Main application component that handles navigation and layout
import React, { useState, useEffect } from 'react';
// import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
// import { Trophy, User, Activity } from 'lucide-react';
//import { Dashboard, Leaderboard, MatchLogging, Profile } from './components/..';
import Dashboard from './components/Dashboard';
import Leaderboard from './components/Leaderboard';
import MatchLogging from './components/Matchlogging';
import Profile from './components/Profile';


const App = () => {
  const [currentPage, setCurrentPage] = useState('home');
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Fetch user data from an API or other source
    const fetchUserData = async () => {
      try {
        const response = await fetch('/api/user');
        const data = await response.json();
        setUser(data);
      } catch (error) {
        console.error('Error fetching user data:', error);
      }
    };

    fetchUserData();
  }, []);

  const renderPage = () => {
    switch(currentPage) {
      case 'home': return <Dashboard user={user} />;
      case 'leaderboard': return <Leaderboard />;
      case 'matches': return <MatchLogging user={user} />;
      case 'profile': return <Profile user={user} />;
      default: return <Dashboard user={user} />;
    }
  };

  const handleNavigation = (page) => {
    setCurrentPage(page);
  };

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Navigation */}
      <nav>
        <button onClick={() => handleNavigation('home')}>Home</button>
        <button onClick={() => handleNavigation('leaderboard')}>Leaderboard</button>
        <button onClick={() => handleNavigation('matches')}>Matches</button>
        <button onClick={() => handleNavigation('profile')}>Profile</button>
      </nav>
      {/* Main content */}
      {renderPage()}
    </div>
  );
};

export default App;