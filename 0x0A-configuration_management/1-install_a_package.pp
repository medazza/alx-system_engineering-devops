#!usr/bin/pup
# Install a specific version of Flask

package	{ 'python3.8':
	ensure	=>	'3.8.10',
}

package { 'python3-pip':
	ensure	=> installed,
}

package { 'flask':
	ensure	=> '2.1.0',
	provider	=> 'pip',
	require	=> Package['python3-pip'],
}

package { 'werkzeug':
	ensure	=> '2.1.1',
	provider	=> 'pip',
	require	=> Package['python3-pip'],
}
