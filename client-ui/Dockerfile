# Use an official Node.js image as the base image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the app code into the container
COPY . .

# Expose the port on which the app runs
EXPOSE 5173

# Set the command to serve the app
CMD npm run dev
