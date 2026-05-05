export default function Card({ children, style = {}, accent, className }) {
  const accentColor = {
    red: 'var(--red-bright)',
    amber: 'var(--amber-bright)',
    green: 'var(--green-bright)',
    blue: 'var(--blue-bright)',
    cyan: 'var(--cyan-bright)',
  }[accent];

  return (
    <div
      className={className}
      style={{
        background: 'var(--bg-panel)',
        border: '1px solid var(--border-dim)',
        borderRadius: 'var(--radius-lg)',
        padding: '16px',
        position: 'relative',
        overflow: 'hidden',
        ...(accentColor && {
          borderTop: `2px solid ${accentColor}`,
        }),
        ...style,
      }}
    >
      {children}
    </div>
  );
}

export function CardHeader({ title, subtitle, action, icon }) {
  return (
    <div style={{
      display: 'flex',
      alignItems: 'flex-start',
      justifyContent: 'space-between',
      marginBottom: 14,
      gap: 8,
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
        {icon && (
          <span style={{ fontSize: 14, opacity: 0.7 }}>{icon}</span>
        )}
        <div>
          <div style={{
            fontFamily: 'var(--font-display)',
            fontSize: 13,
            fontWeight: 600,
            color: 'var(--text-primary)',
            letterSpacing: '0.02em',
          }}>{title}</div>
          {subtitle && (
            <div style={{
              fontFamily: 'var(--font-mono)',
              fontSize: 10,
              color: 'var(--text-muted)',
              letterSpacing: '0.08em',
              textTransform: 'uppercase',
              marginTop: 1,
            }}>{subtitle}</div>
          )}
        </div>
      </div>
      {action && <div>{action}</div>}
    </div>
  );
}

export function MetricValue({ value, unit, color = 'var(--text-primary)', size = 'md' }) {
  const sizes = { sm: 18, md: 24, lg: 32, xl: 42 };
  return (
    <div style={{ display: 'flex', alignItems: 'baseline', gap: 4 }}>
      <span style={{
        fontFamily: 'var(--font-mono)',
        fontSize: sizes[size],
        fontWeight: 600,
        color,
        lineHeight: 1,
      }}>{value}</span>
      {unit && (
        <span style={{
          fontFamily: 'var(--font-mono)',
          fontSize: 11,
          color: 'var(--text-muted)',
        }}>{unit}</span>
      )}
    </div>
  );
}