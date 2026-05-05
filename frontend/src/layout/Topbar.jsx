import { useState, useEffect } from 'react';
import { useAlertStore } from '../store/useAlertStore';
import { useThreatStore } from '../store/useThreatStore';

const THREAT_LEVELS = {
  LOW: { label: 'LOW', color: 'var(--green-bright)', bg: 'var(--green-surface)' },
  MEDIUM: { label: 'MED', color: 'var(--amber-bright)', bg: 'var(--amber-surface)' },
  HIGH: { label: 'HIGH', color: 'var(--red-bright)', bg: 'var(--red-surface)' },
  CRITICAL: { label: 'CRIT', color: 'var(--red-bright)', bg: 'var(--red-surface-strong)' },
};

export default function Topbar() {
  const [time, setTime] = useState(new Date());
  const [wsConnected, setWsConnected] = useState(true);
  const { threatLevel } = useThreatStore();
  const { activeAlerts } = useAlertStore();

  useEffect(() => {
    const t = setInterval(() => setTime(new Date()), 1000);
    return () => clearInterval(t);
  }, []);

  const level = THREAT_LEVELS[threatLevel] || THREAT_LEVELS.LOW;
  const isHighThreat = threatLevel === 'HIGH' || threatLevel === 'CRITICAL';

  return (
    <header style={{
      height: 'var(--topbar-h)',
      background: 'var(--bg-deep)',
      borderBottom: '1px solid var(--border-dim)',
      display: 'flex',
      alignItems: 'center',
      padding: '0 20px',
      gap: 16,
      position: 'relative',
      zIndex: 10,
      flexShrink: 0,
    }}>

      {/* Page title area */}
      <div style={{ flex: 1 }}>
        <div style={{
          fontFamily: 'var(--font-mono)',
          fontSize: 10,
          color: 'var(--text-muted)',
          letterSpacing: '0.12em',
          textTransform: 'uppercase',
          marginBottom: 1,
        }}>Intelligent Ransomware Defense System</div>
        <div style={{
          fontFamily: 'var(--font-display)',
          fontSize: 15,
          fontWeight: 600,
          color: 'var(--text-primary)',
        }}>Security Operations Center</div>
      </div>

      {/* Threat Level Indicator */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        gap: 8,
        padding: '6px 14px',
        background: level.bg,
        border: `1px solid ${level.color}33`,
        borderRadius: 'var(--radius-md)',
      }}>
        <div style={{
          width: 7,
          height: 7,
          borderRadius: '50%',
          background: level.color,
          animation: isHighThreat ? 'pulse-red 1s infinite' : 'pulse-green 2s infinite',
          flexShrink: 0,
        }} />
        <span style={{
          fontFamily: 'var(--font-mono)',
          fontSize: 10,
          color: 'var(--text-muted)',
          letterSpacing: '0.1em',
        }}>THREAT</span>
        <span style={{
          fontFamily: 'var(--font-mono)',
          fontSize: 12,
          fontWeight: 600,
          color: level.color,
          letterSpacing: '0.08em',
        }}>{level.label}</span>
      </div>

      {/* Active Alerts */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        gap: 8,
        padding: '6px 14px',
        background: activeAlerts > 0 ? 'var(--red-surface)' : 'var(--bg-surface)',
        border: `1px solid ${activeAlerts > 0 ? 'rgba(255,59,59,0.2)' : 'var(--border-dim)'}`,
        borderRadius: 'var(--radius-md)',
      }}>
        <span style={{ fontSize: 12 }}>◎</span>
        <span style={{
          fontFamily: 'var(--font-mono)',
          fontSize: 10,
          color: 'var(--text-muted)',
          letterSpacing: '0.1em',
        }}>ALERTS</span>
        <span style={{
          fontFamily: 'var(--font-mono)',
          fontSize: 13,
          fontWeight: 600,
          color: activeAlerts > 0 ? 'var(--red-bright)' : 'var(--text-secondary)',
        }}>{activeAlerts}</span>
      </div>

      {/* WS Connection */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        gap: 6,
        padding: '6px 12px',
        background: 'var(--bg-surface)',
        border: '1px solid var(--border-dim)',
        borderRadius: 'var(--radius-md)',
      }}>
        <div style={{
          width: 5,
          height: 5,
          borderRadius: '50%',
          background: wsConnected ? 'var(--green-bright)' : 'var(--red-bright)',
          animation: wsConnected ? 'pulse-green 2s infinite' : 'pulse-red 1s infinite',
        }} />
        <span style={{
          fontFamily: 'var(--font-mono)',
          fontSize: 10,
          color: 'var(--text-muted)',
          letterSpacing: '0.08em',
        }}>{wsConnected ? 'WS LIVE' : 'OFFLINE'}</span>
      </div>

      {/* Clock */}
      <div style={{
        fontFamily: 'var(--font-mono)',
        fontSize: 13,
        color: 'var(--text-secondary)',
        letterSpacing: '0.06em',
        minWidth: 72,
        textAlign: 'right',
      }}>
        {time.toLocaleTimeString('en-US', { hour12: false })}
      </div>
    </header>
  );
}