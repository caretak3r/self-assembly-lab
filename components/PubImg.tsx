/** Local public/ image with basePath-safe src for GitHub Pages static export. */
export function PubImg({
  src,
  alt,
  caption,
  credit,
  width,
  height
}: {
  src: string
  alt: string
  caption?: string
  credit?: string
  width?: number
  height?: number
}) {
  const base = process.env.NEXT_PUBLIC_BASE_PATH || ''
  const path = src.startsWith('/') ? src : `/${src}`
  return (
    <figure style={{ margin: '1.5rem 0' }}>
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        src={`${base}${path}`}
        alt={alt}
        width={width}
        height={height}
        style={{
          width: '100%',
          height: 'auto',
          borderRadius: 8,
          display: 'block'
        }}
      />
      {(caption || credit) && (
        <figcaption
          style={{ fontSize: '0.875rem', opacity: 0.85, marginTop: 8 }}
        >
          {caption}
          {caption && credit ? ' · ' : null}
          {credit ? <em>{credit}</em> : null}
        </figcaption>
      )}
    </figure>
  )
}
