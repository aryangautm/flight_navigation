function RouteDetails({paths}){
  return paths.map(path => (
    <div className="flex items-start justify-between w-full p-3 ">
      <div className="flex items-start justify-start gap-2">
        <img
          src={"https://flagcdn.com/w40/"+path.countryCode+".png"}
          alt={path.countryName}
          className="w-6 h-6 sm:w-9 sm:h-9 object-contain"
        />
        <div className="flex flex-col items-start justify-start">
          <h1 className="text-[#27273F] font-normal text-sm sm:text-base">
            {path.airportCode}
          </h1>
          <p className="text-[#7C8DB0] font-normal text-sm sm:text-base">
            {path.airportName}
          </p>
          <p className="text-[#7C8DB0] font-normal text-sm sm:text-base">
            {path.cityName+", "+path.countryName}
          </p>
        </div>
      </div>
      <div className="flex flex-col items-end gap-2">
        <p className="text-[#27273F] font-normal text-sm sm:text-base">
          {path.time}
        </p>
        <p className="text-[#27273F] font-normal text-sm sm:text-base">
          {path.distance}
        </p>
        <p className="text-[#7C8DB0] font-normal text-sm sm:text-base">
          {path.feasibilityScore}
        </p>
      </div>
    </div>
  ));
}
export default RouteDetails