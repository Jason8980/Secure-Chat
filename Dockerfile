# Use an official Node.js image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy the entire project (including package.json)
COPY . .

# Install dependencies
RUN npm install

# Build the frontend (if applicable)
RUN npm run build

# Install serve globally
RUN npm install -g serve

# Expose the port
EXPOSE 3000

# Start the frontend with serve
CMD ["serve", "-s", "build", "-l", "3000"]
