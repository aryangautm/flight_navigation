var path = require('path');
var webpack = require('webpack');

module.exports = {
    mode: 'production',
    entry: './src/main.jsx',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js',
    },
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                type: "javascript/auto",

                use: {
                    loader: 'babel-loader',
                },
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader'],
            },
        ],
    },
    resolve: {
        fullySpecified: false,
        extensions: ['.js', '.jsx'],
    },
};
