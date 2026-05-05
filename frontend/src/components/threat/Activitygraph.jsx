import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell } from 'recharts';
import Card, { CardHeader } from '../common/Card';

const generateData = () => Array.from({ length: 24 }, (_, i) => {
  const hour = String(i).padStart(2, '0');
  const val = Math.random() * 60 + 5;
  return {
    hour: `${hour}h`,
    entropy: parseFloat((Math.random() * 0.6 + 0.2).toFixed(2)),
    fileMods: Math.floor(val),
  };
});

const DATA = generateData();

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
      <div style={{ color: 'var(--amber-bright)' }}>Entropy: {payload[0]?.value}</div>
      <div style={{ color: 'var(--blue-bright)' }}>File Mods: {payload[1]?.value}</div>
    </div>
  );
};

export default function ActivityGraph() {
  return (
    <Card>
      <CardHeader title="24h Activity Profile" subtitle="Entropy + modification rate" icon="◈" />
      <ResponsiveContainer width="100%" height={160}>
        <BarChart data={DATA} margin={{ top: 4, right: 4, bottom: 0, left: -24 }} barSize={8} barGap={1}>
          <XAxis
            dataKey="hour"
            tick={{ fill: 'var(--text-muted)', fontSize: 9, fontFamily: 'JetBrains Mono' }}
            tickLine={false}
            axisLine={false}
            interval={3}
          />
          <YAxis
            tick={{ fill: 'var(--text-muted)', fontSize: 9, fontFamily: 'JetBrains Mono' }}
            tickLine={false}
            axisLine={false}
          />
          <Tooltip content={<CustomTooltip />} />
          <Bar dataKey="entropy" radius={[2, 2, 0, 0]}>
            {DATA.map((d, i) => (
              <Cell key={i} fill={d.entropy > 0.7 ? 'var(--red-bright)' : d.entropy > 0.5 ? 'var(--amber-bright)' : 'rgba(255,170,51,0.4)'} />
            ))}
          </Bar>
          <Bar dataKey="fileMods" radius={[2, 2, 0, 0]} fill="rgba(77,159,255,0.35)" />
        </BarChart>
      </ResponsiveContainer>
    </Card>
  );
}