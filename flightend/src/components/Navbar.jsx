import { Link } from "react-router-dom";
import naviator from "../assets/logo/naviator.png";
import { useState } from "react";
import { Signin } from "../container";

const Navbar = () => {
  const [signin, setSignin] = useState(false);

  return (
    <>
      <nav className="w-full flex flex-row items-center justify-between px-2 py-2 relative">

        <div className="flex items-center justify-center gap-3">
          <Link to="/">

            <img
              src={naviator}
              alt="naviator"
              className="md:w-[150px] md:h-[50px] w-[120px] h-[40px] object-contain"
            />
          </Link>

        </div>
        {/* <div className="hidden md:flex items-center space-x-8">
          <div className="">
            <button className="bg-[#605DEC] py-2 px-4 md:py-3 md:px-5 rounded-[5px] border-2 border-[#605DEC] text-base text-[#FAFAFA] hover:text-[#605DEC] hover:bg-white hover:border-2 hover:border-[#605DEC] transition-all duration-200" onClick={() => setSignin(!signin)}>Sign up</button>
            {signin && (
              <Signin signin={signin} setSignin={setSignin} />
            )}
          </div>
        </div> */}

      </nav>
    </>
  );
};

export default Navbar;
