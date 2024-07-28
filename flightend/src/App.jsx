import "./App.css";
import { Route, Routes } from "react-router-dom";
import { Navbar } from "./components";
import {
  FlightExplore,
  Flights
} from "./pages";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

const App = () => {
  return (
    <>
      <div className="font-Nunito overflow-hidden max-w-[1440px] mx-auto">
        <Navbar />
        <Routes>
          <Route path="/" element={<FlightExplore />} />
          <Route path="/explore" element={<FlightExplore />} />
        </Routes>
      </div>
    </>
  );
};

export default App;
