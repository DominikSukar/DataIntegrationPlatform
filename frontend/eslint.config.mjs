import globals from "globals";
import pluginJs from "@eslint/js";
import * as tseslint from "@typescript-eslint/eslint-plugin";
import tsParser from "@typescript-eslint/parser";

export default [
  {
    files: ["**/*.{js,jsx,mjs,cjs,ts,tsx}"],
    languageOptions: { 
      globals: globals.browser,
      parser: tsParser,
      parserOptions: {
        project: "./tsconfig.json",
      },
    },
    plugins: {
      "@typescript-eslint": tseslint,
    },
  },
  pluginJs.configs.recommended,
  ...tseslint.configs.recommended,
];