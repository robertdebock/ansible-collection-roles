# Considerations

Here is a list of things to consider when writing code for this role.

## Readability

The CIS guidelines are difficult enough, try to keep this role as simple as possible:

1. Do not combine rules into a single tasks. Every rule is one or more tasks.
2. Keep this order: module (with parameters), loop (when required), loop_control (when required), when, changed_when (optional), failed_when (optional), notify.

## Verify and Assert

For every variable that's introduced in `defaults/main.yml`, assert the variable to determine if it's set correctly.

For every task in `tasks/main.yml`, have a verification in `molecule/default/*/*.yml` to ensure the tasks change worked. Preferably using different commands/logic to prevent bugs in modules or usage of the module.

## Fix or fail?

This role make quite some choices, here are the thoughts on why to take a decision.

1. Fix if the consequences are limited.
2. Fail if changing has consequences.

If a task needs to fail, add the same task to `tasks/*/*.yml` and to `molecule/default/*/*.yml`.

### Examples

#### 1.1.1.1 Ensure mounting of cramfs filesystems is disabled (Scored)

Disabling cramfs seems straight forward, has limited consequences: Fix

#### 1.1.2 Ensure /tmp is configured

The /tmp directory can be just a directory. Remounting it to it's own filesystem is more involved. For example, files have to be moved: Fail

## Variables

All rules must be selectable with a variable so that consumers of the role can overwrite the CIS guidelines.
