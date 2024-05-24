import { departure, arrival, calendar, person } from "../assets/icons";

import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import { format } from "date-fns";
import { useState } from "react";

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
      <div className="w-full">
        <div className="lg:w-[872px] w-full flex flex-col gap-10">
          <div className="flex w-full h-12 lg:flex-row items-center flex-col lg:shadowCard  relative ">
            <div className="flex w-full lg:w-[173.92px] h-full justify-start items-center border-[1px] border-[#CBD4E6] p-2 rounded-t-[4px] lg:rounded-l-[4px]">
              <img src={departure} alt="departure" />
              <input
                type="text"
                placeholder="SFO"
                className="outline-none cursor-not-allowed border-none ml-2 placeholder:text-[#7C8DB0] placeholder:text-sm placeholder:leading-6"
              />
            </div>

            <div className="flex w-full lg:w-[173.92px] h-full justify-start items-center border-[1px] border-[#CBD4E6] p-2">
              <img src={arrival} alt="departure" />
              <input
                type="text"
                placeholder="NRT"
                className="outline-none cursor-not-allowed border-none ml-2 placeholder:text-[#7C8DB0] placeholder:text-sm placeholder:leading-6"
              />
            </div>

            <div className="flex w-full  h-full justify-start items-center border-[1px] border-[#CBD4E6] p-2">
              <img src={calendar} alt="calendar" />
              <span
                className="datepicker-wrapper text-[#7C8DB0] text-sm leading-6 ml-2 cursor-pointer"
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
            </div>

            <div className="flex w-full lg:w-[174.92px] h-full justify-start items-center border-[1px] border-[#CBD4E6] p-2" style={{ width: "600px" }}>
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
          </div>

            <div className="w-full lg:w-[96px] ">
              <button className="w-full bg-[#605DEC] text-[#FAFAFA] text-lg leading-6 h-[48px] px-5   rounded-b-[4px] lg:rounded-r-[4px]">
                Search
              </button>
            </div>
          </div>

          {/* Select section */}

          <div className="flex flex-wrap items-center  justify-start gap-3 mt-48 lg:mt-1 ">
            <select
              name="price"
              id="max-price"
              className="border-[1px] border-[#CBD4E6] bg-white text-[#27273F] p-1 cursor-pointer"
            >
              <option value="max-price" className="">
                Max price
              </option>
              <option value="$100-300">$100-300</option>
              <option value="$300-600">$300-600</option>
              <option value="$600-1000">$600-1000</option>
            </select>
            <select
              name="shops"
              id="shops"
              className="border-[1px] border-[#CBD4E6] bg-white text-[#27273F] p-1 cursor-pointer"
            >
              <option value="shops" className="">
                Shops
              </option>
            </select>
            <select
              name="times"
              id="times"
              className="border-[1px] border-[#CBD4E6] bg-white text-[#27273F] p-1 cursor-pointer"
            >
              <option value="times" className="">
                Times
              </option>
              <option value="7 AM - 4 PM">7 AM - 4 PM</option>
              <option value="8 AM - 12 PM">8 AM - 12 PM</option>
              <option value="6 PM - 10 PM">6 PM - 10 PM</option>
            </select>
            <select
              name="airlines"
              id="airlines"
              className="border-[1px] border-[#CBD4E6] bg-white text-[#27273F] p-1 cursor-pointer"
            >
              <option value="airlines" className="">
                Airlines
              </option>
              <option value="Japan">Japan</option>
              <option value="Hawai">Hawai</option>
              <option value="Dubai">Dubai</option>
            </select>
            <select
              name="class"
              id="class"
              className="border-[1px] border-[#CBD4E6] bg-white text-[#27273F] p-1 cursor-pointer"
            >
              <option value="class" className="">
                Select Class
              </option>
              <option value="A">A</option>
              <option value="B">B</option>
              <option value="C">C</option>
            </select>
            <select
              name="price"
              id="max-price"
              className="border-[1px] border-[#CBD4E6] bg-white text-[#27273F] p-1 cursor-pointer"
            >
              <option value="max-price" className="">
                more
              </option>
            </select>
          </div>
        </div>
      </div>
    </>
  );
};

export default SelectDetails;
