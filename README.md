# QuantaChain Node Monitor

Terminal-based monitoring dashboard for QuantaChain nodes.
Zero dependency, Python standard library only.

## Features
- Live node health status
- Chain height, total supply, difficulty
- Connected peers with uptime
- Mining reward and daily/yearly estimates
- Wallet balance lookup
- Auto-refresh every 10 seconds
- Keyboard: Q=Quit, B=Balance, R=Refresh

## Requirements
- Python 3.6+
- Linux or macOS terminal
- Running QuantaChain node

## 1. Node Setup (Docker)

Update system and install Docker:

    apt update && apt upgrade -y
    curl -fsSL https://get.docker.com | sh
    systemctl start docker
    systemctl enable docker

Open ports:

    sudo iptables -I INPUT -p tcp --dport 8333 -j ACCEPT
    sudo iptables -I INPUT -p tcp --dport 3000 -j ACCEPT
    sudo iptables -I INPUT -p tcp --dport 7782 -j ACCEPT

Run the node:

    mkdir -p ~/quanta_data
    chmod 777 ~/quanta_data
    docker run -d --name quanta-node --restart always --network host -v ~/quanta_data:/home/quanta/quanta_data xd637/quanta-node:alpha-v2

Check logs:

    docker logs quanta-node --tail 30 -f

Ports: 3000 REST API, 8333 P2P, 7782 RPC

## 2. Create Wallet

    docker exec -it quanta-node quanta new_hd_wallet --file hd_wallet.json
    docker exec -it quanta-node quanta hd_wallet --file hd_wallet.json

## 3. Monitor Setup

    git clone https://github.com/ygd58/quanta-node-monitor.git
    cd quanta-node-monitor
    python3 quanta-monitor.py

## 4. Update Node

    docker stop quanta-node && docker rm quanta-node
    docker pull xd637/quanta-node:latest
    docker run -d --name quanta-node --restart always --network host -v ~/quanta_data:/home/quanta/quanta_data xd637/quanta-node:latest

## Related
- https://github.com/quantachain/quanta
- https://www.quantachain.org
