# This is a Puppet code that ensures the SSH configuration to a server is set
file {'Turn off passwd auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

file {'Daclare identity file':
  path => '/etc/ssh/ssh_config',
  line =>'IdentityFile ~/.ssh/school',
}
