// Root
// └── App
//     ├── Header
//     ├── ToyForm
//     ├── ToyContainer
//         └── ToyCard

// Deliverable 4:
// When the like button is clicked, make a PATCH request to /toys/:id with the id of the toy that was clicked, along with the new number of likes (this should be sent in the body of the PATCH request, as a object: { likes: 10 }), to update the toy on the server. Clicking on the button should also increase the number of likes on the DOM.


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
    fetch("http://localhost:3001/toys")
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
