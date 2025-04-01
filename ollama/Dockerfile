FROM ollama/ollama

# Kópie scriptu na správne miesto v kontajneri
COPY ./pull-llama3.sh /pull-llama3.sh

# Zabezpečte, že skript je spustiteľný
RUN chmod +x /pull-llama3.sh

# Nastavenie predvoleného pracovného adresára
WORKDIR /

# Spustenie skriptu
ENTRYPOINT ["/pull-llama3.sh"]
