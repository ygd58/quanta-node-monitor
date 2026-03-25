#!/usr/bin/env python3
import urllib.request, json, time, os, sys
BASE_URL = "http://localhost:3000"
def fetch(p):
    try:
        with urllib.request.urlopen(BASE_URL+p,timeout=5) as r:
            return json.loads(r.read())
    except: return None
def fetch_post(path,data):
    try:
        pl=json.dumps(data).encode()
        req=urllib.request.Request(BASE_URL+path,data=pl,headers={"Content-Type":"application/json"})
        with urllib.request.urlopen(req,timeout=5) as r:
            return json.loads(r.read())
    except: return None
def clear(): os.system("clear")
def fq(m): return f"{m/1e8:.2f}" if m else "0.00"
def fu(s):
    if not s: return "--"
    return f"{s//3600}s {(s%3600)//60}d {s%60}sn"
def fd(d):
    if not d: return "--"
    if d>=1e9: return f"{d/1e9:.1f}G"
    if d>=1e6: return f"{d/1e6:.1f}M"
    if d>=1e3: return f"{d/1e3:.1f}K"
    return str(d)
def draw():
    h=fetch("/health"); s=fetch("/api/stats"); p=fetch("/api/peers")
    clear()
    print("[96m" + "="*60 + "[0m")
    print("[96m  QUANTACHAIN NODE MONITOR // TESTNET ALPHA V2[0m")
    print("[96m" + "="*60 + "[0m")
    if not h and not s:
        print("[91m  BAGLANILAMADI -- localhost:3000[0m")
        return
    st = h.get("status","?") if h else "?"
    sc = "[92mSAGLIKLI[0m" if st=="healthy" else "[91mSORUNLU[0m"
    print(f"  {sc}   Uptime: {fu(h.get("uptime_seconds") if h else 0)}   {time.strftime("%H:%M:%S")}")
    print("[96m" + "-"*60 + "[0m")
    if s:
        ch=(h or {}).get("chain_height",s.get("chain_length",0))
        pc=(h or {}).get("connected_peers",0)
        mem=(h or {}).get("mempool_size",s.get("pending_transactions",0))
        mr=s.get("mining_reward",0)
        ts=s.get("total_supply",0)
        di=s.get("current_difficulty",0)
        daily=(mr/1e8)*2*60*24
        print(f"  Zincir Yuksekligi : [96m{ch}[0m blok")
        print(f"  Bagli Peer        : [93m{pc}[0m")
        print(f"  Mempool           : {mem} islem")
        print(f"  Mining Odulu      : [96m{fq(mr)}[0m QUA/blok")
        print(f"  Toplam Arz        : [92m{fq(ts)}[0m QUA")
        print(f"  Zorluk            : [93m{fd(di)}[0m")
        print(f"  Gunluk Tahmini    : [92m{daily:.0f}[0m QUA")
        print(f"  Yillik Tahmini    : [92m{daily*365:.0f}[0m QUA")
    print("[96m" + "-"*60 + "[0m")
    print("  PEER BAGLANTILARI")
    if p and p.get("peers"):
        for x in p["peers"]:
            print(f"  > {x.get("address","?"):<22} blok:{x.get("height",0):<6} sure:{fu(x.get("connected_for"))}")
    else: print("  Bagli peer yok")
    print("[96m" + "="*60 + "[0m")
    print("[90m  [Q]Cikis [B]Bakiye [R]Yenile -- 10sn otomatik[0m")
def bq():
    addr=input("  Cuzdan adresi: ").strip()
    if not addr: return
    d=fetch_post("/api/balance",{"address":addr})
    bal=d.get("balance_microunits",d.get("balance",0)) if d else 0
    print(f"[92m  Bakiye: {fq(bal)} QUA[0m")
    input("  [Enter] devam...")
def main():
    import tty,termios,select
    fd=sys.stdin.fileno(); old=termios.tcgetattr(fd); last=0
    try:
        tty.setcbreak(fd)
        while True:
            if time.time()-last>=10: draw(); last=time.time()
            r,_,_=select.select([sys.stdin],[],[],0.5)
            if r:
                ch=sys.stdin.read(1).lower()
                if ch=="q": break
                elif ch=="b":
                    termios.tcsetattr(fd,termios.TCSADRAIN,old)
                    bq(); tty.setcbreak(fd); draw(); last=time.time()
                elif ch=="r": draw(); last=time.time()
    except KeyboardInterrupt: pass
    finally:
        termios.tcsetattr(fd,termios.TCSADRAIN,old)
        clear(); print("Monitor kapatildi.")
if __name__=="__main__": main()