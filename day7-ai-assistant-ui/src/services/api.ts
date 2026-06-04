import type { Message } from "../types/chat";

export const sendMessage = async (messages: Message[]) => {
  const response = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      messages
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to send message");
  }

  return response.json();
};