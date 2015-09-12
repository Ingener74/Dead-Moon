gulp = require 'gulp'
clean = require 'gulp-clean'
run_sequence = require 'run-sequence'
shell = require 'gulp-shell'
cjsx = require 'gulp-cjsx'
gutil = require 'gulp-util'

gulp.task 'clean', ->
  gulp.src './build/'
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

gulp.task 'start_flask', shell.task [
  'cd build && python main.py'
]

gulp.task 'default', (callback) ->
  run_sequence 'build', 'start_flask', callback

