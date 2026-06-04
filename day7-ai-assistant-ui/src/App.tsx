import { useState } from "react";
import type { Message } from "./types/chat";
import { sendMessage } from "./services/api";

function App() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: "1",
      role: "assistant",
      content: "Hello 👋 How can I help you today?",
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!input.trim() || loading) return;

    const userMessage: Message = {
      id: crypto.randomUUID(),
      role: "user",
      content: input,
    };

    const updatedMessages = [
      ...messages,
      userMessage,
    ];

    setMessages(updatedMessages);

    setInput("");
    setLoading(true);

    try {
      const data = await sendMessage(updatedMessages);

      const assistantMessage: Message = {
        id: crypto.randomUUID(),
        role: "assistant",
        content: data.result,
      };

      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      console.error(error);
      const errorMessage: Message = {
        id: crypto.randomUUID(),
        role: "assistant",
        content: "Something went wrong.",
      };

      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="h-screen bg-zinc-950 text-white flex flex-col">
      
      {/* Header */}
      <header className="border-b border-zinc-800 px-6 py-4">
        <h1 className="text-xl font-semibold">
          AI Assistant
        </h1>
      </header>

      {/* Messages Area */}
      <main className="flex-1 overflow-y-auto p-6 space-y-4">
        
        {messages.map((message) => (
          <div
            key={message.id}
            className={`flex ${
              message.role === "user"
                ? "justify-end"
                : "justify-start"
            }`}
          >
            <div
              className={`px-4 py-3 rounded-2xl max-w-lg ${
                message.role === "user"
                  ? "bg-blue-600"
                  : "bg-zinc-800"
              }`}
            >
              {message.content}
            </div>
          </div>
        ))}

      </main>

      {/* Input Area */}
      <footer className="border-t border-zinc-800 p-4">
        <div className="flex gap-3">
          
          <input
            type="text"
            placeholder="Ask something..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className="flex-1 bg-zinc-900 border border-zinc-700 rounded-xl px-4 py-3 outline-none"
          />

          <button
          onClick={handleSend}
          disabled={loading}
          className="bg-white text-black px-5 rounded-xl font-medium disabled:opacity-50"
        >
          {loading ? "Thinking..." : "Send"}
        </button>

        </div>
      </footer>

    </div>
  );
}

export default App;