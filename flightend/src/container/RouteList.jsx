function RouteList({routes}){
    return routes.map((route, index) =>(
        <div
              className="w-full cursor-pointer border-b-[1px] border-[#E9E8FC] hover:bg-[#F6F6FE] transition-all duration-300 focus:bg-[#F6F6FE]"
              onClick={() => {setPathShow(false); SetView(index)}}
            >
        <RouteCard
                destination = {route.destination}
                destinationName = {route.destinationName} 
                destinationCountryCode = {route.destinationCountryCode}
                destinationCity = {route.destinationCity}
                destinationCountry = {route.destinationCountry}
                source = {route.source}
                sourceName = {route.sourceName} 
                sourceCountryCode = {route.sourceCountryCode} 
                sourceCity = {route.sourcecity} 
                sourceCountry = {route.sourceCountry}
                totalTime = {route.totalTime} 
                totalDistance = {route.totalDistance}
                avgFeasibility = {route.avgFeasibility}
                totalEmissions = {route.totalEmissions}
              />
        </div>
    ));
}

export default RouteList;