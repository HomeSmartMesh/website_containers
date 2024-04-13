FROM node:20
WORKDIR /workspace

RUN npm install -g pnpm
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/MicroWebStacks/astro-big-doc.git /astro-big-doc
WORKDIR /astro-big-doc

# Install
RUN pnpm install

# Copy scripts into the container
COPY build.sh build.sh

# Set build.sh as the entrypoint
ENTRYPOINT ["./build.sh"]
