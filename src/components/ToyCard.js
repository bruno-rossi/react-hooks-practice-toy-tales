import React, { useState } from "react";

function ToyCard({ toy, toys, setToys }) {

  const [ likes, setLikes ] = useState(toy.likes);

  function handleDelete(event) {

    fetch(`http://localhost:3001/toys/${toy.id}`, {
      method: "DELETE",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
      }})
    .then(response => response.json())

    const toysAfterDelete = toys.filter(toy => toy.id);

    setToys(toysAfterDelete);

    event.target.parentNode.remove();

  }

  function handleLikeClick() {

    const updatedLikes = likes +1;
    setLikes(likes => updatedLikes);

    const patchedToy = {
      ...toy,
      updatedLikes
    }

    console.log(patchedToy);

    fetch(`http://localhost:3001/toys/${toy.id}`, {
      method: "PATCH",
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
      },
      body: JSON.stringify(patchedToy)
    })
    .then(response => response.json())
    .then(data => {
      
      const toysAfterPatch = toys.map(element => {
        if (element.id === toy.id) {
          return { ...element, likes: updatedLikes}
        } else {
          return element
        }
      });
  
      console.log(toysAfterPatch);
  
      setToys(toysAfterPatch);
    })


  }

  return (
    <div className="card">
      <h2>{toy.name}</h2>
      <img
        src={toy.image}
        alt={toy.name}
        className="toy-avatar"
      />
      <p>{toy.likes} Likes </p>
      <button className="like-btn" onClick={() => handleLikeClick()}>Like {"<3"}</button>
      <button className="del-btn" onClick={handleDelete}>Donate to GoodWill</button>
    </div>
  );
}

export default ToyCard;
