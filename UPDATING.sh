#!/bin/sh -x

directories="default files handlers meta tasks templates vars"
files="README.md requirements.yml"

for role in /home/robertdb/Documents/github.com/robertdebock/ansible-role-* ; do
  for directory in ${directories} ; do
    if [ -d ${role}/${directory} ] ; then
      mkdir -p $(basename ${role} | cut -d- -f3)/${directory}
      cp -r ${role}/${directory}/* $(basename ${role} | cut -d- -f3)/${directory}/
    fi
  done
  for file in ${files} ; do
    if [ -f ${role}/${file} ] ; then
      cp ${role}/${file} $(basename ${role} | cut -d- -f3)/${file}
    fi
  done
done
