FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if available) from frontend
COPY frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy the entire frontend project
COPY frontend ./

# Expose the React development server port
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
