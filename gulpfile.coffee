gulp = require 'gulp'
clean = require 'gulp-clean'
run_sequence = require 'run-sequence'
cjsx = require 'gulp-cjsx'
gutil = require 'gulp-util'
browsersync = require 'browser-sync'

exec = require('child_process').exec;

gulp.task 'full_clean', ->
  gulp.src ['./build/']
  .pipe clean()

gulp.task 'clean', ->
  gulp.src ['./build/templates/', './build/static/']
  .pipe clean()

gulp.task 'css', ->
  gulp.src [
    './bower_components/bootstrap/dist/css/*.min.css',
    './app/static/css/**.css'
  ]
  .pipe gulp.dest './build/static/css'

gulp.task 'js', ->
  gulp.src [
    './bower_components/bootstrap/dist/js/*.min.js',
    './bower_components/react/*.min.js'
  ]
  .pipe gulp.dest './build/static/js'

gulp.task 'html', ->
  gulp.src './app/templates/**/*.html'
  .pipe gulp.dest './build/templates/'

gulp.task 'py', ->
  gulp.src './app/*.py'
  .pipe gulp.dest './build/'

gulp.task 'cjsx', ->
  gulp.src('./app/static/cjsx/*.cjsx')
  .pipe cjsx({bare: true}).on('error', gutil.log)
  .pipe gulp.dest './build/static/js/'

gulp.task 'build', (callback)->
  run_sequence 'clean', ['html', 'css', 'js', 'py', 'cjsx'], callback

gulp.task 'runserver', ->
  exec 'cd build && python main.py'

gulp.task 'start_browser', ['runserver'], ->
  browsersync(
    notify: false,
    proxy: "127.0.0.1:5003"
  )
  gulp.watch [
    'app/templates/*.*',
    'app/static/cjsx/*.*',
    'app/static/css/*.*'
  ], ['build', browsersync.reload]

gulp.task 'default', (callback) ->
  run_sequence 'build', ['start_browser'], callback

gulp.task 'full_build', (callback)->
  run_sequence 'full_clean', ['html', 'css', 'js', 'py', 'cjsx'], callback
