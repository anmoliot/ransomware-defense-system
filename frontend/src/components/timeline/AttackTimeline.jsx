function AttackTimeline({ events }) {
  return (
    <section className="panel">
      <div className="panel-heading">
        <div>
          <p className="eyebrow">Live Timeline</p>
          <h2>Reconstructed attack chain</h2>
        </div>
      </div>
      <ol className="timeline">
        {events.map(([time, title, detail, severity]) => (
          <li key={`${time}-${title}`} className={severity}>
            <time>{time}</time>
            <div>
              <strong>{title}</strong>
              <p>{detail}</p>
            </div>
          </li>
        ))}
      </ol>
    </section>
  )
}

export default AttackTimeline
