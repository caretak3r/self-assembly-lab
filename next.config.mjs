import nextra from 'nextra'

const isProd =
  process.env.GITHUB_ACTIONS === 'true' ||
  process.env.NODE_ENV === 'production'

const basePath = isProd ? '/self-assembly-lab' : ''

const withNextra = nextra({
  search: {
    codeblocks: false
  }
})

export default withNextra({
  output: 'export',
  images: {
    unoptimized: true
  },
  trailingSlash: true,
  ...(basePath
    ? {
        basePath,
        assetPrefix: `${basePath}/`
      }
    : {})
})
