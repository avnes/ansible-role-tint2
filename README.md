master: [![Build Status](https://travis-ci.org/avnes/ansible-role-tint2.png?branch=master)](https://travis-ci.org/avnes/ansible-role-tint2) develop: [![Build Status](https://travis-ci.org/avnes/ansible-role-tint2.png?branch=develop)](https://travis-ci.org/avnes/ansible-role-tint2)

# ansible-role-tint2

Ansible role for installing tint2 and performing basic setup and configuration.

## Requirements

None for running the role.

In order to continuously develop and test this role, you will need docker, pip, molecule, testinfra and python-docker-py installed.

Install docker, pip and python-docker-py with your distributions package manager. Then install molecule and tesinfra with pip:

```
pip install molecule
pip install testinfra
```

## Role Variables

```
config_owner:
  String (mandatory) to specify the Linux user that should have tint2 setup for them.

launcher_item_app:
  List (mandatory) to specify which applications to add to the tint2 launcher.
```

More variables (optional) are found in defaults/main.yml, and the rest of them are used with the tint2rc.j2 template.

## Dependencies

None

## Example Playbook

```
- hosts: all
  vars:
    config_owner: 'maya'
    launcher_item_app:
      - '/usr/share/applications/chromium-browser.desktop'
      - '/usr/share/applications/pcmanfm.desktop'
      - '/usr/share/applications/atom.desktop'
      - '/usr/share/applications/keepassx2.desktop'
      - '/usr/share/applications/lxterminal.desktop'
  roles:
     - { role: avnes.ansible-role-tint2 }
```

## Test

```
molecule create
molecule test
```

## License

MIT

## Author Information

<https://github.com/avnes>
