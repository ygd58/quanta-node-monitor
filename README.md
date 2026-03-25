# QuantaChain Node Monitor

Terminal monitor for QuantaChain nodes. Zero dependency, Python only.

## Install

git clone https://github.com/ygd58/quanta-node-monitor
cd quanta-node-monitor
python3 quanta-monitor.py

## Keys
- Q: Quit
- B: Balance query
- R: Manual refresh
- Auto-refresh every 10 seconds

## Node Setup

docker pull xd637/quanta-node:alpha-v2
mkdir -p ~/quanta_data
docker run -d --name quanta-node --restart always --network host -v ~/quanta_data:/home/quanta/quanta_data xd637/quanta-node:alpha-v2

## Related
- https://github.com/quantachain/quanta
- https://www.quantachain.org
