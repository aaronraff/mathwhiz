export function createChallenge(): Promise<Response> {
  return fetch("http://localhost:8000/api/challenges/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  });
}
