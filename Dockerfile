# Use an official Node.js image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire project
COPY . .

# Build the frontend
RUN npm run build

# Install serve globally
RUN npm install -g serve

# Expose the port
EXPOSE 3000

# Start the frontend with serve
CMD ["serve", "-s", "build", "-l", "3000"]
