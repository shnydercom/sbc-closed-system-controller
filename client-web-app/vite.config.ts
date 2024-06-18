import { defineConfig } from 'vite'
import { VitePWA, VitePWAOptions } from 'vite-plugin-pwa'
import react from '@vitejs/plugin-react-swc'

const PWAoptions: Partial<VitePWAOptions> = {
	manifest: {
		"name": "SBC closed system controller",
		"short_name": "SBC CSC",
		"start_url": "/",
		"scope": "/",
		"display": "standalone",
		"theme_color": "#000000",
		"background_color": "#000000",
		"icons": [
			{
				"src": "/static/icons/icon_144x144.png",
				"sizes": "144x144",
				"type": "image/png",
				"purpose": "any maskable"
			},
			{
				"src": "/static/icons/icon_192x192.png",
				"sizes": "192x192",
				"type": "image/png",
				"purpose": "any maskable"
			},
			{
				"src": "/static/icons/icon_512x512.png",
				"sizes": "512x512",
				"type": "image/png",
				"purpose": "any maskable"
			}
		]
	}
}

// https://vitejs.dev/config/
export default defineConfig({
	plugins: [VitePWA(PWAoptions), react()],
	server: {
		proxy: {
			"/rest": {
				target: 'http://127.0.0.1:8000/rest',
				changeOrigin: true,
				rewrite: (path) => path.replace(/^\/rest/, ''),
			},
		}
	}
})
