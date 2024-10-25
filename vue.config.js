const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    allowedHosts: 'all', // Permitir todos os hosts, incluindo o Ngrok
    client: {
      webSocketURL: 'wss://e9e8-2804-1454-4001-330-dddd-00-40c0.ngrok-free.app/ws', // Use o protocolo wss:// para WebSocket seguro
    },
  }
})