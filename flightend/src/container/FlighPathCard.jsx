/* eslint-disable react/prop-types */
const FlightPathCard = ({ dest, destName, country, countryCode, city, time, distance, feasibility, emissions}) => {
  return (
    <>
     <div className="w-full flex flex-row items-start justify-between gap-7 p-4 ">
         <div className="flex items-start gap-2">
            <img src={'https://flagcdn.com/w40/'+countryCode+'.png'} width="40" alt={country} className="w-6 h-6 sm:w-9 sm:h-9 object-contain" />
            <div className="flex flex-col items-start justify-start">
             <h2 className="text-[#27273F] font-normal text-xs  md:text-base">{dest}</h2>
             <p className="text-[#7C8DB0] font-normal text-xs   md:text-base">{destName},{city},{country}</p>
            </div>
         </div>
         <div className="flex items-start justify-start">
            <p className="text-[#27273F] font-normal text-xs  md:text-base">{time}</p>
         </div>
         <div className="flex flex-col  items-center sm:items-end justify-start">
         <p className="text-[#27273F] font-normal text-xs   md:text-base">{distance}</p>
         {/* <p className="text-[#7C8DB0] font-normal text-xs   md:text-base">{hnl}</p> */}
         </div>
         <div className="flex flex-col items-center sm:items-end justify-start">
         <p className="text-[#27273F] font-normal text-xs  md:text-base">{feasibility}</p>
         <p className="text-[#7C8DB0] font-normal text-xs   md:text-base">{emissions}</p>
         </div>
     </div>
    </>
  )
}

export default FlightPathCard