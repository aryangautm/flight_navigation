import {
  RoutesChoose,
  Hero,
} from "../components";
import { useLocation } from "react-router-dom";
const FlightExplore = () => {
  const { state } = useLocation();
  const routes = state;
  console.log("these are the routes" + routes)
  return (
    <>
      <div className="px-8 w-full flex flex-col">
        <div>
          <Hero />
        </div>
        <div style={{ padding: 50 }}>
          <RoutesChoose routes={routes} />
        </div>
      </div>
    </>
  );
};

export default FlightExplore;
