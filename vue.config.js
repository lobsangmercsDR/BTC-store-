

module.exports = {
    configureWebpack: {
      resolve: {
        fallback: {
          "path": require.resolve("path-browserify"),
          "stream": require.resolve("stream-browserify"),
          "zlib": require.resolve("browserify-zlib"),
          "crypto": require.resolve("crypto-browserify"),
          "fs": false,
          "http": require.resolve("stream-http"),
          "net": require.resolve("net-browserify")
        }
      },
    },
    devServer: {
      "host": 'localhost',
    }
  };
  