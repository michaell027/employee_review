ollama serve &
pid=$!

echo "Waiting for Ollama server to start..."
sleep 5

echo "Pulling Llama3..."
ollama pull llama3

wait $pid
