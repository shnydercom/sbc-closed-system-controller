import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import "@fontsource/metropolis";
import { MainThemeProvider } from './theme.tsx';

ReactDOM.createRoot(document.getElementById('root')!).render(
	<React.StrictMode>
		<MainThemeProvider>
			<App />
		</MainThemeProvider>
	</React.StrictMode>,
)
