# Ansible Collection - robertdebock.roles

A collection of roles found on [robertdebock.nl](https://robertdebock.nl/).

## Using roles in this collection.

1. Install the collection:

```shell
ansible-galaxy collection install robertdebock.roles
```

You can also list a collection in `requirements.yml`:

```yaml
---
collections:
  - name: robertdebock.roles
```

2. Include roles in your playbooks:

```yaml
---
- name: make a great machine
  hosts: all
  tasks:
    - name: bootstrap
      import_role:
        name: robertdebock.roles.bootstrap
```
