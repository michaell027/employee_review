#!/bin/bash

echo "Starting Ollama server..."
ollama serve &
pid=$!

echo "Waiting for Ollama server to start..."
sleep 10

echo "Pulling Llama3..."
ollama pull llama3.2

wait $pid
