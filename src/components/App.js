import React, { useState, useEffect } from "react";

import Header from "./Header";
import ToyForm from "./ToyForm";
import ToyContainer from "./ToyContainer";


function App() {
  const [ showForm, setShowForm ] = useState(false);
  const [ toys, setToys ] = useState([]);

  function handleClick() {
    setShowForm((showForm) => !showForm);
  }

  useEffect(() => {
    fetch("http://127.0.0.1:5555/toys")
    .then(response => response.json())
    .then(data => setToys(data))    
  }, [])

  return (
    <>
      <Header />
      {showForm ? <ToyForm toys={toys} setToys={setToys}/> : null}
      <div className="buttonContainer">
        <button onClick={handleClick}>Add a Toy</button>
      </div>
      <ToyContainer toys={toys} setToys={setToys} />
    </>
  );
}

export default App;
