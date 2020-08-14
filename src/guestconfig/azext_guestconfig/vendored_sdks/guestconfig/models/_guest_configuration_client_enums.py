# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class ActionAfterReboot(str, Enum):
    """Specifies what happens after a reboot during the application of a configuration. The possible
    values are ContinueConfiguration and StopConfiguration
    """

    continue_configuration = "ContinueConfiguration"
    stop_configuration = "StopConfiguration"

class AllowModuleOverwrite(str, Enum):
    """If true - new configurations downloaded from the pull service are allowed to overwrite the old
    ones on the target node. Otherwise, false
    """

    true = "True"
    false = "False"

class ComplianceStatus(str, Enum):
    """A value indicating compliance status of the machine for the assigned guest configuration.
    """

    compliant = "Compliant"
    non_compliant = "NonCompliant"
    pending = "Pending"

class ConfigurationMode(str, Enum):
    """Specifies how the LCM(Local Configuration Manager) actually applies the configuration to the
    target nodes. Possible values are ApplyOnly, ApplyAndMonitor, and ApplyAndAutoCorrect.
    """

    apply_only = "ApplyOnly"
    apply_and_monitor = "ApplyAndMonitor"
    apply_and_auto_correct = "ApplyAndAutoCorrect"

class ProvisioningState(str, Enum):
    """The provisioning state, which only appears in the response.
    """

    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    created = "Created"

class RebootIfNeeded(str, Enum):
    """Set this to true to automatically reboot the node after a configuration that requires reboot is
    applied. Otherwise, you will have to manually reboot the node for any configuration that
    requires it. The default value is false. To use this setting when a reboot condition is enacted
    by something other than DSC (such as Windows Installer), combine this setting with the
    xPendingReboot module.
    """

    true = "True"
    false = "False"

class Type(str, Enum):
    """Type of report, Consistency or Initial
    """

    consistency = "Consistency"
    initial = "Initial"
