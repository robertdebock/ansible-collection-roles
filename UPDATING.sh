#!/bin/sh

# Copy all roles.
for role in ../ansible-role-* ; do
  short=$(echo ${role} | cut -d\- -f3)
  if [ ! -d roles/${short} ] ; then
    echo "Copying ${role} to roles/${short}."
    cp -Rip "${role}" "roles/${short}"
  fi
done

# Clean-up the copied roles.
ls -d roles/* | while read short ; do
  for object in .git .cache .tox .DS_Store ; do
    if [ -d ./${short}/${object} ] ; then
      echo "Removing roles/${short}/${object}."
      rm -Rf "roles/${short}/${object}"
    fi
  done
done

# Regenerate all used collections.
echo "---" > requirements.yml
echo "collections:" >> requirements.yml
cat roles/*/requirements.yml | grep '  - name: ' | grep -v robertdebock | sort | uniq >> requirements.yml
