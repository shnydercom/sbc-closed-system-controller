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
		MuiAppBar: {
			styleOverrides: {
				colorPrimary: {
					backgroundColor: "#86c5f2"
				}
			}
		},
		MuiToggleButton: {
			styleOverrides: {
				root: {
					color: "white",
					borderColor: "white",
					"&.Mui-disabled": {
						color: "rgba(255, 255, 255, 0.5)",
						border: "1px solid rgba(255, 255, 255, 0.5)"
					},
					"&.Mui-selected": {
						color: "rgba(255,0,0,1)",
					}


				},

			}
		}


	},
});

export const darkTheme = createTheme({
	...theme,
	palette: {
		mode: "dark",
	},
})

export const MainThemeProvider = (props: React.PropsWithChildren<{}>) => {
	return (
		<ThemeProvider theme={theme}>
			<CssBaseline />
			{props.children}
		</ThemeProvider>)
}

export const DarkThemeProvider = (props: React.PropsWithChildren<{}>) => {
	return (
		<ThemeProvider theme={darkTheme}>
			<CssBaseline />
			{props.children}
		</ThemeProvider>)
}