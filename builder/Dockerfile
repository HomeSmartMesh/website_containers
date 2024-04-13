# Use the official Node.js 20 image as a base
FROM node:20

# Setup work directory for all operations
WORKDIR /workspace

# Copy scripts into the container
COPY install.sh install.sh
COPY build.sh build.sh

# Run install script
RUN ./install.sh

# Set build.sh as the entrypoint
ENTRYPOINT ["./build.sh"]
