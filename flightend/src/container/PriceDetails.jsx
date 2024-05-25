import { hawaiian } from "../assets/logo";

const PriceDetails = () => {
  return (
    <>
      <div className="flex flex-col items-start lg:items-end justify-start lg:justify-end gap-5 w-full h-full sm:w-[600px]">
        <div className=" w-full border-[1px] border-[#E9E8FC] rounded-lg  flex flex-col gap-2">
          <div className="flex items-start justify-between w-full p-3 ">
            <div className="flex items-start justify-start gap-2">
              <img
                src= "https://flagcdn.com/w40/in.png"
                alt="INDIA"
                className="w-6 h-6 sm:w-9 sm:h-9 object-contain"
              />
              <div className="flex flex-col items-start justify-start">
                <h1 className="text-[#27273F] font-normal text-sm sm:text-base">
                  IXC
                </h1>
                <p className="text-[#7C8DB0] font-normal text-sm sm:text-base">
                  Chandigarh Internation Airport
                </p>
                <p className="text-[#7C8DB0] font-normal text-sm sm:text-base">
                  Chandigarh, India
                </p>
              </div>
            </div>
            <div className="flex flex-col items-end gap-2">
              <p className="text-[#27273F] font-normal text-sm sm:text-base">
                0 Hr
              </p>
              <p className="text-[#27273F] font-normal text-sm sm:text-base">
                0 km
              </p>
              <p className="text-[#7C8DB0] font-normal text-sm sm:text-base">
                100%
              </p>
            </div>
          </div>
          
          
        </div>
      </div>
    </>
  );
};

export default PriceDetails;
