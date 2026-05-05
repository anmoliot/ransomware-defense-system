import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import MainLayout from './layout/MainLayout';
import Dashboard from './pages/Dashboard';
import './styles/Theme.css';

const PlaceholderPage = ({ title }) => (
  <div style={{
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '60vh',
    gap: 12,
  }}>
    <div style={{
      fontFamily: 'var(--font-mono)',
      fontSize: 10,
      color: 'var(--text-muted)',
      letterSpacing: '0.12em',
      textTransform: 'uppercase',
    }}>MODULE</div>
    <div style={{
      fontFamily: 'var(--font-display)',
      fontSize: 24,
      fontWeight: 700,
      color: 'var(--text-primary)',
    }}>{title}</div>
    <div style={{
      fontFamily: 'var(--font-mono)',
      fontSize: 11,
      color: 'var(--text-muted)',
      padding: '6px 14px',
      background: 'var(--bg-elevated)',
      border: '1px solid var(--border-dim)',
      borderRadius: 'var(--radius-md)',
    }}>Coming soon — implemented by backend integration</div>
  </div>
);

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<MainLayout />}>
          <Route path="/" element={<Dashboard />} />
          <Route path="/threats" element={<PlaceholderPage title="Threat Intelligence" />} />
          <Route path="/alerts" element={<PlaceholderPage title="Alert Management" />} />
          <Route path="/logs" element={<PlaceholderPage title="Activity Logs" />} />
          <Route path="/decoys" element={<PlaceholderPage title="Decoy Network" />} />
          <Route path="/recovery" element={<PlaceholderPage title="Recovery Center" />} />
          <Route path="/settings" element={<PlaceholderPage title="Settings" />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}