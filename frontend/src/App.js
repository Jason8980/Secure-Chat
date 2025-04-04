import React, { useState, useEffect } from "react";
import "./App.css";

const username = prompt("Enter your username (Aryan$8980 or Parth8012):");

const App = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [typing, setTyping] = useState(false);
  const socket = new WebSocket("wss://your-koyeb-url/ws");

  useEffect(() => {
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === "message") {
        setMessages((prev) => [...prev, { user: data.user, text: data.text }]);
      } else if (data.type === "typing") {
        setTyping(data.user !== username);
      }
    };
  }, []);

  const sendMessage = () => {
    if (input.trim()) {
      socket.send(JSON.stringify({ type: "message", user: username, text: input }));
      setInput("");
    }
  };

  const handleTyping = () => {
    socket.send(JSON.stringify({ type: "typing", user: username }));
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((msg, index) => (
          <div key={index} className={msg.user === username ? "sent" : "received"}>
            <div className="avatar">{msg.user === "Aryan$8980" ? "K%99" : "D₹!2"}</div>
            <p>{msg.text}</p>
          </div>
        ))}
        {typing && <p className="typing-indicator">Typing...</p>}
      </div>
      <input
        type="text"
        placeholder="Type a message..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyPress={handleTyping}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
};

export default App;
