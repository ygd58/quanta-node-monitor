# QuantaChain Node Monitor

Terminal-based monitoring dashboard for QuantaChain nodes.
QuantaChain node'lari icin terminal tabanli izleme araci.

## Features
- Live node health status
- Chain height, total supply, difficulty
- Connected peers with uptime
- Mining reward & daily/yearly estimates
- Wallet balance lookup
- Auto-refresh every 10 seconds
- Keyboard: Q=Quit, B=Balance, R=Refresh

## Requirements
- Python 3.6+
- Linux / macOS terminal
- Running QuantaChain node

---

## 1. Node Kurulumu / Node Setup (Docker)

### Ubuntu / VPS

apt update && apt upgrade -y
curl -fsSL https://get.docker.com | sh
systemctl start docker
systemctl enable docker

mkdir -p ~/quanta_data
chmod 777 ~/quanta_data

docker run -d \
  --name quanta-node \
  --restart always \
  --network host \
  -v ~/quanta_data:/home/quanta/quanta_data \
  xd637/quanta-node:alpha-v2

docker logs quanta-node --tail 30 -f

### Ports
- 3000: REST API
- 8333: P2P Network
- 7782: RPC

---

## 2. Wallet Olusturma / Create Wallet

docker exec -it quanta-node quanta new_hd_wallet --file hd_wallet.json
docker exec -it quanta-node quanta hd_wallet --file hd_wallet.json

---

## 3. Monitor Kurulumu / Monitor Setup

git clone https://github.com/ygd58/quanta-node-monitor.git
cd quanta-node-monitor
python3 quanta-monitor.py

---

## 4. Node Guncelleme / Update Node

docker stop quanta-node && docker rm quanta-node
docker pull xd637/quanta-node:latest
docker run -d \
  --name quanta-node \
  --restart always \
  --network host \
  -v ~/quanta_data:/home/quanta/quanta_data \
  xd637/quanta-node:latest

---

## Screenshot

============================================================
  QUANTACHAIN NODE MONITOR // TESTNET ALPHA V2
============================================================
  SAGLIKLI   Uptime: 2s 43d 26sn   21:04:41
------------------------------------------------------------
  Zincir Yuksekligi : 2 blok
  Bagli Peer        : 1
  Mining Odulu      : 1.00 QUA/blok
  Toplam Arz        : 2.00 QUA
  Zorluk            : 65.5K
  Gunluk Tahmini    : 2880 QUA
  Yillik Tahmini    : 1051200 QUA
------------------------------------------------------------
  PEER BAGLANTILARI
  > 152.70.75.64:8333      blok:1    sure:2s 43d 31sn
============================================================
  [Q]Cikis [B]Bakiye [R]Yenile -- 10sn otomatik

---

## Related
- https://github.com/quantachain/quanta
- https://www.quantachain.org
