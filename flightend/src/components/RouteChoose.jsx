import { useState } from "react";
import { map } from "../assets/images";
import { RouteDetails, RouteCard} from "../container";
import { Link } from "react-router-dom";

// import routes from "./routes.js";
function RoutesChoose({routes}){
    const [active, setActive] = useState(1);
    console.log(routes);
    const SetView = (active) => {
      setActive(active);
    };

    const ActiveView = () => {
      switch (active) {
        case 1:
          return <RouteDetails paths={routes[0].paths} />;
        case 2:
          return <RouteDetails paths={routes[1].paths} />;
        case 3:
          return <RouteDetails paths={routes[2].paths} />;
        case 4:
          return <RouteDetails paths={routes[3].paths} />;
        case 5:
          return <RouteDetails paths={routes[4].paths} />;
        default:
          return <RouteDetails paths={routes[0].paths} />;
        
      }
    };
    
    return (
        <>
      <div className="flex lg:flex-row flex-col items-start justify-between gap-16 ">
        <div className="w-full lg:w-[872px] h-full flex flex-col gap-5">
          <div className="flex items-start justify-start">
            <h1 className="text-[#6E7491]  text-lg leading-6 font-semibold">
              Top 5 best Flight Routes
            </h1>
          </div>
          <div className="w-full flex flex-col items-start justify-start  border-[1px] border-[#E9E8FC] rounded-xl">
            {routes.map((route, index) =>(
              <div
              className="w-full cursor-pointer border-b-[1px] border-[#E9E8FC] hover:bg-[#F6F6FE] transition-all duration-300 focus:bg-[#F6F6FE]"
              onClick={() => {SetView(index+1)}}>
              <RouteCard
                destination = {route.destination}
                destinationName = {route.destinationName} 
                destinationCountryCode = {route.destinationCountryCode}
                destinationCity = {route.destinationCity}
                destinationCountry = {route.destinationCountryName}
                source = {route.source}
                sourceName = {route.sourceName} 
                sourceCountryCode = {route.sourceCountryCode} 
                sourceCity = {route.sourceCity} 
                sourceCountry = {route.sourceCountryName}
                totalTime = {route.totalTime} 
                totalDistance = {route.totalDistance}
                avgFeasibility = {route.avgFeasibility}
                totalEmissions = {route.totalEmissions}
              />
              </div>
            ))}
          </div>
        </div>
        {(<div className="mt-10 flex flex-col gap-10 justify-end items-start lg:items-end">
            {ActiveView()}
          </div>
        )}
      </div>
    </>
    );
}

export default RoutesChoose;