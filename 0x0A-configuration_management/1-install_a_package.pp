#!usr/bin/pup
# Install a specific version of Flask
package {'python3-pip':
	ensure => installed,
}

package {'flask':
	ensure 	 => '2.1.0',
	provider => 'pip',
	require => Package['python3-pip'],
}

package {'werkzeug':
	ensure => '2.1.0',
	provider => 'pip',
	require => Package['python3-pip'],
}
