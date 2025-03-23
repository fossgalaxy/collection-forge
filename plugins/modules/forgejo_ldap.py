#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_test

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    new:
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: bool
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.my_test:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_namespace.my_collection.my_test:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_namespace.my_collection.my_test:
    name: fail me
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule
import ansible_collections.fossgalaxy.forge.plugins.module_utils.forgejo.forgejo_podman as forgejo_common

import requests

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        hostname=dict(type='str', required=True),
        search_base=dict(type='str', required=True),

#        port=dict(type='int', required=False),

        # bind account
        bind_dn=dict(type='str', required=True),
        bind_password=dict(type='str', required=True),

        # attributes (FreeIPA defaults)
#        attr_username=dict(type='str', required=False),
#        attr_email=dict(type='str', required=False),
#        attr_firstname=dict(type='str', required=False),
#        attr_surname=dict(type='str', required=False),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        account={},
        resp={}
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    sources = forgejo_common.get_auth_sources(module)
    for source in sources:
        if len(source) > 1 and source[1] == 'freeipa':
            result['changed'] = False
            module.exit_json(**result)
            return

    # execute the command
    result['account'] = forgejo_common.create_ldap(module, 
                                                   module.params['hostname'],
                                                   module.params['search_base'],
                                                   bind_dn=module.params['bind_dn'],
                                                   bind_pass=module.params['bind_password'],
                                                   )
    result['changed'] = True

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
