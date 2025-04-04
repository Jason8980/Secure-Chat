Secure Chat

This is a secure chat application built with FastAPI (backend) and React (frontend). It is designed for two users only:

Aryan$8980 (your account)

Parth8012 (your friend)


When you log in:

Your messages appear on the right with a round logo showing K%99.

Your friend's messages appear on the left with a round logo showing D₹!2.

A typing indicator shows when the other person is typing.


Features

Secure Chat: Only two users can chat.

Hacker-Themed UI: A cool, dark, green theme.

WhatsApp-Style Layout: Messages align right or left.

Typing Indicator: Shows when the other user is typing.

Real-Time Communication: Uses WebSockets for instant messaging.

Deployment via Docker: The project uses a multi-stage Dockerfile that builds the React app and serves it with FastAPI.


Directory Structure

Secure-Chat/
├── backend/
│   └── main.py         # FastAPI backend code
├── frontend/
│   ├── package.json    # React project file
│   ├── public/
│   │   └── index.html  # HTML template for React
│   └── src/
│       ├── App.js      # Main React component with chat logic
│       ├── App.css     # Styling for the chat app
│       └── index.js    # Entry point for React
├── requirements.txt    # Python dependencies (FastAPI, Uvicorn, etc.)
└── Dockerfile          # Multi-stage Dockerfile to build frontend and backend

How to Run Locally

Prerequisites

Python 3.9 installed

Node.js and npm installed


Steps

1. Clone the Repository:

git clone https://github.com/Jason8980/Secure-Chat.git
cd Secure-Chat


2. Build the Frontend:

Go to the frontend folder:

cd frontend

Install dependencies:

npm install

Build the React app:

npm run build

This creates a build folder inside frontend.



3. Run the Backend:

Go to the project root:

cd ..

Run the FastAPI server (make sure your backend code in backend/main.py serves the built frontend):

uvicorn backend.main:app --host 0.0.0.0 --port 8000

Open your browser at http://localhost:8000 to see the chat UI.




How to Deploy with Docker on Koyeb

1. Multi-Stage Dockerfile:

Your Dockerfile (placed at the root) uses two stages:

Stage 1: Builds the React frontend.

Stage 2: Sets up the FastAPI backend and copies the built frontend.


Example Dockerfile content:

# Stage 1: Build the React Frontend
FROM node:16-alpine AS build-frontend
WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Set Up the Python Backend
FROM python:3.9-slim
WORKDIR /app
COPY backend/ ./backend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --from=build-frontend /app/frontend/build ./frontend/build
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "80"]


2. Push to GitHub:

Commit and push all your changes to GitHub.



3. Deploy on Koyeb:

Go to your Koyeb Dashboard.

Create a new service using your GitHub repository.

Koyeb will automatically build the Dockerfile.

Make sure the start command is set as in the Dockerfile.

Your app will be available at your public Koyeb URL.




Usage

1. Open the deployed URL in your browser.


2. When prompted, log in as Aryan$8980 or Parth8012.


3. Start chatting!

Your messages will appear on the right with the logo K%99.

Your friend’s messages will appear on the left with the logo D₹!2.

A typing indicator will show when the other person is typing.




License

This project is open source and free to use.
