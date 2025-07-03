# Use a Node.js base image
FROM node:lts-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose the port your Fastify app listens on (e.g., 3000)
EXPOSE 8080

RUN npm run build

# Command to run the Fastify application
CMD ["node", "index.js"]