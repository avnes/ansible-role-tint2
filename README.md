master: [![Build Status](https://travis-ci.org/avnes/ansible-role-tint2.png?branch=master)](https://travis-ci.org/avnes/ansible-role-tint2) develop: [![Build Status](https://travis-ci.org/avnes/ansible-role-tint2.png?branch=develop)](https://travis-ci.org/avnes/ansible-role-tint2)

# Role Name

Ansible role for installing tint2 and performing basic setup and configuration.

## Requirements

None for running the role. In order to continuously develop and test this role, you will need docker, pip, molecule, testinfra and python-docker-py installed.

Install docker, pip and python-docker-py with your distributions package manager. Then install molecule and tesinfra with pip:

```
pip install molecule
pip install testinfra
```

## Role Variables

```
config_owner:
  String (mandatory) to specify the Linux user that should have tint2 setup for them.
```

More variables are found in defaults/main.yml, and of most them are used with the tint2.j2 template.

## Dependencies

None

## Example Playbook

```
- hosts: all
  roles:
     - { role: avnes.ansible-role-tint2, config_owner: 'maya' }
```

## Test

```
ANSIBLE_CONFIG=./role.cfg; export ANSIBLE_CONFIG
ansible-playbook -i tests/inventory --syntax-check role.yml
ansible-playbook -i tests/inventory --check --connection=local --sudo -vvvv role.yml -K
```

## Molecule test

```
molecule create
molecule test
```

## Run

```
ANSIBLE_CONFIG=./role.cfg; export ANSIBLE_CONFIG
ansible-playbook -i tests/inventory --connection=local --sudo -vvvv role.yml -K
```

## License

MIT

## Author Information

<https://github.com/avnes>
