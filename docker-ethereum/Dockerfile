# Use Ubuntu as the base image
FROM ubuntu:20.04

# Install dependencies
RUN apt-get update && apt-get install -y software-properties-common \
    && add-apt-repository -y ppa:ethereum/ethereum \
    && apt-get update && apt-get install -y ethereum

# Create a data directory for the blockchain
RUN mkdir -p /root/.ethereum

# Expose necessary ports
EXPOSE 8545 30303 30303/udp

# Run geth with necessary flags
CMD ["geth", "--http", "--http.addr", "0.0.0.0", "--http.port", "8545", \
     "--http.api", "eth,net,web3,personal", "--allow-insecure-unlock", "--dev"]

