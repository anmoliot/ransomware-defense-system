import { useThreatStore } from '../../store/useThreatStore';

const indicators = [
  { key: 'ml_model', label: 'ML Model', desc: 'Behavioral Analysis' },
  { key: 'file_monitor', label: 'File Monitor', desc: 'inotify / FSEvent' },
  { key: 'canary_system', label: 'Canary System', desc: 'Deception Layer' },
  { key: 'network_guard', label: 'Network Guard', desc: 'Isolation Ready' },
  { key: 'backup_service', label: 'Backup Service', desc: 'Snapshot Active' },
  { key: 'entropy_engine', label: 'Entropy Engine', desc: 'Chi-Square Analysis' },
];

export default function StatusIndicators() {
  const { networkIsolated } = useThreatStore();

  const statuses = {
    ml_model: 'ACTIVE',
    file_monitor: 'ACTIVE',
    canary_system: 'ACTIVE',
    network_guard: networkIsolated ? 'ISOLATED' : 'STANDBY',
    backup_service: 'ACTIVE',
    entropy_engine: 'ACTIVE',
  };

  const colorMap = { ACTIVE: 'var(--green-bright)', STANDBY: 'var(--amber-bright)', ISOLATED: 'var(--red-bright)', ERROR: 'var(--red-bright)' };
  const pulseMap = { ACTIVE: 'pulse-green 2s infinite', STANDBY: 'pulse-amber 1.5s infinite', ISOLATED: 'pulse-red 0.8s infinite' };

  return (
    <div style={{
      display: 'grid',
      gridTemplateColumns: 'repeat(3, 1fr)',
      gap: 8,
    }}>
      {indicators.map(ind => {
        const status = statuses[ind.key];
        const color = colorMap[status] || 'var(--text-muted)';
        return (
          <div key={ind.key} style={{
            background: 'var(--bg-elevated)',
            border: '1px solid var(--border-dim)',
            borderRadius: 'var(--radius-md)',
            padding: '10px 12px',
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 4 }}>
              <div style={{
                width: 6,
                height: 6,
                borderRadius: '50%',
                background: color,
                animation: pulseMap[status] || 'none',
                flexShrink: 0,
              }} />
              <span style={{
                fontFamily: 'var(--font-mono)',
                fontSize: 9,
                fontWeight: 600,
                color,
                letterSpacing: '0.08em',
              }}>{status}</span>
            </div>
            <div style={{
              fontFamily: 'var(--font-display)',
              fontSize: 12,
              fontWeight: 600,
              color: 'var(--text-primary)',
            }}>{ind.label}</div>
            <div style={{
              fontFamily: 'var(--font-mono)',
              fontSize: 9,
              color: 'var(--text-muted)',
              marginTop: 1,
            }}>{ind.desc}</div>
          </div>
        );
      })}
    </div>
  );
}