FROM ollama/ollama

# Copy script to the container
COPY ./pull-llama3.sh /pull-llama3.sh

# Ensure the script is executable
RUN chmod +x /pull-llama3.sh

# Set working directory
WORKDIR /

# Use bash to execute the script properly
ENTRYPOINT ["/bin/bash", "/pull-llama3.sh"]
