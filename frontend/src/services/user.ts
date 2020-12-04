export function createUser(joinCode: string, data: { name: string; }): Promise<Response> {
  return fetch(`http://localhost:8000/api/users/${joinCode}/`, {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    },
  });
}
