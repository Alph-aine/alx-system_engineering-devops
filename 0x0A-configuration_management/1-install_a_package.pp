# This code ensures Flask with the specified version is installed
package { ['python3', 'python3-pip']:
  ensure => installed,
}
exec { 'flask':
  command => '/usr/bin/pip3 install -U Flask==2.1.0',
  require => Package['python3-pip'],
}
