#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: mikhail_create_file

short_description: This module creates a file

version_added: "1.0.0"

description: This module creates a file

options:
    path:
        description: path to the file.
        required: true
        type: str
    content:
        description: content of the file
        required: true
        type: str

author:
    - Mikhail Pastushenko (@MikhailPastushenko)
'''

EXAMPLES = r'''
- name: Test file 
  mikhail_namespace.mikhail_collection.mikhail_create_file:
    path: /test/ansible-filetest
    content: test file
'''

RETURN = r'''

'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    module.params['path'] = "/tmp/testfile"
    module.params['content'] = "hello"

    with open(module.params['path'], 'w') as f:
        f.write(module.params['content'])

    result['changed'] = True

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
