import { useState } from "react";
import { map } from "../assets/images";
import {
  delta,
  france,
  hawaiian,
  japan,
  quantas,
  united,
} from "../assets/logo";
import { RouteDetails, RouteCard } from "../container";

const FlightChoose = () => {
  const pathList = [
    [
      {
        countryCode: "in",
        countryName: "India",
        airportCode: "IXC",
        airportName: "Chandigarh International Airport",
        cityName: "Chandigarh",
        time: "0 hr",
        distance: "0 km",
        feasibilityScore: "100%",
      },
      {
        countryCode: "in",
        countryName: "India",
        airportCode: "DEL",
        airportName: "Indira Gandhi Internation Airport",
        cityName: "Delhi",
        time: "2hrs",
        distance: "267 km",
        feasibilityScore: "98.6%",
      },
      {
        countryCode: "us",
        countryName: "United States of America",
        airportCode: "JKF",
        airportName: "John F. Kennedy International Airport",
        cityName: "New York",
        time: "19hr",
        distance: "11213 km",
        feasibilityScore: "94.2%",
      },
    ],
    [
      {
        countryCode: "pk",
        countryName: "Pakistan",
        airportCode: "LMO",
        airportName: "Dastan International Airport",
        cityName: "Lahore",
        time: "0 hr",
        distance: "0 km",
        feasibilityScore: "100%",
      },
      {
        countryCode: "in",
        countryName: "India",
        airportCode: "DEL",
        airportName: "Indira Gandhi Internation Airport",
        cityName: "Delhi",
        time: "2hrs",
        distance: "885 km",
        feasibilityScore: "98.6%",
      },
      {
        countryCode: "us",
        countryName: "United States of America",
        airportCode: "JKF",
        airportName: "John F. Kennedy International Airport",
        cityName: "New York",
        time: "19hr",
        distance: "11213 km",
        feasibilityScore: "94.2%",
      },
    ],
    [
      {
        countryCode: "bd",
        countryName: "Bangladesh",
        airportCode: "DAC",
        airportName: "Terror International Airport",
        cityName: "Dhaka",
        time: "0 hr",
        distance: "0 km",
        feasibilityScore: "100%",
      },
      {
        countryCode: "in",
        countryName: "India",
        airportCode: "DEL",
        airportName: "Indira Gandhi Internation Airport",
        cityName: "Delhi",
        time: "2hrs",
        distance: "696 km",
        feasibilityScore: "98.6%",
      },
      {
        countryCode: "us",
        countryName: "United States of America",
        airportCode: "JKF",
        airportName: "John F. Kennedy International Airport",
        cityName: "New York",
        time: "19hr",
        distance: "11213 km",
        feasibilityScore: "94.2%",
      },
    ],
  ];
  const [active, setActive] = useState(1);
  const SetView = (active) => {
    setActive(active);
  };

  const ActiveView = () => {
    switch (active) {
      case 1:
        return <RouteDetails paths={pathList[0]} />;
      case 2:
        return <RouteDetails paths={pathList[1]} />;
      case 3:
        return <RouteDetails paths={pathList[2]} />;
      default:
        return <RouteDetails paths={pathList[0]} />;
    }
  };
  return (
    <>
      <div className="flex lg:flex-row flex-col items-start justify-between gap-16 ">
        <div className="w-full lg:w-[872px] h-full flex flex-col gap-5">
          <div className="flex items-start justify-start">
            <h1 className="text-[#6E7491]  text-lg leading-6 font-semibold">
              Choose a <span className="text-[#605DEC]">departing </span>/{" "}
              <span className="text-[#605DEC]">returning </span>flight
            </h1>
          </div>
          <div className="w-full flex flex-col items-start justify-start  border-[1px] border-[#E9E8FC] rounded-xl">
            <div
              className="w-full cursor-pointer border-b-[1px] border-[#E9E8FC] hover:bg-[#F6F6FE] transition-all duration-300 focus:bg-[#F6F6FE]"
              onClick={() => {
                SetView(1);
              }}
            >
              <RouteCard
                destination="JFK"
                destinationName="John F. Kennedy Airport"
                destinationCountryCode="us"
                destinationCity="New York"
                destinationCountryName="United States of America"
                source="IXC"
                sourceName="Chandigarh International Airport"
                sourceCountryCode="in"
                sourceCity="Chandigarh"
                sourceCountryName="India"
                totalTime="21 hr"
                totalDistance="11480"
                avgFeasibility="96.4%"
                totalEmissions="23312 kg CO2"
              />
            </div>
            <div
              className="w-full cursor-pointer border-b-[1px] border-[#E9E8FC]  hover:bg-[#F6F6FE] transition-all duration-300 focus:bg-[#F6F6FE]"
              onClick={() => {
                SetView(2);
              }}
            >
              <FlightPathCard
                dest="LAO"
                destName=" Indira Gandhi International Airport"
                country="India"
                countryCode="pk"
                city="Delhi"
                time="2 Hrs"
                distance="267.3 KM"
                feasibility="98.6%"
                emissions="232 KG of CO2"
              />
            </div>
            <div
              className="w-full cursor-pointer border-b-[1px] border-[#E9E8FC]  hover:bg-[#F6F6FE] transition-all duration-300 focus:bg-[#F6F6FE]"
              onClick={() => {
                SetView(3);
              }}
            >
              <FlightPathCard
                dest="MUH"
                destName=" Indira Gandhi International Airport"
                country="India"
                countryCode="bd"
                city="Delhi"
                time="2 Hrs"
                distance="267.3 KM"
                feasibility="98.6%"
                emissions="232 KG of CO2"
              />
            </div>
          </div>
          <div className="w-full lg:mt-12">
            <img src={map} alt="map" className="w-full h-full object-cover" />
          </div>
        </div>

        {/* {priceShown && (
         <PriceGraph/>
        )} */}

        {
          <div className="mt-10 flex flex-col gap-10 justify-end items-start lg:items-end">
            {ActiveView()}
            <button
              className="text-[#605DEC] border-2 border-[#605DEC] py-2 px-3 rounded hover:bg-[#605DEC] hover:text-white transition-all duration-200"
              onClick={() => {
                setPriceShow(true);
              }}
            >
              Close
            </button>
          </div>
        }
      </div>
    </>
  );
};

export default FlightChoose;
