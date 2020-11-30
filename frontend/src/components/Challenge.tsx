import React from 'react';
import { useParams } from "react-router-dom";

function Challenge() {
  const { id } = useParams<{ id: string }>();
  return (
    <p>{id}</p>
  );
}

export default Challenge;
