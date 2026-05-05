import { useState } from 'react';
import Card, { CardHeader } from '../common/Card';
import Button from '../common/Button';
import { useThreatStore } from '../../store/useThreatStore';
import { useAlertStore } from '../../store/useAlertStore';

const ACTIONS = [
  {
    id: 'isolate',
    label: 'Isolate Network',
    desc: 'Disconnect device from network immediately',
    variant: 'danger',
    icon: '⊘',
    confirm: true,
    confirmMsg: 'This will disconnect the device from the network. Continue?',
  },
  {
    id: 'kill_processes',
    label: 'Kill Suspicious',
    desc: 'Terminate all flagged processes',
    variant: 'danger',
    icon: '✕',
    confirm: true,
    confirmMsg: 'Kill all processes with HIGH/CRITICAL anomaly score?',
  },
  {
    id: 'snapshot',
    label: 'Create Snapshot',
    desc: 'Emergency backup of protected folders',
    variant: 'warning',
    icon: '⟳',
    confirm: false,
  },
  {
    id: 'protect_folders',
    label: 'Lock Protected',
    desc: 'Enable write-lock on critical folders',
    variant: 'primary',
    icon: '⬡',
    confirm: false,
  },
  {
    id: 'deploy_canaries',
    label: 'Deploy Canaries',
    desc: 'Place new canary files across filesystem',
    variant: 'default',
    icon: '◇',
    confirm: false,
  },
  {
    id: 'full_scan',
    label: 'Full System Scan',
    desc: 'Re-baseline behavioral model',
    variant: 'default',
    icon: '◈',
    confirm: false,
  },
];

export default function ResponsePanel() {
  const [executing, setExecuting] = useState(null);
  const [executed, setExecuted] = useState(new Set());
  const [confirmAction, setConfirmAction] = useState(null);
  const { isolateNetwork, networkIsolated, simulateThreat } = useThreatStore();
  const { addAlert } = useAlertStore();

  const execute = async (actionId) => {
    setExecuting(actionId);
    await new Promise(r => setTimeout(r, 1200));

    if (actionId === 'isolate') {
      isolateNetwork();
      addAlert({
        severity: 'HIGH',
        type: 'RESPONSE',
        message: 'Network isolation executed — device disconnected from network',
        process: 'RDSYS_RESPONSE',
        pid: 0,
        path: 'N/A',
      });
    }

    setExecuted(prev => new Set([...prev, actionId]));
    setExecuting(null);
    setConfirmAction(null);
  };

  const handleClick = (action) => {
    if (action.confirm) {
      setConfirmAction(action);
    } else {
      execute(action.id);
    }
  };

  return (
    <>
      <Card>
        <CardHeader
          title="Response Controls"
          subtitle="Automated + manual response"
          icon="◎"
          action={
            <button
              onClick={simulateThreat}
              style={{
                padding: '3px 8px',
                background: 'var(--red-surface)',
                border: '1px solid rgba(255,59,59,0.2)',
                borderRadius: 4,
                color: 'var(--red-bright)',
                fontFamily: 'var(--font-mono)',
                fontSize: 9,
                cursor: 'pointer',
                letterSpacing: '0.06em',
              }}
            >SIM ATTACK</button>
          }
        />

        {networkIsolated && (
          <div style={{
            padding: '8px 12px',
            background: 'var(--red-surface-strong)',
            border: '1px solid rgba(255,59,59,0.3)',
            borderRadius: 'var(--radius-md)',
            marginBottom: 12,
            display: 'flex',
            alignItems: 'center',
            gap: 8,
          }}>
            <div style={{
              width: 7,
              height: 7,
              borderRadius: '50%',
              background: 'var(--red-bright)',
              animation: 'pulse-red 0.8s infinite',
              flexShrink: 0,
            }} />
            <span style={{
              fontFamily: 'var(--font-mono)',
              fontSize: 11,
              color: 'var(--red-bright)',
              fontWeight: 600,
            }}>NETWORK ISOLATED — DEVICE QUARANTINED</span>
          </div>
        )}

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
          {ACTIONS.map(action => {
            const done = executed.has(action.id);
            const running = executing === action.id;
            return (
              <button
                key={action.id}
                onClick={() => !done && !running && handleClick(action)}
                disabled={running}
                style={{
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'flex-start',
                  gap: 3,
                  padding: '10px 12px',
                  background: done ? 'var(--green-surface)' : running ? 'var(--bg-active)' : 'var(--bg-elevated)',
                  border: `1px solid ${done ? 'rgba(34,217,122,0.2)' : running ? 'var(--border-default)' : 'var(--border-dim)'}`,
                  borderRadius: 'var(--radius-md)',
                  cursor: done ? 'default' : running ? 'wait' : 'pointer',
                  transition: 'all var(--transition)',
                  textAlign: 'left',
                }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: 6, width: '100%' }}>
                  <span style={{ fontSize: 12, color: done ? 'var(--green-bright)' : 'var(--text-secondary)' }}>
                    {done ? '✓' : running ? '⟳' : action.icon}
                  </span>
                  <span style={{
                    fontFamily: 'var(--font-mono)',
                    fontSize: 11,
                    fontWeight: 600,
                    color: done ? 'var(--green-bright)' : 'var(--text-primary)',
                    letterSpacing: '0.04em',
                  }}>{running ? 'Executing...' : done ? 'Done' : action.label}</span>
                </div>
                <span style={{
                  fontFamily: 'var(--font-mono)',
                  fontSize: 9,
                  color: 'var(--text-muted)',
                  lineHeight: 1.3,
                }}>{action.desc}</span>
              </button>
            );
          })}
        </div>
      </Card>

      {/* Confirm Modal */}
      {confirmAction && (
        <div style={{
          position: 'fixed',
          inset: 0,
          background: 'rgba(6,8,16,0.85)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 1000,
        }} onClick={() => setConfirmAction(null)}>
          <div
            onClick={e => e.stopPropagation()}
            style={{
              background: 'var(--bg-elevated)',
              border: '1px solid rgba(255,59,59,0.3)',
              borderRadius: 'var(--radius-xl)',
              padding: 24,
              maxWidth: 360,
              width: '90%',
              animation: 'slide-in-up 0.2s ease',
            }}
          >
            <div style={{
              fontFamily: 'var(--font-mono)',
              fontSize: 10,
              color: 'var(--red-bright)',
              letterSpacing: '0.12em',
              textTransform: 'uppercase',
              marginBottom: 8,
            }}>⚠ Confirm Action</div>
            <div style={{
              fontFamily: 'var(--font-display)',
              fontSize: 16,
              fontWeight: 600,
              color: 'var(--text-primary)',
              marginBottom: 8,
            }}>{confirmAction.label}</div>
            <div style={{
              fontFamily: 'var(--font-mono)',
              fontSize: 12,
              color: 'var(--text-secondary)',
              marginBottom: 20,
              lineHeight: 1.5,
            }}>{confirmAction.confirmMsg}</div>
            <div style={{ display: 'flex', gap: 8, justifyContent: 'flex-end' }}>
              <Button variant="ghost" onClick={() => setConfirmAction(null)}>Cancel</Button>
              <Button variant="danger" onClick={() => execute(confirmAction.id)}>
                Execute
              </Button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}