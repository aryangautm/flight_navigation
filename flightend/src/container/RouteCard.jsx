/* eslint-disable react/prop-types */

const RouteCard = ({destination, destinationName, destinationCountryCode, destinationCity, destinationCountry, source, sourceName, sourceCountryCode, sourceCity, sourceCountry, totalTime, totalDistance, avgFeasibility, totalEmissions}) => {
  return (
    <>
      <div className="w-full flex flex-row items-start justify-between gap-7 p-4 ">
         <div className="flex items-start gap-2">
            <img src={'https://flagcdn.com/w40/'+sourceCountryCode+'.png'} width="40" alt={sourceName} className="w-6 h-6 sm:w-9 sm:h-9 object-contain" />
            <div className="flex flex-col items-start justify-start">
             <h2 className="text-[#27273F] font-normal text-xs  md:text-base">{source}</h2>
             <p className="text-[#7C8DB0] font-normal text-xs   md:text-base">{sourceName}</p>
             <p className="text-[#7C8DB0] font-normal text-xs   md:text-base">{sourceCity}, {sourceCountry}</p>
            </div>
         </div>
         <div className="flex items-start gap-2">
            <img src={'https://flagcdn.com/w40/'+destinationCountryCode+'.png'} width="40" alt={destinationCountry} className="w-6 h-6 sm:w-9 sm:h-9 object-contain" />
            <div className="flex flex-col items-start justify-start">
            <h2 className="text-[#27273F] font-normal text-xs  md:text-base">{destination}</h2>
            <p className="text-[#7C8DB0] font-normal text-xs   md:text-base">{destinationName}</p>
            <p className="text-[#7C8DB0] font-normal text-xs   md:text-base">{destinationCity}, {destinationCountry}</p>
            </div>
         </div>
         <div className="flex items-start justify-start">
            <p className="text-[#27273F] font-normal text-xs  md:text-base">{totalTime}</p>
         </div>
         <div className="flex flex-col  items-center sm:items-end justify-start">
         <p className="text-[#27273F] font-normal text-xs   md:text-base">{totalDistance}</p>
         {/* <p className="text-[#7C8DB0] font-normal text-xs   md:text-base">{hnl}</p> */}
         </div>
         <div className="flex flex-col items-center sm:items-end justify-start">
         <p className="text-[#27273F] font-normal text-xs  md:text-base">{avgFeasibility}</p>
         <p className="text-[#7C8DB0] font-normal text-xs   md:text-base">{totalEmissions}</p>
         </div>
     </div>
    </>
  );
};

export default RouteCard;
