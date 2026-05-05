import { NavLink } from 'react-router-dom';

const NAV_ITEMS = [
  { path: '/', label: 'Dashboard', icon: '⬡' },
  { path: '/threats', label: 'Threat Intel', icon: '◈' },
  { path: '/alerts', label: 'Alerts', icon: '◎', badge: 3 },
  { path: '/logs', label: 'Activity Logs', icon: '≡' },
  { path: '/decoys', label: 'Decoy Network', icon: '◇' },
  { path: '/recovery', label: 'Recovery', icon: '⟳' },
  { path: '/settings', label: 'Settings', icon: '⚙' },
];

const navLinkStyle = ({ isActive }) => ({
  display: 'flex',
  alignItems: 'center',
  gap: 10,
  padding: '8px 12px',
  borderRadius: 'var(--radius-md)',
  textDecoration: 'none',
  color: isActive ? 'var(--text-primary)' : 'var(--text-secondary)',
  background: isActive ? 'var(--bg-active)' : 'transparent',
  borderLeft: isActive ? '2px solid var(--blue-bright)' : '2px solid transparent',
  fontSize: 13,
  fontWeight: isActive ? 500 : 400,
  transition: 'all var(--transition)',
});

export default function Sidebar() {
  return (
    <aside style={{
      width: 'var(--sidebar-w)',
      height: '100%',
      background: 'var(--bg-deep)',
      borderRight: '1px solid var(--border-dim)',
      display: 'flex',
      flexDirection: 'column',
      flexShrink: 0,
      zIndex: 10,
    }}>
      <div style={{ height: 'var(--topbar-h)', display: 'flex', alignItems: 'center', gap: 10, padding: '0 20px', borderBottom: '1px solid var(--border-dim)' }}>
        <div style={{ width: 28, height: 28, background: 'linear-gradient(135deg, var(--red-bright), var(--amber-bright))', borderRadius: 6, display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 14, flexShrink: 0 }}>🛡</div>
        <div>
          <div style={{ fontFamily: 'var(--font-display)', fontWeight: 800, fontSize: 13, color: 'var(--text-primary)' }}>RDSYS</div>
          <div style={{ fontFamily: 'var(--font-mono)', fontSize: 9, color: 'var(--text-muted)', letterSpacing: '0.12em', textTransform: 'uppercase' }}>Defense v2.4</div>
        </div>
      </div>

      <nav style={{ flex: 1, padding: '12px 8px', display: 'flex', flexDirection: 'column', gap: 2 }}>
        {NAV_ITEMS.map(item => (
          <NavLink key={item.path} to={item.path} end={item.path === '/'} style={navLinkStyle}>
            <span style={{ fontSize: 16, width: 18, textAlign: 'center', flexShrink: 0 }}>{item.icon}</span>
            <span style={{ flex: 1 }}>{item.label}</span>
            {item.badge && (
              <span style={{ background: 'var(--red-bright)', color: '#fff', fontSize: 10, fontWeight: 600, fontFamily: 'var(--font-mono)', padding: '1px 6px', borderRadius: 10 }}>
                {item.badge}
              </span>
            )}
          </NavLink>
        ))}
      </nav>

      <div style={{ padding: '12px 8px 16px', borderTop: '1px solid var(--border-dim)' }}>
        <div style={{ padding: '10px 12px', background: 'var(--green-surface)', border: '1px solid rgba(34,217,122,0.15)', borderRadius: 'var(--radius-md)' }}>
          <div style={{ fontFamily: 'var(--font-mono)', fontSize: 9, color: 'var(--text-muted)', letterSpacing: '0.1em', textTransform: 'uppercase', marginBottom: 4 }}>System Status</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <div style={{ width: 6, height: 6, borderRadius: '50%', background: 'var(--green-bright)', animation: 'pulse-green 2s infinite', flexShrink: 0 }} />
            <span style={{ fontFamily: 'var(--font-mono)', fontSize: 11, color: 'var(--green-bright)', fontWeight: 500 }}>MONITORING ACTIVE</span>
          </div>
        </div>
      </div>
    </aside>
  );
}