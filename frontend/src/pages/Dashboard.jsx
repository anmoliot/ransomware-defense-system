import { useThreatStore } from '../store/useThreatStore';
import Card, { CardHeader, MetricValue } from '../components/common/Card';
import SystemHealthCard from '../components/system/SystemHealthCard';
import RiskMeter from '../components/system/RiskMeter';
import StatusIndicators from '../components/system/StatusIndicators';
import ThreatForecastChart from '../components/threat/ThreatForecastChart';
import ThreatTimeline from '../components/threat/ThreatTimeline';
import ActivityGraph from '../components/threat/ActivityGraph';
import SuspiciousLogTable from '../components/logs/SuspiciousLogTable';
import AlertList from '../components/logs/AlertList';
import ResponsePanel from '../components/response/ResponsePanel';

function StatCard({ label, value, unit, color, sub, accentStyle }) {
  return (
    <div style={{
      background: 'var(--bg-panel)',
      border: '1px solid var(--border-dim)',
      borderRadius: 'var(--radius-lg)',
      padding: '14px 16px',
      position: 'relative',
      overflow: 'hidden',
      ...(accentStyle || {}),
    }}>
      <div style={{
        fontFamily: 'var(--font-mono)',
        fontSize: 9,
        color: 'var(--text-muted)',
        letterSpacing: '0.12em',
        textTransform: 'uppercase',
        marginBottom: 6,
      }}>{label}</div>
      <MetricValue value={value} unit={unit} color={color} size="lg" />
      {sub && (
        <div style={{
          fontFamily: 'var(--font-mono)',
          fontSize: 10,
          color: 'var(--text-muted)',
          marginTop: 4,
        }}>{sub}</div>
      )}
    </div>
  );
}

export default function Dashboard() {
  const { riskScore, monitoredFiles, anomaliesDetected, entropySpikes, canaryTrips, blockedProcesses, threatLevel } = useThreatStore();

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>

      {/* KPI Row */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(6, 1fr)', gap: 10 }}>
        <StatCard
          label="Risk Score"
          value={riskScore}
          unit="/100"
          color={riskScore > 70 ? 'var(--red-bright)' : riskScore > 45 ? 'var(--amber-bright)' : 'var(--green-bright)'}
          accentStyle={{ borderTop: `2px solid ${riskScore > 70 ? 'var(--red-bright)' : riskScore > 45 ? 'var(--amber-bright)' : 'var(--green-bright)'}` }}
        />
        <StatCard label="Files Monitored" value={monitoredFiles.toLocaleString()} color="var(--blue-bright)" sub="Active watch" />
        <StatCard label="Anomalies" value={anomaliesDetected} color={anomaliesDetected > 5 ? 'var(--red-bright)' : 'var(--amber-bright)'} sub="Last 24h" />
        <StatCard label="Entropy Spikes" value={entropySpikes} color={entropySpikes > 2 ? 'var(--red-bright)' : 'var(--amber-bright)'} sub="Above threshold" />
        <StatCard label="Canary Trips" value={canaryTrips} color={canaryTrips > 0 ? 'var(--red-bright)' : 'var(--green-bright)'} sub={canaryTrips > 0 ? '⚠ Detected' : 'All clear'} />
        <StatCard label="Blocked PIDs" value={blockedProcesses} color={blockedProcesses > 0 ? 'var(--red-bright)' : 'var(--text-secondary)'} sub="Auto-terminated" />
      </div>

      {/* Main Content Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 14 }}>

        {/* Left Column */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          {/* Risk Meter + Indicators */}
          <Card>
            <CardHeader title="Threat Level" subtitle="Current risk assessment" icon="⬡" />
            <div style={{ display: 'flex', justifyContent: 'center', marginBottom: 14 }}>
              <RiskMeter />
            </div>
            <StatusIndicators />
          </Card>
          <SystemHealthCard />
        </div>

        {/* Center Column */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          <ThreatForecastChart />
          <ActivityGraph />
          <ThreatTimeline />
        </div>

        {/* Right Column */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
          <ResponsePanel />
          <AlertList />
        </div>
      </div>

      {/* Full width log table */}
      <SuspiciousLogTable />

    </div>
  );
}