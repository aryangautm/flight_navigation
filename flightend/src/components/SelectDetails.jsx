import { departure, arrival, calendar, person } from "../assets/icons";

import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import { format } from "date-fns";
import { useState } from "react";

const AutoSuggest = (initialValue) => {
  const [input, setInput] = useState('');
  const [matchingSuggestions, setMatchingSuggestions] = useState([]);
  const [isOpen, setIsOpen] = useState(false);

  const handleInputChange = (event) => {
    const inputValue = event.target.value.toLowerCase();
    setInput(inputValue);

    const filteredSuggestions = suggestions.filter((suggestion) =>
      suggestion.toLowerCase().startsWith(inputValue)
    );
    setMatchingSuggestions(filteredSuggestions);
  };

  const handleSuggestionClick = (suggestion) => {
    setInput(suggestion);
    setIsOpen(false);
  };

  return {
    input,
    matchingSuggestions,
    isOpen,
    setInput,
    setIsOpen,
    handleInputChange,
    handleSuggestionClick,
  };
}


const SelectDetails = () => {
  const [startDate, setStartDate] = useState(null);
  const [openDate, setOpenDate] = useState(false);
  const [departureTime, setDepartureTime] = useState("");

  const handleTimeChange = (event) => {
    setDepartureTime(event.target.value);
  };
  
  const handleDateChange = (date) => {
    setStartDate(date);
    setOpenDate(false);
  };

  // const [openOptions, setOpenOptions] = useState(false);
  // const [options, setOptions] = useState({
  //   adult: 1,
  //   minor: 0,
  // });

  const handleOptions = (name, operation) => {
    setOptions((prev) => {
      return {
        ...prev,
        [name]: operation === "i" ? options[name] + 1 : options[name] - 1,
      };
    });
  };

  return (
    <>
      <div className="flex w-full max-w-[1024px] lg:h-[65px] lg:flex-row items-center flex-col mt-20  shadowCard relative ">
          <div className="flex w-full h-full justify-start items-center border-[1px] border-[#CBD4E6] p-2 lg:rounded-l-[4px] relative">
            <img src={departure} alt="departure" />
            <input
              type="text"
              placeholder="From where?"
              value={departureSuggest.input}
              onChange={departureSuggest.handleInputChange}
              onFocus={() => departureSuggest.setIsOpen(true)}
              className="uppercase placeholder:capitalize outline-none border-none ml-2 text-base text-[#7C8DB0] placeholder:text-[#7C8DB0] placeholder:text-base placeholder:leading-6"
             
            />
           { departureSuggest.isOpen && ( 
           <ul className="w-[220px] h-56 absolute top-[70px]  bg-white rounded overflow-scroll">
              {departureSuggest.matchingSuggestions.map((suggestion) => (
                <li
                  key={suggestion}
                  onClick={() => departureSuggest.handleSuggestionClick(suggestion)}
                  className="uppercase  cursor-pointer hover:bg-[#605DEC] px-3 py-1 text-[#7C8DB0] hover:text-[#F6F6FE]  mt-1"
                >
                  {suggestion}
                </li>
              ))}
            </ul>
            )}
          </div>

          <div className="flex w-full h-full justify-start items-center border-[1px] border-[#CBD4E6] p-2">
            <img src={arrival} alt="arrival" />
            <input
              type="text"
              placeholder="Where to?"
              value={arrivalSuggest.input}
        onChange={arrivalSuggest.handleInputChange}
        onFocus={() => arrivalSuggest.setIsOpen(true)}
              className="uppercase placeholder:capitalize outline-none border-none ml-2 text-base text-[#7C8DB0] placeholder:text-[#7C8DB0] placeholder:text-base placeholder:leading-6"
            />
           { arrivalSuggest.isOpen && (
            <ul className="w-[220px] h-56 absolute top-[70px] bg-white rounded overflow-scroll">
              {arrivalSuggest.matchingSuggestions.map((suggestion) => (
                <li
                  key={suggestion}
                  onClick={() => arrivalSuggest.handleSuggestionClick(suggestion)}
                  className="uppercase cursor-pointer hover:bg-[#605DEC] px-3 py-1 text-[#7C8DB0] hover:text-[#F6F6FE]  mt-1"
                >
                  {suggestion}
                </li>
              ))}
            </ul>
            )}
          </div>

          {/* <div className="flex w-full h-full justify-start items-center border-[1px] border-[#CBD4E6] p-2">
            <img src={calendar} alt="calendar" />
            <span
              className="text-[#7C8DB0] text-base leading-6 ml-2 cursor-pointer"
              onClick={() => setOpenDate(!openDate)}
            >
              {startDate
                ? `${format(startDate, "dd/MM/yyyy")}`
                : "Departure Date"}
            </span>
            {openDate && (
              <DatePicker
          selected={startDate}
          onChange={handleDateChange}
          inline
          className="absolute top-64 lg:top-20 z-10"
               />
            )}
          </div> */}
          {/* <div className="flex w-full h-full justify-start items-center border-[1px] border-[#CBD4E6] p-2">
            <img src={calendar} alt="clock" />
            <span
              className="text-[#7C8DB0] text-base leading-6 ml-2 cursor-pointer"
              onClick={() => setOpenTime(!openTime)}
            >
              {startTime ? `${format(startTime, "hh/mm/ss")}`: "Departure Time"}
            </span>
            {openTime && (
              // <TimePicker selected={startTime} onChange={handleTimeChange} inline className="absolute top-64 lg:top-20 z-10"/>
              <DesktopTimePicker defaultValue={dayjs('2022-04-17T15:30')} inline className="absolute top-64 lg:top-20 z-10"/>) }
          </div> */}

          {/* <div className="flex w-full lg:w-[174.92px] h-full justify-start items-center border-[1px] border-[#CBD4E6] p-2" style={{ width: "600px" }}>
            <div style={{ width: '100%' }}>
              <label style={{ display: 'block', marginBottom: '0px', color: '#7C8DB0'}} >Departure Time</label>
              <input
                type="time"
                value={departureTime}
                onChange={handleTimeChange}
                required
                style={{width: '100%', padding: '2px', borderRadius: '0px', border: '0px solid red' }}
              />
            </div>
          </div> */}

          <button className="w-full bg-[#605DEC] text-[#FAFAFA] text-lg leading-6 h-[45px] lg:h-[65px] px-5  lg:rounded-r-[4px]" 
            onClick = {async () => {
              console.log(departureSuggest.input);
              console.log(arrivalSuggest.input);
              const url = "http://192.168.29.135:8000/api/shortest-path/?source=" + departureSuggest.input.toUpperCase()+"&destination="+arrivalSuggest.input.toUpperCase();
              console.log(url);
              const res = await fetch(url);
              const data = await res.json() ;
              navigate("/explore", {state:data});

            }}
              >
              Search
            </button>
          {/* <Link to="/explore" className="w-full ">
            <button className="w-full bg-[#605DEC] text-[#FAFAFA] text-lg leading-6 h-[45px] lg:h-[65px] px-5  lg:rounded-r-[4px]">
              Search
            </button>
          </Link> */}
        </div>
    </>
  );
};

export default SelectDetails;
