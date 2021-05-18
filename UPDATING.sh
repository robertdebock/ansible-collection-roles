#!/bin/sh

# Copy all roles.
for role in ../ansible-role-* ; do
  short=$(echo ${role} | cut -d\- -f3)
  if [ ! -d roles/${short} ] ; then
    mkdir "roles/${short}"
    echo "Copying ${role} to roles/${short}."
    for object in LICENSE README.md defaults files handlers meta requirements.yml tasks templates vars ; do
      if [ -d "${role}/${object}" ] ; then
        cp -Rip "${role}/${object}" "roles/${short}/${object}"
      elif [ -f "${role}/${object}" ] ; then
        cp "${role}/${object}" "roles/${short}/${object}"
      fi
    done
  fi
done

# Regenerate all used collections.
echo "---" > requirements.yml
echo "collections:" >> requirements.yml
cat roles/*/requirements.yml | grep '  - name: ' | grep -v robertdebock | sort | uniq >> requirements.yml
