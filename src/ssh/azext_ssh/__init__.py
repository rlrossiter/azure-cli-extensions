# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader
from knack.help_files import helps

helps['ssh'] = """
    type: command
    short-summary: SSH into Azure VMs
    examples:
        - name: Give a resource group and VM to SSH
          text: |
            az ssh --resource-group [group] --name [vmName] : az ssh --resource-group mygroup --name myvm
"""


class SshCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType

        ssh_vm_custom = CliCommandType(
            operations_tmpl='azext_ssh.custom#{}')
        super(SshCommandsLoader, self).__init__(
            cli_ctx=cli_ctx, custom_command_type=ssh_vm_custom)

    def load_command_table(self, _):
        with self.command_group('') as g:
            g.custom_command('ssh', 'ssh_vm')
        return self.command_table

    def load_arguments(self, _):
        with self.argument_context('ssh') as c:
            c.argument('resource_group', options_list=['--resource-group'])
            c.argument('vm_name', options_list=['--name'])
            c.extra('public_key_file', options_list=['--public-key-file'])
            c.extra('private_key_file', options_list=['--private-key-file'])


COMMAND_LOADER_CLS = SshCommandsLoader