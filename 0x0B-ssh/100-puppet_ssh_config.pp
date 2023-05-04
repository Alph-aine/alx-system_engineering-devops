# This is a Puppet code that ensures the SSH configuration to a server is set
file {'Turn off passwd auth':
  path => '~/.ssh/config',
  line => 'PasswordAuthentication no',
}

file {'Daclare identity file':
  path => '~/.ssh/config',
  line =>'IdentityFile ~/.ssh/school',
}
