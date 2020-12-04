import React, { useState } from "react";
import { useParams } from "react-router-dom";
import { createUser } from "../services/user";

function Challenge() {
  const { joinCode } = useParams<{ joinCode: string }>();
  const [name, setName] = useState("");
  const [error, setError] = useState("");

  function handleNameChange(e: React.ChangeEvent<HTMLInputElement>) {
    setName(e.target.value);
  }

  function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    createUser(joinCode, { name: name })
      .then(async res => {
        if (!res.ok) {
          throw new Error();
        }
      })
      .catch(e => {
        setError("Unable to find the challenge that you are looking for.");
      });
  }

  return (
    <div className="text-center">
      { error === "" &&
        <form onSubmit={handleSubmit}>
          <label htmlFor="name" className="block">What should we call you?</label>
          <input
            name="name"
            value={name}
            onChange={handleNameChange}
            className="border border-purple-500 border-solid rounded w-64 max-w-s my-4"
          />
          <button
            className="rounded text-white bg-purple-500 px-4 py-2 block mx-auto"
          >
            Enter challenge
          </button>
        </form>
      }
      { error !== "" && <p>{error}</p> }
    </div>
  );
}

export default Challenge;
