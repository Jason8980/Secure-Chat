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

# Change port back to 8000 for Koyeb compatibility
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
