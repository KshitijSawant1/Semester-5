import React from "react";
import ClockGrid from "./ClockGrid";


const App = () => (
  <div className="min-h-screen bg-black flex flex-col items-center justify-center text-white">
    <h1 className="text-2xl font-bold mb-6">🕒 Clock of Clocks</h1>
    <ClockGrid />
  </div>
);

export default App;
