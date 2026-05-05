export const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';
export const WS_URL = import.meta.env.VITE_WS_URL || 'ws://localhost:8000/ws';

export const ENDPOINTS = {
  DETECT_STATUS: '/detect/status',
  DETECT_EVENT: '/detect/event',
  ALERTS: '/alerts',
  ALERT_ACK: (id) => `/alerts/${id}/ack`,
  RESPONSE_ISOLATE: '/response/isolate',
  RESPONSE_KILL: '/response/kill',
  RESPONSE_SNAPSHOT: '/response/snapshot',
  RESPONSE_CANARIES: '/response/canaries/deploy',
  RESPONSE_SCAN: '/response/scan',
};