# Stage 1: Build the React Frontend
FROM node:16-alpine AS build-frontend
WORKDIR /app/frontend
# Copy package files and install dependencies
COPY frontend/package*.json ./
RUN npm install
# Copy all frontend source code and build the app
COPY frontend/ ./
RUN npm run build

# Stage 2: Set Up the Python Backend
FROM python:3.9-slim
WORKDIR /app

# Copy backend code
COPY backend/ ./backend
# Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the built frontend from Stage 1 into the backend folder
COPY --from=build-frontend /app/frontend/build ./frontend/build

# Expose static files and set the startup command
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "80"]
