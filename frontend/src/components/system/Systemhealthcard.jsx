import Card, { CardHeader } from '../common/Card';
import { useThreatStore } from '../../store/useThreatStore';

function StatRow({ label, value, color, bar, unit }) {
  return (
    <div style={{ marginBottom: 12 }}>
      <div style={{
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'baseline',
        marginBottom: 4,
      }}>
        <span style={{
          fontFamily: 'var(--font-mono)',
          fontSize: 10,
          color: 'var(--text-muted)',
          letterSpacing: '0.08em',
          textTransform: 'uppercase',
        }}>{label}</span>
        <span style={{
          fontFamily: 'var(--font-mono)',
          fontSize: 13,
          fontWeight: 600,
          color: color || 'var(--text-primary)',
        }}>{value}{unit && <span style={{ fontSize: 9, color: 'var(--text-muted)', marginLeft: 2 }}>{unit}</span>}</span>
      </div>
      {bar !== undefined && (
        <div style={{
          height: 3,
          background: 'var(--bg-elevated)',
          borderRadius: 2,
          overflow: 'hidden',
        }}>
          <div style={{
            width: `${Math.min(bar, 100)}%`,
            height: '100%',
            background: color || 'var(--blue-bright)',
            borderRadius: 2,
            transition: 'width 0.5s ease',
          }} />
        </div>
      )}
    </div>
  );
}

export default function SystemHealthCard() {
  const { monitoredFiles, anomaliesDetected, entropySpikes, canaryTrips, blockedProcesses } = useThreatStore();

  const healthScore = Math.max(0, 100 - anomaliesDetected * 8 - entropySpikes * 5 - canaryTrips * 15);

  return (
    <Card accent={healthScore < 50 ? 'red' : healthScore < 75 ? 'amber' : 'green'}>
      <CardHeader title="System Health" subtitle="Real-time metrics" icon="⬡" />

      <StatRow
        label="Health Score"
        value={healthScore}
        unit="%"
        color={healthScore > 75 ? 'var(--green-bright)' : healthScore > 50 ? 'var(--amber-bright)' : 'var(--red-bright)'}
        bar={healthScore}
      />
      <StatRow
        label="Files Monitored"
        value={monitoredFiles.toLocaleString()}
        color="var(--blue-bright)"
      />
      <StatRow
        label="Anomalies Detected"
        value={anomaliesDetected}
        color={anomaliesDetected > 5 ? 'var(--red-bright)' : 'var(--amber-bright)'}
      />
      <StatRow
        label="Entropy Spikes"
        value={entropySpikes}
        color={entropySpikes > 2 ? 'var(--red-bright)' : 'var(--amber-bright)'}
      />
      <StatRow
        label="Canary Trips"
        value={canaryTrips}
        color={canaryTrips > 0 ? 'var(--red-bright)' : 'var(--green-bright)'}
      />
      <StatRow
        label="Blocked Processes"
        value={blockedProcesses}
        color={blockedProcesses > 0 ? 'var(--red-bright)' : 'var(--text-secondary)'}
      />
    </Card>
  );
}