const path = require('path')
const webpack = require('webpack')
const merge = require('webpack-merge')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const HtmlWebpackExcludeAssetsPlugin = require('html-webpack-exclude-assets-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const StyleExtHtmlWebpackPlugin = require('style-ext-html-webpack-plugin')
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin')
const TerserPlugin = require('terser-webpack-plugin')

const config = require('../config')
const webpackBaseConfig = require('./webpack.base')

module.exports = merge(webpackBaseConfig, {
  mode: 'production',
  optimization: {
    minimizer: [
      new OptimizeCSSAssetsPlugin({}),
      new TerserPlugin()
    ]
  },
  module: {
    rules: [
      {
        test: /\.styl$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader', 'stylus-loader']
      },
      {
        test: /\.(jpe?g|png|gif|svg|mp4|ogg|mp3|ttf)$/,
        use: [{
          loader: 'file-loader',
          options: {
            name: '[path][name].[ext]'
          }
        }]
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      filename: config.buildOptions.htmlFileName,
      template: config.htmlInput,
      inject: true
    }),
    new MiniCssExtractPlugin(),
    new HtmlWebpackExcludeAssetsPlugin(),
    new StyleExtHtmlWebpackPlugin(),
  ]
})
