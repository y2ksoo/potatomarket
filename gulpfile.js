const gulp = require("gulp");

const css = () => {
    const postCSS = require("gulp-postcss");
    const sass = require("gulp-sass");
    const minify = require("gulp-csso");
    sass.compiler = require('node-sass');
    return gulp
        .src("mysite/assets/scss/styles.scss")
        .pipe(sass().on("error", sass.logError))
        .pipe(postCSS([require("tailwindcss"),require("autoprefixer")        ]))
        .pipe(minify())
        .pipe(gulp.dest("mysite/static/css"));
};

exports.default = css;
