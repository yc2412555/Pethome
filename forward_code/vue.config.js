module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://rap2api.taobao.org/app/mock/223896',
        ws: true,
        changeOrigin: true
      }
    }
  }
}
