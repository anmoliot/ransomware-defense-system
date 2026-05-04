import { useState } from 'react'
import {
  FiActivity,
  FiGitBranch,
  FiPlayCircle,
  FiSearch,
  FiShield,
  FiZap,
} from 'react-icons/fi'
import './App.css'
import ThreatGraph from './components/graph/ThreatGraph'
import ProcessTree from './components/graph/ProcessTree'
import AttackTimeline from './components/timeline/AttackTimeline'
import ResponsePanel from './components/response/ResponsePanel'

const graph = {
  nodes: [
    { id: 'user:analyst', label: 'analyst', type: 'user', x: 6, y: 42, risk: 10 },
    { id: 'process:powershell', label: 'powershell.exe', type: 'process', x: 27, y: 24, risk: 86 },
    { id: 'process:cmd', label: 'cmd.exe', type: 'process', x: 48, y: 42, risk: 72 },
    { id: 'network:smb', label: 'SMB 445', type: 'network', x: 70, y: 27, risk: 68 },
    { id: 'file:canary', label: 'salary.xlsx', type: 'file', x: 71, y: 61, risk: 96 },
    { id: 'ioc:c2', label: '203.0.113.99', type: 'ioc', x: 91, y: 42, risk: 92 },
  ],
  edges: [
    ['user:analyst', 'process:powershell', 'launch'],
    ['process:powershell', 'process:cmd', 'spawn'],
    ['process:cmd', 'network:smb', 'connect'],
    ['process:cmd', 'file:canary', 'modify'],
    ['network:smb', 'ioc:c2', 'match'],
  ],
}

const processTree = {
  name: 'explorer.exe',
  risk: 12,
  children: [
    {
      name: 'powershell.exe',
      risk: 86,
      children: [
        {
          name: 'cmd.exe',
          risk: 72,
          children: [{ name: 'encryptor.exe', risk: 98, children: [] }],
        },
      ],
    },
  ],
}

const timeline = [
  ['10:21', 'powershell.exe launched', 'Encoded command detected', 'warning'],
  ['10:22', 'cmd.exe spawned', 'Child process created from PowerShell', 'warning'],
  ['10:22', 'Canary triggered', 'salary.xlsx modified', 'critical'],
  ['10:23', 'SMB propagation', 'Outbound connection to port 445', 'critical'],
  ['10:24', 'Incident correlated', 'Ransomware Incident risk score 94', 'critical'],
]

function App() {
  const [activeView, setActiveView] = useState('Overview')
  const [interactionStatus, setInteractionStatus] = useState('Ready')

  return (
    <main className="soc-shell">
      <aside className="sidebar">
        <div className="brand">
          <FiShield />
          <span>Ransomware Defense</span>
        </div>
        <nav>
          {[
            [FiActivity, 'Overview'],
            [FiGitBranch, 'Correlation'],
            [FiSearch, 'Hunting'],
            [FiZap, 'Response'],
          ].map(([Icon, label]) => (
            <button
              className={activeView === label ? 'active' : ''}
              key={label}
              onClick={() => {
                setActiveView(label)
                setInteractionStatus(`${label} selected`)
              }}
              type="button"
            >
              <Icon /> {label}
            </button>
          ))}
        </nav>
      </aside>

      <section className="workspace">
        <header className="topbar">
          <div>
            <p className="eyebrow">Enterprise EDR/XDR Phase 3</p>
            <h1>SOC Attack Workbench</h1>
          </div>
          <div className="topbar-actions">
            <button
              className="interaction-test"
              onClick={() => setInteractionStatus('React click handler working')}
              type="button"
            >
              Interaction Test
            </button>
            <div className="status-pill critical">ATTACK · Risk 94</div>
          </div>
        </header>

        <div className="runtime-banner">{interactionStatus}</div>

        <section className="metrics-grid">
          <Metric icon={<FiActivity />} label="Incidents" value="7" note="3 critical" />
          <Metric icon={<FiGitBranch />} label="Correlated Signals" value="42" note="endpoint + network + IOC" />
          <Metric icon={<FiSearch />} label="Hunt Matches" value="19" note="PowerShell, entropy, SMB" />
          <Metric icon={<FiPlayCircle />} label="Playbooks" value="4" note="1 ready to execute" />
        </section>

        <section className="primary-grid">
          <ThreatGraph graph={graph} />
          <ProcessTree tree={processTree} />
        </section>

        <section className="secondary-grid">
          <AttackTimeline events={timeline} />
          <ResponsePanel />
        </section>
      </section>
    </main>
  )
}

function Metric({ icon, label, value, note }) {
  return (
    <article className="metric">
      <div className="metric-icon">{icon}</div>
      <div>
        <p>{label}</p>
        <strong>{value}</strong>
        <span>{note}</span>
      </div>
    </article>
  )
}

export default App
