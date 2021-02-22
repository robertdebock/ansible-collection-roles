# Updating the roles

1. Delete the roles:

```shell
cd roles
rm -Rf *
```

2. Copy the roles in:

```shell
for role in /home/robertdb/Documents/github.com/robertdebock/ansible-role-* ; do cp -r ${role} $(basename ${role} | cut -d- -f3) ; done
```

3. Remove the .git folder.

```
find ./ -name .git -type d -exec rm -Rf {} \;
```
