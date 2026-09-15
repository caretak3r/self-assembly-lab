import { useMDXComponents as getThemeComponents } from 'nextra-theme-docs'
import { Callout } from 'nextra/components'
import { YouTube } from './components/YouTube'
import { PubImg } from './components/PubImg'

const themeComponents = getThemeComponents()

export function useMDXComponents(components?: Record<string, unknown>) {
  return {
    ...themeComponents,
    Callout,
    YouTube,
    PubImg,
    ...components
  }
}
