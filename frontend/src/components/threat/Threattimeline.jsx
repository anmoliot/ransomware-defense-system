import Card, { CardHeader } from '../common/Card';

const EVENTS = [
  { time: '14:32:01', type: 'CANARY_TRIP', msg: 'Canary file accessed — /decoys/doc_template.docx', severity: 'CRITICAL' },
  { time: '14:31:44', type: 'ENTROPY_SPIKE', msg: 'Entropy 0.94 detected in /home/user/Downloads', severity: 'HIGH' },
  { time: '14:31:12', type: 'RAPID_MOD', msg: '320 file modifications in 60s — pid:4821', severity: 'HIGH' },
  { time: '14:30:55', type: 'ANOMALY', msg: 'Behavioral anomaly score 0.87 exceeded threshold', severity: 'MEDIUM' },
  { time: '14:29:03', type: 'PROCESS', msg: 'Unknown process spawned: suspicious_proc.exe', severity: 'MEDIUM' },
  { time: '14:27:11', type: 'ACCESS', msg: 'Abnormal file access pattern in /var/backup/', severity: 'LOW' },
  { time: '14:25:30', type: 'SCAN', msg: 'System scan completed — baseline updated', severity: 'INFO' },
];

const SEV_COLORS = {
  CRITICAL: 'var(--red-bright)',
  HIGH: '#ff6b35',
  MEDIUM: 'var(--amber-bright)',
  LOW: 'var(--blue-bright)',
  INFO: 'var(--text-muted)',
};

const SEV_BG = {
  CRITICAL: 'rgba(255,59,59,0.08)',
  HIGH: 'rgba(255,107,53,0.06)',
  MEDIUM: 'rgba(255,170,51,0.06)',
  LOW: 'rgba(77,159,255,0.05)',
  INFO: 'transparent',
};

export default function ThreatTimeline() {
  return (
    <Card>
      <CardHeader title="Event Timeline" subtitle="Recent security events" icon="≡" />
      <div style={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
        {EVENTS.map((ev, i) => (
          <div key={i} style={{
            display: 'flex',
            alignItems: 'flex-start',
            gap: 10,
            padding: '8px 10px',
            background: SEV_BG[ev.severity],
            borderRadius: 'var(--radius-sm)',
            borderLeft: `2px solid ${SEV_COLORS[ev.severity]}`,
            animation: i === 0 ? 'slide-in-right 0.3s ease forwards' : 'none',
          }}>
            <span style={{
              fontFamily: 'var(--font-mono)',
              fontSize: 10,
              color: 'var(--text-muted)',
              whiteSpace: 'nowrap',
              paddingTop: 1,
            }}>{ev.time}</span>
            <div style={{ flex: 1, minWidth: 0 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 1 }}>
                <span style={{
                  fontFamily: 'var(--font-mono)',
                  fontSize: 9,
                  fontWeight: 600,
                  color: SEV_COLORS[ev.severity],
                  letterSpacing: '0.08em',
                }}>{ev.type}</span>
                <span style={{
                  fontFamily: 'var(--font-mono)',
                  fontSize: 9,
                  color: 'var(--text-muted)',
                  padding: '1px 5px',
                  background: 'var(--bg-elevated)',
                  borderRadius: 3,
                }}>{ev.severity}</span>
              </div>
              <div style={{
                fontFamily: 'var(--font-mono)',
                fontSize: 11,
                color: 'var(--text-secondary)',
                overflow: 'hidden',
                textOverflow: 'ellipsis',
                whiteSpace: 'nowrap',
              }}>{ev.msg}</div>
            </div>
          </div>
        ))}
      </div>
    </Card>
  );
}