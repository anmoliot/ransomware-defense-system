import { Outlet } from 'react-router-dom';
import Sidebar from './Sidebar';
import Topbar from './Topbar';

export default function MainLayout() {
  return (
    <div style={{ display: 'flex', height: '100vh', position: 'relative', zIndex: 1 }}>
      <Sidebar />
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', minWidth: 0, overflow: 'hidden' }}>
        <Topbar />
        <main style={{
          flex: 1,
          overflow: 'auto',
          padding: 20,
          background: 'var(--bg-void)',
        }}>
          <Outlet />
        </main>
      </div>
    </div>
  );
}