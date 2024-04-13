#!/bin/bash

# Install global dependencies
npm install -g pnpm

apt-get update && apt-get install -y git

# Clone the astro-big-doc project
git clone https://github.com/MicroWebStacks/astro-big-doc.git /astro-big-doc

# Navigate into the project directory
cd /astro-big-doc

# Install project dependencies
pnpm install
