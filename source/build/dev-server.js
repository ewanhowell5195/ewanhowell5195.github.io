var config = require('../config')
var publicPath = '/'
var staticFolder = 'assets'

if (!process.env.NODE_ENV) {
  process.env.NODE_ENV = 'development'
}

var path = require('path')
var express = require('express')
var webpack = require('webpack')
var webpackConfig = require('../build/webpack.dev')

// default port where dev server listens for incoming traffic
var port = process.env.PORT || config.port || 8080

var app = express()
var compiler = webpack(webpackConfig)


var devMiddleware = require('webpack-dev-middleware')(compiler, {
  publicPath: publicPath,
  quiet: true
})

var hotMiddleware = require('webpack-hot-middleware')(compiler, {
  log: () => {}
})
// force page reload when html-webpack-plugin template changes
let lastHtml = ''
compiler.plugin('compilation', function (compilation) {
  compilation.plugin('html-webpack-plugin-after-emit', function (data, cb) {
    const newHtml = data.html.source()
    if (lastHtml !== newHtml) {
      hotMiddleware.publish({ action: 'reload' })
    }
    lastHtml = newHtml
    cb()
  })
})

// handle fallback for HTML5 history API
app.use(require('connect-history-api-fallback')())

// serve webpack bundle output
app.use(devMiddleware)

// enable hot-reload and state-preserving
// compilation error display
app.use(hotMiddleware)

// serve pure static assets
var staticPath = path.posix.join(publicPath, staticFolder)
app.use(staticPath, express.static('./assets'))

var uri = 'http://localhost:' + port

var _resolve
var readyPromise = new Promise(resolve => {
  _resolve = resolve
})

console.log('> Starting dev server...')
devMiddleware.waitUntilValid(() => {
  console.log('> Listening at ' + uri + '\n')
  // when env is testing, don't need open it
  _resolve()
})

var server = app.listen(port)

module.exports = {
  ready: readyPromise,
  close: () => {
    server.close()
  }
}
