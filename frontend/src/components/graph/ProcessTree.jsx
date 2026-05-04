import { useState } from 'react'

function ProcessTree({ tree }) {
  return (
    <section className="panel">
      <div className="panel-heading">
        <div>
          <p className="eyebrow">Process Lineage</p>
          <h2>Expandable ancestry</h2>
        </div>
      </div>
      <div className="tree-list">
        <TreeNode node={tree} depth={0} />
      </div>
    </section>
  )
}

function TreeNode({ node, depth }) {
  const [open, setOpen] = useState(true)
  const hasChildren = node.children?.length > 0
  return (
    <div className="tree-node">
      <button type="button" onClick={() => setOpen(!open)} style={{ paddingLeft: `${depth * 18 + 8}px` }}>
        <span>{hasChildren ? (open ? '−' : '+') : '•'}</span>
        <strong>{node.name}</strong>
        <em className={node.risk > 80 ? 'risk-high' : node.risk > 50 ? 'risk-med' : ''}>Risk {node.risk}</em>
      </button>
      {open && hasChildren && node.children.map((child) => (
        <TreeNode key={`${node.name}-${child.name}`} node={child} depth={depth + 1} />
      ))}
    </div>
  )
}

export default ProcessTree
