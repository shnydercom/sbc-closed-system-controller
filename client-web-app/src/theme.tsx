import { CssBaseline, ThemeProvider, createTheme } from '@mui/material';
import "@fontsource/metropolis";
import React from 'react';

export const theme = createTheme({
	typography: {
		fontFamily: 'Metropolis',
	},
	components: {
		MuiCssBaseline: {
			styleOverrides: `
        @font-face {
          font-family: 'Metropolis';
        }
      `,
		},
	},
});

export const MainThemeProvider = (props: React.PropsWithChildren<{}>) => {
	return (
		<ThemeProvider theme={theme}>
			<CssBaseline />
				{props.children}
		</ThemeProvider>)
}