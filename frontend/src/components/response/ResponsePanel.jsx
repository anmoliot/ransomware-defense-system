import { FiDownload, FiPauseCircle, FiSlash, FiSquare } from 'react-icons/fi'
import { useState } from 'react'

const actions = [
  [FiSlash, 'Isolate host', 'Ready'],
  [FiSquare, 'Kill process', 'Dry run'],
  [FiDownload, 'Export IOC', 'Queued'],
  [FiPauseCircle, 'Backup logs', 'Ready'],
]

function ResponsePanel() {
  const [lastAction, setLastAction] = useState('No action selected')

  return (
    <section className="panel">
      <div className="panel-heading">
        <div>
          <p className="eyebrow">SOAR Playbook</p>
          <h2>Ransomware containment</h2>
        </div>
      </div>
      <div className="response-actions">
        {actions.map(([Icon, label, status]) => (
          <button
            type="button"
            key={label}
            onClick={() => setLastAction(`${label} queued in dry-run mode`)}
            title={label}
          >
            <Icon />
            <span>{label}</span>
            <em>{status}</em>
          </button>
        ))}
      </div>
      <p className="action-status">{lastAction}</p>
      <div className="hunt-box">
        <span>Hunt Query</span>
        <code>process_name:powershell.exe and entropy &gt; 7</code>
      </div>
    </section>
  )
}

export default ResponsePanel
