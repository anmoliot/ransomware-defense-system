import { create } from 'zustand';

const MOCK_ALERTS = [
  {
    id: 'a1',
    severity: 'HIGH',
    type: 'ENTROPY_SPIKE',
    message: 'High entropy detected in /home/user/documents — possible encryption in progress',
    process: 'suspicious_proc.exe',
    pid: 4821,
    path: '/home/user/documents/',
    timestamp: new Date(Date.now() - 120000).toISOString(),
    acknowledged: false,
  },
  {
    id: 'a2',
    severity: 'CRITICAL',
    type: 'CANARY_TRIP',
    message: 'Canary file modified — ransomware signature detected',
    process: 'svchost.exe',
    pid: 1024,
    path: 'C:\\Users\\Admin\\canary_doc.docx',
    timestamp: new Date(Date.now() - 45000).toISOString(),
    acknowledged: false,
  },
  {
    id: 'a3',
    severity: 'MEDIUM',
    type: 'RAPID_FILE_MOD',
    message: 'Abnormal file modification rate: 340 files/min in /var/data/',
    process: 'python3',
    pid: 9823,
    path: '/var/data/',
    timestamp: new Date(Date.now() - 300000).toISOString(),
    acknowledged: false,
  },
  {
    id: 'a4',
    severity: 'LOW',
    type: 'ANOMALY_SCORE',
    message: 'Behavioral anomaly score exceeded threshold (0.87)',
    process: 'notepad.exe',
    pid: 7650,
    path: 'C:\\Temp\\',
    timestamp: new Date(Date.now() - 600000).toISOString(),
    acknowledged: true,
  },
];

export const useAlertStore = create((set, get) => ({
  alerts: MOCK_ALERTS,
  activeAlerts: MOCK_ALERTS.filter(a => !a.acknowledged).length,

  acknowledgeAlert: (id) => set(state => {
    const alerts = state.alerts.map(a => a.id === id ? { ...a, acknowledged: true } : a);
    return { alerts, activeAlerts: alerts.filter(a => !a.acknowledged).length };
  }),

  addAlert: (alert) => set(state => {
    const newAlert = { ...alert, id: Date.now().toString(), timestamp: new Date().toISOString(), acknowledged: false };
    const alerts = [newAlert, ...state.alerts];
    return { alerts, activeAlerts: alerts.filter(a => !a.acknowledged).length };
  }),

  clearAll: () => set(state => {
    const alerts = state.alerts.map(a => ({ ...a, acknowledged: true }));
    return { alerts, activeAlerts: 0 };
  }),
}));