# Alfred Ansible Workflow

An [Alfred](https://www.alfredapp.com) workflow to search the [Ansible module documentation](https://docs.ansible.com/ansible/latest/index.html#).

![Alfred window showing the ansible workflow](./img/alfred_ansible.png)


### Requirements

As macOS still ships [Python 2 which is no longer supported since January 1st, 2020](https://www.python.org/doc/sunset-python-2/#:~:text=The%20sunset%20date%20has%20now,when%20we%20released%20Python%202.7.) - Python 3 is required to be installed. The workflow uses the Python 3 interpreter returned by `/usr/bin/env python3` so the installation method won't matter. Only the following modules from the standard library are used:

* json
* requests
* sys
* re

However, i do recommend the usage of [homebrew](https://docs.brew.sh/Homebrew-and-Python). The CI tests cover python version up from `3.5`.

## Usage

The workflow is triggered using the keyword `ansible` and will use the following input as search parameters.

![Workflow searching for lineinfile](./img/alfred_ansible_usage.png)

Pressing `enter` on any of the results will open the corresponding documentation page in the default browser.

![Safari window with the builtin.lineinfile module documentation](./img/alfred_ansible_browser.png)
