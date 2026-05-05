import { create } from 'zustand';

const generateHistory = () => {
  const now = Date.now();
  return Array.from({ length: 30 }, (_, i) => ({
    time: new Date(now - (29 - i) * 60000).toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute: '2-digit' }),
    score: Math.floor(Math.random() * 40 + 10),
    events: Math.floor(Math.random() * 15),
  }));
};

export const useThreatStore = create((set, get) => ({
  threatLevel: 'MEDIUM',
  riskScore: 42,
  monitoredFiles: 14872,
  anomaliesDetected: 7,
  entropySpikes: 3,
  canaryTrips: 1,
  threatHistory: generateHistory(),
  blockedProcesses: 2,
  networkIsolated: false,

  setThreatLevel: (level) => set({ threatLevel: level }),
  setRiskScore: (score) => set({ riskScore: score }),

  simulateThreat: () => {
    const score = Math.floor(Math.random() * 60 + 40);
    const level = score > 80 ? 'CRITICAL' : score > 60 ? 'HIGH' : score > 40 ? 'MEDIUM' : 'LOW';
    set(state => ({
      riskScore: score,
      threatLevel: level,
      anomaliesDetected: state.anomaliesDetected + Math.floor(Math.random() * 3 + 1),
      entropySpikes: state.entropySpikes + 1,
      threatHistory: [
        ...state.threatHistory.slice(1),
        {
          time: new Date().toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute: '2-digit' }),
          score,
          events: Math.floor(Math.random() * 20 + 5),
        }
      ]
    }));
  },

  isolateNetwork: () => set({ networkIsolated: true, threatLevel: 'CRITICAL' }),
  restoreNetwork: () => set({ networkIsolated: false }),
}));