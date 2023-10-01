module.exports = {
    // Otras configuraciones de ESLint aquí
  
    overrides: [
      {
        files: ["*.vue"],
        rules: {
          "vue/no-unused-components": "off",
        },
      },
    ],
  };
  