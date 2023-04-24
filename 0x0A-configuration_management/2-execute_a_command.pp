# This is a command to kill a process named 'killmenow'
exec { 'kill-process':
  command => '/bin/pkill killmenow',
}
