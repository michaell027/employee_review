#!/bin/bash

echo "Starting Ollama server..."
ollama serve &
pid=$!

echo "Waiting for Ollama server to start..."
sleep 10

# Check if the model is already downloaded
if ollama list | grep -q "llama3.2"; then
    echo "LLaMA 3.2 model is already downloaded."
else
    echo "Downloading LLaMA 3.2 model..."
    ollama pull llama3.2
fi

# Keep Ollama server running
wait $pid
