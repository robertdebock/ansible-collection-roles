# f5networks.f5_modules

This collection includes the most recently released ansible modules for BIG-IP and BIG-IQ from F5Networks. This collection packages and distributes playbooks, roles, modules, and plugins.

## Requirements

 - ansible >= 2.9
 - ipaddress (python < 3.5)

## Installation

To install in ansible default or defined paths use:
```bash
ansible-galaxy collection install f5networks.f5_modules
```

To specify the installation location use `-p`. If specifying a folder, make sure to update the `ansible.cfg` so ansible will check this folder as well.
```bash
ansible-galaxy collection install f5networks.f5_modules -p collections/
```

To specify the version of the collection to install, include it at the end of the collection with `:==1.0.0`:
```bash
ansible-galaxy collection install f5networks.f5_modules:==1.0.0
```

Sematic Versioning examples below:
- Increment major (for example: x in x.y.z) version number for an incompatible API change.
- Increment minor (for example: y in x.y.z) version number for new functionality in a backwards compatible manner.
- Increment patch (for example: z in x.y.z) version number for backwards compatible bug fixes.

## Deprecation Notice
Support for versions of Python earlier than 3.5 is being deprecated and will be removed at a future date. 

## Example Usage


To use a module from a collection, reference the full namespace, collection, and modules name that you want to use:

```
---
- name: Using Collections
  hosts: f5
  connection: local

  tasks:
    - f5networks.f5_modules.bigip_pool:
        name: my-pool
        ....

```

## Author Information

F5 Networks
[F5 Networks](http://www.f5.com)
