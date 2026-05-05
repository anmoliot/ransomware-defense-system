import {
  AreaChart, Area, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, ReferenceLine
} from 'recharts';
import { useThreatStore } from '../../store/useThreatStore';
import Card, { CardHeader } from '../common/Card';

const CustomTooltip = ({ active, payload, label }) => {
  if (!active || !payload?.length) return null;
  return (
    <div style={{
      background: 'var(--bg-elevated)',
      border: '1px solid var(--border-default)',
      borderRadius: 'var(--radius-md)',
      padding: '8px 12px',
      fontFamily: 'var(--font-mono)',
      fontSize: 11,
    }}>
      <div style={{ color: 'var(--text-muted)', marginBottom: 4 }}>{label}</div>
      <div style={{ color: 'var(--red-bright)' }}>Score: {payload[0]?.value}</div>
      <div style={{ color: 'var(--blue-bright)' }}>Events: {payload[1]?.value}</div>
    </div>
  );
};

export default function ThreatForecastChart() {
  const { threatHistory } = useThreatStore();
  const lastN = threatHistory.slice(-20);

  return (
    <Card>
      <CardHeader
        title="Threat Activity"
        subtitle="30-min rolling window"
        icon="◈"
        action={
          <span style={{
            fontFamily: 'var(--font-mono)',
            fontSize: 10,
            color: 'var(--text-muted)',
            padding: '3px 8px',
            background: 'var(--bg-elevated)',
            borderRadius: 4,
            border: '1px solid var(--border-dim)',
          }}>LIVE</span>
        }
      />
      <ResponsiveContainer width="100%" height={180}>
        <AreaChart data={lastN} margin={{ top: 4, right: 4, bottom: 0, left: -20 }}>
          <defs>
            <linearGradient id="scoreGrad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#ff3b3b" stopOpacity={0.3} />
              <stop offset="100%" stopColor="#ff3b3b" stopOpacity={0} />
            </linearGradient>
            <linearGradient id="eventGrad" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#4d9fff" stopOpacity={0.2} />
              <stop offset="100%" stopColor="#4d9fff" stopOpacity={0} />
            </linearGradient>
          </defs>
          <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" vertical={false} />
          <XAxis
            dataKey="time"
            tick={{ fill: 'var(--text-muted)', fontSize: 9, fontFamily: 'JetBrains Mono' }}
            tickLine={false}
            axisLine={false}
            interval={4}
          />
          <YAxis
            tick={{ fill: 'var(--text-muted)', fontSize: 9, fontFamily: 'JetBrains Mono' }}
            tickLine={false}
            axisLine={false}
          />
          <Tooltip content={<CustomTooltip />} />
          <ReferenceLine y={60} stroke="rgba(255,170,51,0.3)" strokeDasharray="4 4" />
          <ReferenceLine y={80} stroke="rgba(255,59,59,0.3)" strokeDasharray="4 4" />
          <Area
            type="monotone"
            dataKey="score"
            stroke="#ff3b3b"
            strokeWidth={1.5}
            fill="url(#scoreGrad)"
            dot={false}
            activeDot={{ r: 3, fill: '#ff3b3b' }}
          />
          <Area
            type="monotone"
            dataKey="events"
            stroke="#4d9fff"
            strokeWidth={1}
            fill="url(#eventGrad)"
            dot={false}
            activeDot={{ r: 3, fill: '#4d9fff' }}
          />
        </AreaChart>
      </ResponsiveContainer>
      <div style={{
        display: 'flex',
        gap: 16,
        marginTop: 10,
      }}>
        {[
          { label: 'Risk Score', color: 'var(--red-bright)' },
          { label: 'Events', color: 'var(--blue-bright)' },
          { label: 'Warning (60)', color: 'var(--amber-bright)', dashed: true },
          { label: 'Critical (80)', color: 'var(--red-bright)', dashed: true },
        ].map(item => (
          <div key={item.label} style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
            <div style={{
              width: item.dashed ? 14 : 10,
              height: 2,
              background: item.color,
              opacity: item.dashed ? 0.6 : 1,
              borderRadius: 1,
              borderTop: item.dashed ? `1px dashed ${item.color}` : 'none',
              flexShrink: 0,
            }} />
            <span style={{
              fontFamily: 'var(--font-mono)',
              fontSize: 9,
              color: 'var(--text-muted)',
            }}>{item.label}</span>
          </div>
        ))}
      </div>
    </Card>
  );
}