import React, { useState } from 'react';
import './mainForm.css';

const FlightForm = () => {
  const [flightDate, setFlightDate] = useState('');
  const [departureAirport, setDepartureAirport] = useState('');
  const [arrivalAirport, setArrivalAirport] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const formData = {
      flightDate,
      departureAirport,
      arrivalAirport
    };
    console.log('Form Data:', formData);
  };

  return (
    <div className='main-content'>
      <h1>Flight Details</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="flightDate">Date of Flight:</label>
          <input
            type="date"
            id="flightDate"
            value={flightDate}
            onChange={(e) => setFlightDate(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="departureAirport">Departure Airport:</label>
          <input
            type="text"
            id="departureAirport"
            value={departureAirport}
            onChange={(e) => setDepartureAirport(e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="arrivalAirport">Arrival Airport:</label>
          <input
            type="text"
            id="arrivalAirport"
            value={arrivalAirport}
            onChange={(e) => setArrivalAirport(e.target.value)}
          />
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default FlightForm;
