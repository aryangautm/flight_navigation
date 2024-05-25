import { departure, arrival } from "../assets/icons";
import 'react-datepicker/dist/react-datepicker.css';
import { useState } from "react";
import 'react-time-picker/dist/TimePicker.css';
import 'react-clock/dist/Clock.css';
import { suggestions } from "../data/constant";
import { useNavigate } from "react-router-dom";
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

const Hero2 = () => {
  const navigate = useNavigate();
  const departureSuggest = AutoSuggest('');
  const arrivalSuggest = AutoSuggest('');


  return (
    <>
      <header className="flex flex-col items-center relative w-full h-[300px] px-7 py-4">
        <div className="flex justify-center items-center">
          <h1 className="font-extrabold text-12px sm:text-1xl md:text-5xl text-center leading-[55px] sm:leading-[70px] md:leading-[100px] text-gradient" >
            Naviator Flight Search
          </h1>
        </div>

        <div className="flex w-full max-w-[480px] lg:h-[65px] lg:flex-row items-center flex-col mt-20  shadowCard relative ">
          <div className="flex w-full h-full justify-start items-center border-[1px] border-[#CBD4E6] p-2 lg:rounded-l-[4px] relative">
            <img src={departure} alt="departure" />
            <input
              type="text"
              placeholder="From where?"
              value={departureSuggest.input}
              onChange={departureSuggest.handleInputChange}
              onFocus={() => departureSuggest.setIsOpen(true)}
              className="uppercase placeholder:capitalize outline-none border-none ml-2 text-base text-[#7C8DB0] placeholder:text-[#7C8DB0] placeholder:text-base placeholder:leading-6 max-w-[160px]"

            />
            {departureSuggest.isOpen && (
              <ul className="w-[220px] h-20 absolute top-[70px]  bg-white rounded overflow-scroll">
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
            {arrivalSuggest.isOpen && (
              <ul className="w-[220px] h-20 absolute top-[70px] bg-white rounded overflow-scroll">
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
          <button className="w-full bg-[#605DEC] text-[#FAFAFA] text-lg leading-6 h-[45px] lg:h-[65px] px-5  lg:rounded-r-[4px]"
            onClick={async () => {
              console.log(departureSuggest.input);
              console.log(arrivalSuggest.input);
              const url = "http://127.0.0.1:8000/api/shortest-path/?source=" + departureSuggest.input.toUpperCase() + "&destination=" + arrivalSuggest.input.toUpperCase();
              console.log(url);
              const res = await fetch(url);
              const data = await res.json();
              navigate("/explore", { state: data });

            }}
          >
            Search
          </button>
        </div>
      </header>
    </>
  );
};

export default Hero2;
