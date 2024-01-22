# 0x0A. Configuration management

## Table of Contents
1. [Overview](#overview)
2. [Puppet Resource Type: File](#puppet-resource-type-file)
3. [Puppet's Declarative Language](#puppets-declarative-language)
4. [Puppet Lint](#puppet-lint)
5. [Puppet Emacs Mode](#puppet-emacs-mode)

## 1. Overview

Configuration management is a crucial aspect of IT infrastructure management, allowing for the consistent and automated configuration of systems. Puppet is a widely-used configuration management tool that helps automate the provisioning and management of infrastructure.

## 2. Puppet Resource Type: File

In Puppet, a "resource type" defines a type of system object or property that you want to manage. The `file` resource type, in particular, is used to manage files on a system. It allows you to define attributes such as file path, permissions, owner, group, and content.

### Example Puppet Manifest for Creating a File

```puppet
file { '/path/to/file':
  ensure   => file,
  mode     => '0644',
  owner    => 'user',
  group    => 'group',
  content  => 'File content here',
}
```

This example creates a file with specified attributes.

## 3. Puppet's Declarative Language

Puppet uses a declarative language, allowing you to describe the desired state of your system without specifying the step-by-step procedure to achieve that state. This model-driven approach makes Puppet more expressive and easier to understand.

Instead of scripting every action, you declare the end result you want, and Puppet takes care of figuring out how to achieve it.

## 4. Puppet Lint

Puppet Lint is a tool that checks Puppet code against a set of style guidelines. It helps maintain consistency in your Puppet manifests and ensures best practices. Running Puppet Lint on your codebase can catch potential issues early in the development process.

To use Puppet Lint:

```bash
puppet-lint your_manifest.pp
```

## 5. Puppet Emacs Mode

If you use Emacs as your text editor, Puppet Emacs Mode provides syntax highlighting and other features to enhance your Puppet coding experience. It helps in easily identifying Puppet language elements and ensures cleaner code.

To set up Puppet Emacs Mode, refer to the official documentation or install it using package managers like `MELPA` for Emacs.

---

Feel free to explore more about Puppet and its features by referring to the official [Puppet Documentation](https://puppet.com/docs/puppet/latest/).

## Author
* **AZZA MOHAMED** [AZZA](https://github.com/medazza)- ALX-Africa SE Student cohort 17