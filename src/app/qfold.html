import React, { useState, useEffect, useCallback } from 'react';
import { Play, Pause, Shield, Terminal as TermIcon, Cpu } from 'lucide-react';

// ============================================================================
// [ENCRYPTION_HEADER: RSA-4096 INITIALIZED]
// [SECURE_TUNNEL: ESTABLISHED // PROTOCOL: OMEGA-7]
// [MODULE_INIT: QUANTUM_FOLD_ENGINE_v2.1]
// [GEOMETRY_PROTO: 15-BIT_CONVOLUTIONAL_ACTIVE]
// [TONAL_GEOMETRY: ASCII_INTENSITY_MAP_LOCKED]
// ============================================================================

const GRID_DIMS = [12, 12, 16];
const CHAR_MAP = ['.', ',', '-', '~', ':', ';', '=', '+', '*', 'x', '#', '%', '@'];

const quantize15Bit = (r, g, b) => {
  const r5 = Math.floor((r / 255) * 31);
  const g5 = Math.floor((g / 255) * 31);
  const b5 = Math.floor((b / 255) * 31);
  return [Math.min(255, r5 * 8), Math.min(255, g5 * 8), Math.min(255, b5 * 8)];
};

const getMagmaColor = (t) => {
  const colors = [
    [0, 0, 4], [24, 12, 60], [87, 21, 126],
    [177, 50, 90], [241, 135, 56], [252, 253, 164]
  ];
  t = Math.max(0, Math.min(1, t));
  const idx = t * (colors.length - 1);
  const i = Math.floor(idx);
  const f = idx - i;
  if (i >= colors.length - 1) return quantize15Bit(...colors[colors.length - 1]);
  const c1 = colors[i];
  const c2 = colors[i + 1];
  return quantize15Bit(
    Math.round(c1[0] + (c2[0] - c1[0]) * f),
    Math.round(c1[1] + (c2[1] - c1[1]) * f),
    Math.round(c1[2] + (c2[2] - c1[2]) * f)
  );
};

export default function App() {
  const [grid, setGrid] = useState(null);
  const [isRunning, setIsRunning] = useState(false);
  const [sliceIndex, setSliceIndex] = useState(0);
  const [logs, setLogs] = useState([
    "[SYSTEM] BOOT SEQUENCE INITIATED...",
    "[SYSTEM] ALLOCATING 2304 QUBITS IN 4D MANIFOLD.",
    "[SECURITY] ENCRYPTION HEADERS INJECTED.",
    "[GEOMETRY] 15-BIT TONAL CONVOLUTION READY."
  ]);

  const addLog = (msg) => setLogs(prev => [...prev.slice(-5), msg]);

  const initSimulation = useCallback(() => {
    const newGrid = Array.from({ length: GRID_DIMS[0] }, () =>
      Array.from({ length: GRID_DIMS[1] }, () =>
        Array.from({ length: GRID_DIMS[2] }, () => {
          const r = Math.random() * 2 - 1;
          const i = Math.random() * 2 - 1;
          const norm = Math.sqrt(r * r + i * i) || 1;
          return { r: r / norm, i: i / norm };
        })
      )
    );
    setGrid(newGrid);
    addLog("[ENGINE] SIMULATION MATRIX RESET.");
  }, []);

  useEffect(() => { initSimulation(); }, [initSimulation]);

  const stepSimulation = useCallback(() => {
    setGrid(prev => {
      if (!prev) return prev;
      return prev.map((row, y) =>
        row.map((cell, x) =>
          cell.map((voxel, z) => {
            const left  = prev[y][(x - 1 + 12) % 12][z];
            const right = prev[y][(x + 1) % 12][z];
            const up    = prev[(y - 1 + 12) % 12][x][z];
            const down  = prev[(y + 1) % 12][x][z];

            const convR = voxel.r * 0.6 + (left.r + right.r + up.r + down.r) * 0.1;
            const convI = voxel.i * 0.6 + (left.i + right.i + up.i + down.i) * 0.1;

            const phase = (Math.random() - 0.5) * 0.5;
            const cos = Math.cos(phase);
            const sin = Math.sin(phase);

            let newR = convR * cos - convI * sin;
            let newI = convR * sin + convI * cos;

            const norm = Math.sqrt(newR * newR + newI * newI) || 1;
            return { r: newR / norm, i: newI / norm };
          })
        )
      );
    });
  }, []);

  useEffect(() => {
    if (!isRunning) return;
    const id = setInterval(stepSimulation, 100);
    return () => clearInterval(id);
  }, [isRunning, stepSimulation]);

  if (!grid) {
    return (
      <div className="min-h-screen bg-slate-950 flex items-center justify-center text-emerald-500 font-mono">
        INITIALIZING TENSOR CORE...
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-slate-950 text-slate-300 font-mono p-6 flex flex-col items-center">
      {/* HEADER */}
      <div className="w-full max-w-4xl border-b-2 border-emerald-800/50 pb-4 mb-6 flex justify-between items-end">
        <div>
          <h1 className="text-3xl font-black tracking-tighter text-emerald-500 flex items-center gap-3">
            <Shield className="w-8 h-8 text-emerald-400" />
            Q-FOLD ENGINE_
          </h1>
          <p className="text-xs text-emerald-700/80 mt-1">
            [SYS_STAT: OPERATIONAL] // [ENC_LVL: MAXIMUM] // [VOXEL_DEPTH: 15-BIT]
          </p>
        </div>
        <div className="text-right text-xs text-slate-500">
          <p>LOC: 0x8F9A.44V</p>
          <p className="text-emerald-600 animate-pulse">UPLINK ACTIVE</p>
        </div>
      </div>

      <div className="w-full max-w-4xl grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* CONTROLS + TUI LOG */}
        <div className="col-span-1 space-y-6">
          <div className="bg-slate-900 border border-slate-800 p-4 rounded-lg shadow-2xl relative overflow-hidden">
            <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-emerald-600 to-purple-600" />
            <h2 className="text-sm font-bold text-slate-400 mb-4 flex items-center gap-2">
              <Cpu className="w-4 h-4" /> COMMAND_UPLINK
            </h2>

            <button
              onClick={() => {
                setIsRunning(r => !r);
                addLog(isRunning ? "[ENGINE] SIMULATION PAUSED." : "[ENGINE] SIMULATION RUNNING...");
              }}
              className={`w-full flex items-center justify-center gap-2 py-2 px-4 rounded font-bold transition-all mb-6 ${
                isRunning
                  ? 'bg-red-900/50 text-red-400 border border-red-800/50'
                  : 'bg-emerald-900/50 text-emerald-400 border border-emerald-800/50'
              }`}
            >
              {isRunning ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4" />}
              {isRunning ? 'PAUSE' : 'EXECUTE'}
            </button>

            <div className="space-y-2">
              <div className="flex justify-between text-xs text-slate-400">
                <span>W-AXIS FOLD INDEX</span>
                <span className="text-emerald-400">Z: {sliceIndex}</span>
              </div>
              <input
                type="range"
                min="0"
                max="15"
                value={sliceIndex}
                onChange={(e) => setSliceIndex(+e.target.value)}
                className="w-full accent-emerald-500 bg-slate-800 rounded-lg appearance-none h-2 cursor-pointer"
              />
            </div>
          </div>

          {/* SECURE TERMINAL */}
          <div className="bg-black border border-slate-800 p-4 rounded-lg shadow-2xl text-xs">
            <h2 className="text-slate-500 mb-3 border-b border-slate-800 pb-2 flex items-center gap-2">
              <TermIcon className="w-4 h-4" /> SECURE_LOG
            </h2>
            <div className="space-y-1 h-32 flex flex-col justify-end">
              {logs.map((log, i) => (
                <div key={i} className={i === logs.length - 1 ? 'text-emerald-400' : 'text-slate-600'}>
                  &gt; {log}
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* VOXEL VIEW */}
        <div className="col-span-1 md:col-span-2 flex items-center justify-center bg-slate-900 border border-slate-800 rounded-lg p-6 relative">
          <div
            className="grid gap-[2px] bg-slate-950 border-2 border-slate-800 p-1"
            style={{ gridTemplateColumns: 'repeat(12, minmax(0, 1fr))' }}
          >
            {grid.map((row, y) =>
              row.map((cellCol, x) => {
                const voxel = cellCol[sliceIndex];
                const t = (voxel.r + 1) / 2;
                const rgb = getMagmaColor(t);
                const char = CHAR_MAP[Math.floor(t * (CHAR_MAP.length - 1))];

                return (
                  <div
                    key={`${y}-${x}`}
                    className="w-8 h-8 flex items-center justify-center text-[10px] font-black"
                    style={{
                      backgroundColor: `rgb(${rgb[0]},${rgb[1]},${rgb[2]})`,
                      color: t > 0.6 ? 'rgba(0,0,0,0.65)' : 'rgba(255,255,255,0.65)',
                      boxShadow: 'inset 0 0 0 1px rgba(0,0,0,0.25)'
                    }}
                    title={`Re: ${voxel.r.toFixed(3)} | Im: ${voxel.i.toFixed(3)}`}
                  >
                    {char}
                  </div>
                );
              })
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
