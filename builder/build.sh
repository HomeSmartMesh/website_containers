#!/bin/bash

# Navigate into the astro-big-doc directory
cd /astro-big-doc

# Copy necessary files from the user_repo
rm -rf /astro-big-doc/content
rm -rf /astro-big-doc/public
cp -R /user_repo/content /astro-big-doc
cp -R /user_repo/public /astro-big-doc
cp /user_repo/menu.yaml /astro-big-doc/menu.yaml

# Build the site
pnpm run build
