import { departure, arrival } from "../assets/icons";
import "react-datepicker/dist/react-datepicker.css";
import { useState, useEffect, useRef } from "react";
import "react-time-picker/dist/TimePicker.css";
import "react-clock/dist/Clock.css";
import { suggestions } from "../data/constant";
import { useNavigate } from "react-router-dom";
const AutoSuggest = (initialValue) => {
  const [input, setInput] = useState("");
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
};

const Hero = () => {
  const navigate = useNavigate();
  const departureSuggest = AutoSuggest("");
  const arrivalSuggest = AutoSuggest("");
  const inputRef = useRef(null);
  const inputRef2 = useRef(null);
  const suggestionListRef = useRef(null);
  const suggestionListRef2 = useRef(null);

  useEffect(() => {
    function handleClickOutside(event) {
      if (
        inputRef.current &&
        suggestionListRef.current &&
        !inputRef.current.contains(event.target) &&
        !suggestionListRef.current.contains(event.target)
      ) {
        departureSuggest.setIsOpen(false);
      }
    }

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [departureSuggest]);

  useEffect(() => {
    function handleClickOutside(event) {
      if (
        inputRef2.current &&
        suggestionListRef2.current &&
        !inputRef2.current.contains(event.target) &&
        !suggestionListRef2.current.contains(event.target)
      ) {
        arrivalSuggest.setIsOpen(false);
      }
    }

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [arrivalSuggest]);


  return (
    <>
      <header className="flex flex-col items-center relative w-full h-[529px] px-7 py-4">
        <div className="flex justify-center items-center">
          <h1 className="font-extrabold text-5xl sm:text-7xl md:text-8xl text-center leading-[55px] sm:leading-[70px] md:leading-[100px] text-gradient">
            Naviator <br /> Flight Search
          </h1>
        </div>

        <div className="flex w-full max-w-[1024px] lg:h-[65px] lg:flex-row items-center flex-col mt-20  shadowCard relative ">
          <div className="flex w-full h-full justify-start items-center border-[1px] border-[#CBD4E6] p-2 lg:rounded-l-[4px] relative">
            <img src={departure} alt="departure" />
            <input
              ref={inputRef}
              type="text"
              placeholder="From where?"
              value={departureSuggest.input}
              onChange={(e) => {
                departureSuggest.handleInputChange(e);
                if (e.target.value.length > 0) {
                  departureSuggest.setIsOpen(true);
                } else {
                  departureSuggest.setIsOpen(false);
                }
              }}
              className="uppercase placeholder:capitalize outline-none border-none ml-2 text-base text-[#7C8DB0] placeholder:text-[#7C8DB0] placeholder:text-base placeholder:leading-6"
            />
            {departureSuggest.isOpen && (
              <ul ref={suggestionListRef} className="suggestion-list w-[220px] h-56 absolute top-[70px]  bg-white rounded overflow-scroll">
                {departureSuggest.matchingSuggestions.map((suggestion) => (
                  <li
                    key={suggestion}
                    onClick={() =>
                      departureSuggest.handleSuggestionClick(suggestion)
                    }
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
              ref={inputRef2}
              type="text"
              placeholder="Where to?"
              value={arrivalSuggest.input}
              onChange={(e) => {
                arrivalSuggest.handleInputChange(e);
                if (e.target.value.length > 0) {
                  arrivalSuggest.setIsOpen(true);
                } else {
                  arrivalSuggest.setIsOpen(false);
                }
              }}
              className="uppercase placeholder:capitalize outline-none border-none ml-2 text-base text-[#7C8DB0] placeholder:text-[#7C8DB0] placeholder:text-base placeholder:leading-6"
            />
            {arrivalSuggest.isOpen && (
              <ul ref={suggestionListRef2} className="suggestion-list w-[220px] h-56 absolute top-[70px] bg-white rounded overflow-scroll">
                {arrivalSuggest.matchingSuggestions.map((suggestion) => (
                  <li
                    key={suggestion}
                    onClick={() =>
                      arrivalSuggest.handleSuggestionClick(suggestion)
                    }
                    className="uppercase cursor-pointer hover:bg-[#605DEC] px-3 py-1 text-[#7C8DB0] hover:text-[#F6F6FE]  mt-1"
                  >
                    {suggestion}
                  </li>
                ))}
              </ul>
            )}
          </div>
          <button
            className="w-full bg-[#605DEC] text-[#FAFAFA] text-lg leading-6 h-[45px] lg:h-[65px] px-5  lg:rounded-r-[4px]"
            onClick={async () => {
              try {
                console.log(departureSuggest.input);
                console.log(arrivalSuggest.input);

                const url = `http://127.0.0.1:8000/api/shortest-path/?source=${departureSuggest.input.toUpperCase()}&destination=${arrivalSuggest.input.toUpperCase()}`;
                console.log(url);

                const response = await fetch(url);
                if (!response.ok) {
                  throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                navigate("/explore", { state: data });
              } catch (error) {
                console.error('There was an error with the fetch operation:', error);
              }
            }}
          >
            Search
          </button>
        </div>
      </header>
    </>
  );
};

export default Hero;
