# Use Node.js LTS image
FROM node:18

# Set working directory inside container
WORKDIR /app

# Copy package.json first (for caching dependencies)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Expose port
EXPOSE 3000

# Start backend
CMD ["node", "server.js"]

