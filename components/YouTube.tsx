/** Embeddable YouTube player for MDX chapters (verified public video IDs only). */
export function YouTube({
  id,
  title = 'YouTube video'
}: {
  id: string
  title?: string
}) {
  return (
    <div
      className="youtube-embed"
      style={{
        position: 'relative',
        paddingBottom: '56.25%',
        height: 0,
        overflow: 'hidden',
        margin: '1.5rem 0',
        borderRadius: 8,
        background: '#0f172a'
      }}
    >
      <iframe
        src={`https://www.youtube-nocookie.com/embed/${id}`}
        title={title}
        loading="lazy"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowFullScreen
        referrerPolicy="strict-origin-when-cross-origin"
        style={{
          position: 'absolute',
          top: 0,
          left: 0,
          width: '100%',
          height: '100%',
          border: 0
        }}
      />
    </div>
  )
}
