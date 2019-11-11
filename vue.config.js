const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  publicPath: 'http://127.0.0.1:8080/',
  outputDir: './dist/',
  assetsDir: './public/static',

  devServer: {
    disableHostCheck: true
  },
  chainWebpack: config => {
    config.optimization.splitChunks(false)

    config.plugin('BundleTracker').use(BundleTracker, [{filename: './webpack-stats.json'}])

    config.devServer.public('http://0.0.0.0:8080').host('0.0.0.0').port(8080).https(false).headers({"Access-Control-Allow-Origin":["\*"]})
  },

  pages: {
    index: 'src/main.js'
  }
}