# automate the task of creating a custom HTTP header response
# but with Puppet.
package { 'nginx':
  ensure   => present,
  require  => Exec['update'],
  provider => 'apt',
}

-> exec { 'update':
  command  => 'sudo apt update',
  provider => shell,
  refreshonly = true,
}

-> file_line { 'header line':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => " location / {
	add_header X-Served-By ${hostname};",
  match  => '^\tlocation / {',
}

-> service { 'nginx':
  ensure = 'running',
  enable    => true,
  subscribe => File_line['header line'],
}
