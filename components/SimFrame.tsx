/** BasePath-safe embedded HTML simulator frame for GitHub Pages static export. */
export function SimFrame({
  src,
  title,
  height = 680
}: {
  src: string
  title: string
  height?: number
}) {
  const base = process.env.NEXT_PUBLIC_BASE_PATH || ''
  const path = src.startsWith('/') ? src : `/${src}`
  const fullSrc = `${base}${path}`

  return (
    <figure style={{ margin: '1.5rem 0' }}>
      <iframe
        src={fullSrc}
        title={title}
        style={{
          width: '100%',
          height,
          border: '1px solid rgba(148, 163, 184, 0.25)',
          borderRadius: 10,
          background: '#0c0f14',
          display: 'block'
        }}
        loading="lazy"
      />
      <figcaption
        style={{
          fontSize: '0.875rem',
          opacity: 0.85,
          marginTop: 8,
          display: 'flex',
          justifyContent: 'space-between',
          gap: 12,
          flexWrap: 'wrap'
        }}
      >
        <span>{title}</span>
        <a
          href={fullSrc}
          target="_blank"
          rel="noopener noreferrer"
          style={{ textDecoration: 'underline' }}
        >
          Open full-screen simulator ↗
        </a>
      </figcaption>
    </figure>
  )
}
