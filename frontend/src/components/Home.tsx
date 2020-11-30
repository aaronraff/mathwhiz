import React from 'react';
import { useHistory } from "react-router-dom";
import { createChallenge } from "../services/challenge";

function Home() {
  const history = useHistory();

  function handleClick() {
    createChallenge()
      .then(res => res.json())
      .then(data => {
        const id = data.challenge.id;
        history.push(`/challenge/${id}`);
      })
      .catch(err => console.log(err));
  }

  return (
    <div className="text-center">
      <button
        className="mt-32 bg-blue-400 text-white py-3 px-4 rounded-full"
        onClick={handleClick}
      >
        Start a challenge now!
      </button>
    </div>
  );
}

export default Home;
