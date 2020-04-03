const path = require("path");
const VueLoaderPlugin = require("vue-loader/lib/plugin");

module.exports = {
  mode: "development",
  entry: path.resolve(__dirname, "frontend", "index.js"),

  output: {
    filename: "main.js",
    path: path.resolve(
      __dirname,
      process.env.FLASK_APPLICATION_PATH,
      "static",
      "js"
    ),
  },

  resolve: {
    alias: {
      vue$: "vue/dist/vue.esm.js",
    },
    extensions: [".vue", ".js"],
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        loader: "babel-loader",
      },
      {
        test: /\.vue$/,
        loader: "vue-loader",
      },
    ],
  },

  plugins: [new VueLoaderPlugin()],
};
