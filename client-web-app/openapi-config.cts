import type { ConfigFile } from '@rtk-query/codegen-openapi'

const config: ConfigFile = {
  schemaFile: 'http://localhost:8000/openapi.json',
  apiFile: './src/store/emptyApi.ts',
  apiImport: 'emptySplitApi',
  outputFile: './src/store/rtkQueryClientApi.ts',
  exportName: 'rtkQueryClientApi',
  hooks: true,
}

export default config