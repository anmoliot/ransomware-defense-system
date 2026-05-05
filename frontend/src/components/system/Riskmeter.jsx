import { useThreatStore } from '../../store/useThreatStore';

const LEVEL_CONFIG = {
  LOW: { color: '#22d97a', label: 'LOW RISK', glow: 'rgba(34,217,122,0.3)' },
  MEDIUM: { color: '#ffaa33', label: 'MODERATE', glow: 'rgba(255,170,51,0.3)' },
  HIGH: { color: '#ff6b35', label: 'HIGH RISK', glow: 'rgba(255,107,53,0.4)' },
  CRITICAL: { color: '#ff3b3b', label: 'CRITICAL', glow: 'rgba(255,59,59,0.5)' },
};

export default function RiskMeter() {
  const { riskScore, threatLevel } = useThreatStore();
  const config = LEVEL_CONFIG[threatLevel] || LEVEL_CONFIG.LOW;

  // SVG arc math
  const R = 60, cx = 80, cy = 80;
  const startAngle = -210;
  const totalArc = 240;
  const fillAngle = startAngle + (riskScore / 100) * totalArc;

  const toRad = deg => (deg * Math.PI) / 180;
  const arcPath = (start, end, r) => {
    const s = toRad(start), e = toRad(end);
    const x1 = cx + r * Math.cos(s), y1 = cy + r * Math.sin(s);
    const x2 = cx + r * Math.cos(e), y2 = cy + r * Math.sin(e);
    const large = end - start > 180 ? 1 : 0;
    return `M ${x1} ${y1} A ${r} ${r} 0 ${large} 1 ${x2} ${y2}`;
  };

  const ticks = Array.from({ length: 11 }, (_, i) => {
    const angle = toRad(-210 + i * 24);
    const r1 = 52, r2 = 57;
    return {
      x1: cx + r1 * Math.cos(angle), y1: cy + r1 * Math.sin(angle),
      x2: cx + r2 * Math.cos(angle), y2: cy + r2 * Math.sin(angle),
    };
  });

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: 4,
    }}>
      <svg width="160" height="140" viewBox="0 0 160 140">
        {/* Tick marks */}
        {ticks.map((t, i) => (
          <line key={i} x1={t.x1} y1={t.y1} x2={t.x2} y2={t.y2}
            stroke="var(--border-subtle)" strokeWidth={i % 5 === 0 ? 1.5 : 0.8} />
        ))}

        {/* Track */}
        <path d={arcPath(-210, 30, R)} fill="none"
          stroke="var(--bg-elevated)" strokeWidth={8} strokeLinecap="round" />

        {/* Fill arc */}
        {riskScore > 0 && (
          <path d={arcPath(-210, -210 + (riskScore / 100) * 240, R)} fill="none"
            stroke={config.color} strokeWidth={8} strokeLinecap="round"
            style={{ filter: `drop-shadow(0 0 6px ${config.glow})` }} />
        )}

        {/* Center score */}
        <text x={cx} y={cy - 6} textAnchor="middle" dominantBaseline="central"
          style={{ fontFamily: 'var(--font-mono)', fontSize: 26, fontWeight: 600, fill: config.color }}>
          {riskScore}
        </text>
        <text x={cx} y={cy + 14} textAnchor="middle"
          style={{ fontFamily: 'var(--font-mono)', fontSize: 9, fill: 'var(--text-muted)', letterSpacing: '0.08em' }}>
          RISK SCORE
        </text>

        {/* Level labels */}
        <text x={22} y={108} textAnchor="middle"
          style={{ fontFamily: 'var(--font-mono)', fontSize: 8, fill: 'var(--green-bright)', letterSpacing: '0.05em' }}>
          LOW
        </text>
        <text x={138} y={108} textAnchor="middle"
          style={{ fontFamily: 'var(--font-mono)', fontSize: 8, fill: 'var(--red-bright)', letterSpacing: '0.05em' }}>
          HIGH
        </text>
      </svg>

      <div style={{
        fontFamily: 'var(--font-display)',
        fontSize: 12,
        fontWeight: 700,
        color: config.color,
        letterSpacing: '0.12em',
        textTransform: 'uppercase',
      }}>{config.label}</div>
    </div>
  );
}