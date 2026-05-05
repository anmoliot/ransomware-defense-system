import { API_BASE } from './endpoints';

async function request(path, options = {}) {
  try {
    const res = await fetch(`${API_BASE}${path}`, {
      headers: { 'Content-Type': 'application/json', ...options.headers },
      ...options,
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error(`API error [${path}]:`, err);
    throw err;
  }
}

export const api = {
  // Detection
  getDetectionStatus: () => request('/detect/status'),
  postFileEvent: (data) => request('/detect/event', { method: 'POST', body: JSON.stringify(data) }),

  // Alerts
  getAlerts: (params = {}) => {
    const q = new URLSearchParams(params).toString();
    return request(`/alerts${q ? '?' + q : ''}`);
  },
  acknowledgeAlert: (id) => request(`/alerts/${id}/ack`, { method: 'POST' }),
  deleteAlert: (id) => request(`/alerts/${id}`, { method: 'DELETE' }),

  // Response
  isolateDevice: () => request('/response/isolate', { method: 'POST' }),
  killProcess: (pid) => request('/response/kill', { method: 'POST', body: JSON.stringify({ pid }) }),
  createSnapshot: () => request('/response/snapshot', { method: 'POST' }),
  deployCanaries: () => request('/response/canaries/deploy', { method: 'POST' }),
  runFullScan: () => request('/response/scan', { method: 'POST' }),
};