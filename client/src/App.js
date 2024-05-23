import './App.css';
import React from 'react';
import FlightForm from './components/FlightForm/mainForm';
import Navbar from './components/NavBar/navBar';

function App() {
  return (
    <div className="App">
      <Navbar />
      <FlightForm />
    </div>
  );
}

export default App;
