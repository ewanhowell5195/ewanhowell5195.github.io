const path = require('path')
const webpack = require('webpack')
const merge = require('webpack-merge')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const FriendlyErrorsPlugin = require('friendly-errors-webpack-plugin')

const config = require('../config')
const webpackBaseConfig = require('./webpack.base')

module.exports = merge(webpackBaseConfig, {
  mode: 'development',
  entry: ['./build/dev-client.js'],
  module: {
    rules: [{
        test: /\.styl$/,
        use: [
          'style-loader',
          'css-loader',
          'stylus-loader'
        ]
      },
      {
        test: /\.(jpe?g|png|gif|svg|mp4|ogg|mp3|ttf)$/,
        use: [{
          loader: 'file-loader',
          options: {}
        }]
      }
    ]
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(),
    new HtmlWebpackPlugin({
      filename: config.buildOptions.htmlFileName,
      template: config.htmlInput,
      inject: true
    }),
    new FriendlyErrorsPlugin()
  ]
})
