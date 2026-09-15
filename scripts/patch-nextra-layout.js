/**
 * nextra-theme-docs Layout strips `children` before Zod-parsing theme config,
 * but LayoutPropsSchema still marks children as required — fails on Zod 4.
 * Make children optional so static export / SSR works.
 */
const fs = require('fs')
const path = require('path')

const target = path.join(
  __dirname,
  '..',
  'node_modules',
  'nextra-theme-docs',
  'dist',
  'schemas.js'
)

if (!fs.existsSync(target)) {
  console.warn('[patch-nextra] schemas.js not found, skip')
  process.exit(0)
}

let text = fs.readFileSync(target, 'utf8')
const from = '  children: reactNode,'
const to = '  children: reactNode.optional(),'
if (text.includes(to)) {
  console.log('[patch-nextra] already patched')
  process.exit(0)
}
if (!text.includes(from)) {
  console.warn('[patch-nextra] expected pattern missing; skip')
  process.exit(0)
}
fs.writeFileSync(target, text.replace(from, to))
console.log('[patch-nextra] patched LayoutPropsSchema.children → optional')
