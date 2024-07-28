# Dockerfile for React Frontend
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json /app/
COPY package-lock.json /app/
RUN npm install

# Copy project files
COPY . /app/

# Build the application
RUN npm run build

# Install serve to serve the build folder
RUN npm install -g serve

# Expose the port the app runs on
EXPOSE 3000

# Serve the build folder
CMD ["serve", "-s", "build"]
