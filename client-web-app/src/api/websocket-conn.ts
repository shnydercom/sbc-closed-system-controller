export const wsConnection = new WebSocket(`ws://${window.location.host}:8000/ws`);
//wsConnection.onmessage = 