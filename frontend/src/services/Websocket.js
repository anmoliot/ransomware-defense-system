import { WS_URL } from './endpoints';
import { useThreatStore } from '../store/useThreatStore';
import { useAlertStore } from '../store/useAlertStore';

class WebSocketService {
  constructor() {
    this.ws = null;
    this.reconnectTimeout = null;
    this.reconnectDelay = 3000;
    this.maxDelay = 30000;
  }

  connect() {
    try {
      this.ws = new WebSocket(WS_URL);

      this.ws.onopen = () => {
        console.log('[WS] Connected');
        this.reconnectDelay = 3000;
      };

      this.ws.onmessage = (event) => {
        try {
          const msg = JSON.parse(event.data);
          this._handleMessage(msg);
        } catch (e) {
          console.error('[WS] Parse error:', e);
        }
      };

      this.ws.onclose = () => {
        console.log('[WS] Disconnected — reconnecting...');
        this._scheduleReconnect();
      };

      this.ws.onerror = (err) => {
        console.error('[WS] Error:', err);
        this.ws.close();
      };
    } catch (e) {
      console.error('[WS] Connection failed:', e);
      this._scheduleReconnect();
    }
  }

  _handleMessage(msg) {
    const { type, payload } = msg;
    const threatStore = useThreatStore.getState();
    const alertStore = useAlertStore.getState();

    switch (type) {
      case 'THREAT_UPDATE':
        threatStore.setThreatLevel(payload.level);
        threatStore.setRiskScore(payload.score);
        break;
      case 'NEW_ALERT':
        alertStore.addAlert(payload);
        break;
      case 'ANOMALY_DETECTED':
        // Update stats — handled by simulateThreat in mock mode
        break;
      default:
        console.log('[WS] Unknown message type:', type);
    }
  }

  _scheduleReconnect() {
    clearTimeout(this.reconnectTimeout);
    this.reconnectTimeout = setTimeout(() => {
      this.reconnectDelay = Math.min(this.reconnectDelay * 2, this.maxDelay);
      this.connect();
    }, this.reconnectDelay);
  }

  disconnect() {
    clearTimeout(this.reconnectTimeout);
    if (this.ws) {
      this.ws.close();
      this.ws = null;
    }
  }

  send(type, payload) {
    if (this.ws?.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify({ type, payload }));
    }
  }
}

export const wsService = new WebSocketService();