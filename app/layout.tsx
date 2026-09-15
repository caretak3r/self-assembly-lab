import { Footer, Layout, Navbar } from 'nextra-theme-docs'
import { Banner, Head } from 'nextra/components'
import { getPageMap } from 'nextra/page-map'
import type { ReactNode } from 'react'
import 'nextra-theme-docs/style.css'

export const metadata = {
  title: {
    default: 'Self-Assembly Lab',
    template: '%s – Self-Assembly Lab'
  },
  description:
    'Educational docs for young scientists & engineers: molecular DNA self-assembly, swarm robotics, and programmable matter — with honest frontier framing.'
}

const banner = (
  <Banner storageKey="frontier-2026-09">
    Honest framing: engineered self-assembly is mostly lab-scale. Nature already
    self-assembles; engineers program interactions; products are still limited.
  </Banner>
)

const navbar = (
  <Navbar
    logo={<b>Self-Assembly Lab</b>}
    projectLink="https://github.com/caretak3r/self-assembly-lab"
  />
)

const footer = (
  <Footer>
    {new Date().getFullYear()} © caretak3r · Educational corpus curated 2026-09-15
    (ET) ·{' '}
    <a href="https://github.com/caretak3r/self-assembly-lab">GitHub</a>
  </Footer>
)

export default async function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en" dir="ltr" suppressHydrationWarning>
      <Head />
      <body>
        <Layout
          banner={banner}
          navbar={navbar}
          pageMap={await getPageMap()}
          docsRepositoryBase="https://github.com/caretak3r/self-assembly-lab/tree/main/content"
          editLink="Edit this page on GitHub"
          footer={footer}
          sidebar={{ defaultMenuCollapseLevel: 1 }}
        >
          {children}
        </Layout>
      </body>
    </html>
  )
}
