import { useState } from 'react'

function ThreatGraph({ graph }) {
  const [selectedNode, setSelectedNode] = useState(graph.nodes[0])

  return (
    <section className="panel graph-panel">
      <div className="panel-heading">
        <div>
          <p className="eyebrow">Attack Graph</p>
          <h2>User to process to IOC</h2>
        </div>
      </div>
      <div className="graph-canvas">
        <svg viewBox="0 0 100 76" role="img" aria-label="Threat graph">
          {graph.edges.map(([source, target, label]) => {
            const from = graph.nodes.find((node) => node.id === source)
            const to = graph.nodes.find((node) => node.id === target)
            return (
              <g key={`${source}-${target}`}>
                <line x1={from.x} y1={from.y} x2={to.x} y2={to.y} />
                <text x={(from.x + to.x) / 2} y={(from.y + to.y) / 2 - 1}>{label}</text>
              </g>
            )
          })}
          {graph.nodes.map((node) => (
            <g key={node.id}>
              <circle
                className={`node node-${node.type}`}
                cx={node.x}
                cy={node.y}
                onClick={() => setSelectedNode(node)}
                r="4.8"
                tabIndex="0"
              />
              <text className="node-label" onClick={() => setSelectedNode(node)} x={node.x} y={node.y + 10}>{node.label}</text>
            </g>
          ))}
        </svg>
      </div>
      <div className="graph-detail">
        <strong>{selectedNode.label}</strong>
        <span>{selectedNode.type} · Risk {selectedNode.risk}</span>
      </div>
    </section>
  )
}

export default ThreatGraph
