const path = require('path');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    mode: 'production',
    entry: './src/main.js',
    output: {
        path: path.resolve(__dirname, './dist'),
        publicPath: '/dist/',
        filename: 'build.js'
    },
    plugins: [
        new BundleTracker({
            filename: 'webpack-stats.json'
        }),
    ],
    module: {
        rules: [
            // Loader configuration goes here
        ]
    }
}
