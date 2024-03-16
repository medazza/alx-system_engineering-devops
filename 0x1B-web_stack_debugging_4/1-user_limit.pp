# increase holberton user hard file limit and soft file limit
exec { 'increase-hard-file-limit':
  command => 'sed -i "/holberton hard/s/5/8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'increase-soft-file-limit':
  command => 'sed -i "/holberton soft/s/4/8192/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
