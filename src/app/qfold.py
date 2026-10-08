#!/usr/bin/env python3
"""
Q-Fold Engine — Python edition (stdlib only).

# ============================================================================
# [ENCRYPTION_HEADER: RSA-4096 INITIALIZED]
# [SECURE_TUNNEL: ESTABLISHED // PROTOCOL: OMEGA-7]
# [GEOMETRY_PROTO: 15-BIT_CONVOLUTIONAL_ACTIVE]
# [TONAL_GEOMETRY: ASCII_INTENSITY_MAP_LOCKED]
# ============================================================================

Usage:
  python3 qfold.py            # ANSI terminal, 10 steps/sec, keys: space pause, q quit, +/- slice
  python3 qfold.py --serve    # open the same engine in a browser on http://127.0.0.1:8765
"""

from __future__ import annotations

import math
import os
import random
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

W, D = 12, 16
CHARS = list(".,-~:;=+*x#%@")
STOPS = [
    (0, 0, 4),
    (24, 12, 60),
    (87, 21, 126),
    (177, 50, 90),
    (241, 135, 56),
    (252, 253, 164),
]


def q15(v: float) -> int:
    return min(255, int((v / 255.0) * 31) * 8)


def magma(t: float) -> tuple[int, int, int]:
    t = max(0.0, min(1.0, t))
    idx = t * (len(STOPS) - 1)
    i = int(idx)
    f = idx - i
    if i >= len(STOPS) - 1:
        a = STOPS[-1]
        return q15(a[0]), q15(a[1]), q15(a[2])
    a, b = STOPS[i], STOPS[i + 1]
    return (
        q15(a[0] + (b[0] - a[0]) * f),
        q15(a[1] + (b[1] - a[1]) * f),
        q15(a[2] + (b[2] - a[2]) * f),
    )


def seed():
    grid = []
    for _y in range(W):
        row = []
        for _x in range(W):
            col = []
            for _z in range(D):
                r = random.uniform(-1, 1)
                i = random.uniform(-1, 1)
                n = math.hypot(r, i) or 1.0
                col.append((r / n, i / n))
            row.append(col)
        grid.append(row)
    return grid


def evolve(prev):
    nxt = []
    for y in range(W):
        row = []
        for x in range(W):
            col = []
            for z in range(D):
                vr, vi = prev[y][x][z]
                lr, li = prev[y][(x - 1) % W][z]
                rr, ri = prev[y][(x + 1) % W][z]
                ur, ui = prev[(y - 1) % W][x][z]
                dr, di = prev[(y + 1) % W][x][z]
                cr = vr * 0.6 + (lr + rr + ur + dr) * 0.1
                ci = vi * 0.6 + (li + ri + ui + di) * 0.1
                phase = (random.random() - 0.5) * 0.5
                c, s = math.cos(phase), math.sin(phase)
                nr = cr * c - ci * s
                ni = cr * s + ci * c
                n = math.hypot(nr, ni) or 1.0
                col.append((nr / n, ni / n))
            row.append(col)
        nxt.append(row)
    return nxt


def ansi_cell(ch: str, rgb: tuple[int, int, int]) -> str:
    r, g, b = rgb
    return f"\x1b[38;2;{r};{g};{b}m{ch}\x1b[0m"


def draw(grid, z: int, running: bool) -> None:
    lines = [
        "\x1b[2J\x1b[H",
        "\x1b[32mQ-FOLD ENGINE_\x1b[0m  python",
        f"[VOXEL: 15-BIT]  Z={z:02d}  {'RUNNING' if running else 'PAUSED'}",
        "space=pause  +/-=slice  q=quit",
        "",
    ]
    for y in range(W):
        row = []
        for x in range(W):
            vr, _vi = grid[y][x][z]
            t = (vr + 1) / 2
            rgb = magma(t)
            ch = CHARS[max(0, min(len(CHARS) - 1, int(t * (len(CHARS) - 1))))]
            row.append(ansi_cell(ch + ch, rgb))
        lines.append(" ".join(row))
    sys.stdout.write("\n".join(lines) + "\n")
    sys.stdout.flush()


def run_tui() -> None:
    grid = seed()
    z = 0
    running = True
    if os.name != "nt":
        import select
        import termios
        import tty

        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        tty.setcbreak(fd)
    else:
        select = None  # type: ignore
        old = None
        fd = None
    try:
        while True:
            if running:
                grid = evolve(grid)
            draw(grid, z, running)
            if os.name != "nt":
                ready, _, _ = select.select([sys.stdin], [], [], 0.1)
                if ready:
                    key = sys.stdin.read(1)
                    if key == "q":
                        break
                    if key == " ":
                        running = not running
                    if key in "+=":
                        z = (z + 1) % D
                    if key in "-_":
                        z = (z - 1) % D
            else:
                time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        if old is not None and fd is not None:
            import termios

            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        print("\n[ENGINE] HALT.")


PAGE = r"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Q-Fold (python)</title>
<style>
body{margin:0;background:#020617;color:#cbd5e1;font-family:ui-monospace,monospace;padding:16px}
h1{color:#34d399;font-size:22px} .grid{display:grid;grid-template-columns:repeat(12,28px);gap:2px}
.cell{width:28px;height:28px;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:900}
button{font:inherit;background:#022c22;color:#6ee7b7;border:1px solid #065f46;padding:8px 14px;border-radius:8px;cursor:pointer}
</style></head><body>
<h1>Q-FOLD ENGINE_ <small style="color:#64748b">served by qfold.py</small></h1>
<p style="font-size:12px;color:#047857">[VOXEL: 15-BIT] // python stdlib server</p>
<button id="run">EXECUTE</button>
<label> Z <input id="slice" type="range" min="0" max="15" value="0"></label>
<div id="grid" class="grid"></div>
<script>
const W=12,D=16,CHARS=[...".,-~:;=+*x#%@"];
const STOPS=[[0,0,4],[24,12,60],[87,21,126],[177,50,90],[241,135,56],[252,253,164]];
const q15=v=>Math.min(255,Math.floor((v/255)*31)*8);
function magma(t){t=Math.max(0,Math.min(1,t));const idx=t*(STOPS.length-1),i=Math.floor(idx),f=idx-i;
 const a=STOPS[Math.min(i,STOPS.length-1)],b=STOPS[Math.min(i+1,STOPS.length-1)];
 return [q15(a[0]+(b[0]-a[0])*f),q15(a[1]+(b[1]-a[1])*f),q15(a[2]+(b[2]-a[2])*f)];}
function seed(){const g=[];for(let y=0;y<W;y++){g[y]=[];for(let x=0;x<W;x++){g[y][x]=[];
 for(let z=0;z<D;z++){const r=Math.random()*2-1,i=Math.random()*2-1,n=Math.hypot(r,i)||1;g[y][x][z]={r:r/n,i:i/n};}}}return g;}
function evolve(p){const n=[];for(let y=0;y<W;y++){n[y]=[];for(let x=0;x<W;x++){n[y][x]=[];
 for(let z=0;z<D;z++){const v=p[y][x][z],L=p[y][(x-1+W)%W][z],R=p[y][(x+1)%W][z],U=p[(y-1+W)%W][x][z],Dn=p[(y+1)%W][x][z];
 const cR=v.r*0.6+(L.r+R.r+U.r+Dn.r)*0.1,cI=v.i*0.6+(L.i+R.i+U.i+Dn.i)*0.1,ph=(Math.random()-.5)*.5,c=Math.cos(ph),s=Math.sin(ph);
 let nR=cR*c-cI*s,nI=cR*s+cI*c,m=Math.hypot(nR,nI)||1;n[y][x][z]={r:nR/m,i:nI/m};}}}return n;}
let grid=seed(),on=false,timer=0;
const el=document.getElementById("grid");
function paint(){const z=+document.getElementById("slice").value;let h="";
 for(let y=0;y<W;y++)for(let x=0;x<W;x++){const t=(grid[y][x][z].r+1)/2,rgb=magma(t);
  const ch=CHARS[Math.max(0,Math.min(CHARS.length-1,Math.floor(t*(CHARS.length-1))))];
  h+=`<div class="cell" style="background:rgb(${rgb});color:${t>.6?"#000a":"#fffc"}">${ch}</div>`;}
 el.innerHTML=h;}
document.getElementById("run").onclick=()=>{on=!on;document.getElementById("run").textContent=on?"PAUSE":"EXECUTE";
 clearInterval(timer); if(on) timer=setInterval(()=>{grid=evolve(grid);paint();},100);};
document.getElementById("slice").oninput=paint; paint();
</script></body></html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):  # noqa: N802
        body = PAGE.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        return


def serve() -> None:
    port = 8765
    httpd = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"[ENGINE] serving http://127.0.0.1:{port}  (Ctrl-C to stop)")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[ENGINE] HALT.")


if __name__ == "__main__":
    if "--serve" in sys.argv:
        serve()
    else:
        run_tui()
