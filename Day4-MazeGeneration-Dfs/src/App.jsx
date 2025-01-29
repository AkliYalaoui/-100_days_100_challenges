import React from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Maze from "./components/Maze";
import Explanation from "./components/Explanation";

const App = () => {
  return (
    <>
      <Header />
      <Maze />
      <Explanation />
      <Footer />
    </>
  );
};

export default App;
