import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import "@fontsource/metropolis";
import { MainThemeProvider } from './theme.tsx';
import { store } from './store/reduxStore.ts';
import { Provider } from 'react-redux'

ReactDOM.createRoot(document.getElementById('root')!).render(
	<React.StrictMode>
		<Provider store={store}>
			<MainThemeProvider>
				<App />
			</MainThemeProvider>
		</Provider>
	</React.StrictMode>,
)
