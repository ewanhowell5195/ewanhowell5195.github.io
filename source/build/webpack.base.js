const path = require('path')

const config = require('../config')

module.exports = {
  entry: [
    './' + path.join('.', config.styleInput),
    './' + path.join('.', config.scriptInput)
  ],
  output: {
    path: config.buildPath,
    filename: 'bundle.js'
  },
  target: 'web',
  module: {
    rules: [
      {
        test: /\.pug$/,
        use: [ 'pug-loader' ]
      },
      {
        test: /\.worker\.js$/,
        use: [ 'worker-loader' ]
      }
    ]
  }
}
