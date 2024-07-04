#!/bin/bash

echo "Installing dependencies..."
npm install

if ! command -v http-server &> /dev/null
then
    echo "http-server could not be found, installing globally..."
    npm install -g http-server
fi

echo "Starting server..."
http-server . -o /index.html