import { useState } from 'react';

const VARIANTS = {
  default: {
    background: 'var(--bg-elevated)',
    border: '1px solid var(--border-default)',
    color: 'var(--text-primary)',
    hover: 'var(--bg-hover)',
  },
  danger: {
    background: 'var(--red-surface)',
    border: '1px solid rgba(255,59,59,0.3)',
    color: 'var(--red-bright)',
    hover: 'rgba(255,59,59,0.15)',
  },
  success: {
    background: 'var(--green-surface)',
    border: '1px solid rgba(34,217,122,0.3)',
    color: 'var(--green-bright)',
    hover: 'rgba(34,217,122,0.15)',
  },
  warning: {
    background: 'var(--amber-surface)',
    border: '1px solid rgba(255,170,51,0.3)',
    color: 'var(--amber-bright)',
    hover: 'rgba(255,170,51,0.15)',
  },
  primary: {
    background: 'var(--blue-surface)',
    border: '1px solid rgba(77,159,255,0.3)',
    color: 'var(--blue-bright)',
    hover: 'rgba(77,159,255,0.15)',
  },
  ghost: {
    background: 'transparent',
    border: '1px solid transparent',
    color: 'var(--text-secondary)',
    hover: 'var(--bg-hover)',
  },
};

export default function Button({ children, variant = 'default', onClick, disabled, icon, size = 'md', style = {} }) {
  const [hovered, setHovered] = useState(false);
  const v = VARIANTS[variant] || VARIANTS.default;
  const sizes = {
    sm: { padding: '5px 10px', fontSize: 11, height: 28 },
    md: { padding: '7px 14px', fontSize: 12, height: 34 },
    lg: { padding: '10px 20px', fontSize: 13, height: 40 },
  };
  const s = sizes[size];

  return (
    <button
      onClick={onClick}
      disabled={disabled}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        gap: 6,
        padding: s.padding,
        height: s.height,
        background: hovered && !disabled ? v.hover : v.background,
        border: v.border,
        borderRadius: 'var(--radius-md)',
        color: disabled ? 'var(--text-disabled)' : v.color,
        fontFamily: 'var(--font-mono)',
        fontSize: s.fontSize,
        fontWeight: 500,
        letterSpacing: '0.06em',
        cursor: disabled ? 'not-allowed' : 'pointer',
        transition: 'all var(--transition)',
        whiteSpace: 'nowrap',
        opacity: disabled ? 0.5 : 1,
        ...style,
      }}
    >
      {icon && <span style={{ fontSize: s.fontSize + 2 }}>{icon}</span>}
      {children}
    </button>
  );
}