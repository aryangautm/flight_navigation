import { Link } from "react-router-dom";
import {
  FlightChoose,
  RoutesChoose,
  SelectDetails,
  Hero2,
} from "../components";
import { FlightDealsCard, PlacesCard } from "../container";
import { right } from "../assets/icons";
import { bed, holes, kenya, seoul, shangai, wall } from "../assets/images";
import { useLocation } from "react-router-dom";
const FlightExplore = () => {
  const { state } = useLocation();
  const routes = state;
  return (
    <>
      <div className="px-8 w-full flex flex-col">
        <div className="mt-10">
          <Hero2 />
        </div>
        <div className="mt-16">
          <RoutesChoose routes={routes} />
        </div>
      </div>
    </>
  );
};

export default FlightExplore;
