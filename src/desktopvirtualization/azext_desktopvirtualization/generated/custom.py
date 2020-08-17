# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=unused-argument


def desktopvirtualization_workspace_list(client,
                                         resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list_by_subscription()


def desktopvirtualization_workspace_show(client,
                                         resource_group_name,
                                         workspace_name):
    return client.get(resource_group_name=resource_group_name,
                      workspace_name=workspace_name)


def desktopvirtualization_workspace_create(client,
                                           resource_group_name,
                                           workspace_name,
                                           location,
                                           tags=None,
                                           description=None,
                                           friendly_name=None,
                                           application_group_references=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   workspace_name=workspace_name,
                                   tags=tags,
                                   location=location,
                                   description=description,
                                   friendly_name=friendly_name,
                                   application_group_references=application_group_references)


def desktopvirtualization_workspace_update(client,
                                           resource_group_name,
                                           workspace_name,
                                           tags=None,
                                           description=None,
                                           friendly_name=None,
                                           application_group_references=None):
    return client.update(resource_group_name=resource_group_name,
                         workspace_name=workspace_name,
                         tags=tags,
                         description=description,
                         friendly_name=friendly_name,
                         application_group_references=application_group_references)


def desktopvirtualization_workspace_delete(client,
                                           resource_group_name,
                                           workspace_name):
    return client.delete(resource_group_name=resource_group_name,
                         workspace_name=workspace_name)


def desktopvirtualization_applicationgroup_list(client,
                                                resource_group_name=None,
                                                filter=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name,
                                             filter=filter)
    return client.list_by_subscription(filter=filter)


def desktopvirtualization_applicationgroup_show(client,
                                                resource_group_name,
                                                application_group_name):
    return client.get(resource_group_name=resource_group_name,
                      application_group_name=application_group_name)


def desktopvirtualization_applicationgroup_create(client,
                                                  resource_group_name,
                                                  application_group_name,
                                                  location,
                                                  host_pool_arm_path,
                                                  application_group_type,
                                                  tags=None,
                                                  description=None,
                                                  friendly_name=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   application_group_name=application_group_name,
                                   tags=tags,
                                   location=location,
                                   description=description,
                                   friendly_name=friendly_name,
                                   host_pool_arm_path=host_pool_arm_path,
                                   application_group_type=application_group_type)


def desktopvirtualization_applicationgroup_update(client,
                                                  resource_group_name,
                                                  application_group_name,
                                                  tags=None,
                                                  description=None,
                                                  friendly_name=None):
    return client.update(resource_group_name=resource_group_name,
                         application_group_name=application_group_name,
                         tags=tags,
                         description=description,
                         friendly_name=friendly_name)


def desktopvirtualization_applicationgroup_delete(client,
                                                  resource_group_name,
                                                  application_group_name):
    return client.delete(resource_group_name=resource_group_name,
                         application_group_name=application_group_name)


def desktopvirtualization_hostpool_list(client,
                                        resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list()


def desktopvirtualization_hostpool_show(client,
                                        resource_group_name,
                                        host_pool_name):
    return client.get(resource_group_name=resource_group_name,
                      host_pool_name=host_pool_name)


def desktopvirtualization_hostpool_create(client,
                                          resource_group_name,
                                          host_pool_name,
                                          location,
                                          host_pool_type,
                                          personal_desktop_assignment_type,
                                          load_balancer_type,
                                          tags=None,
                                          friendly_name=None,
                                          description=None,
                                          custom_rdp_property=None,
                                          max_session_limit=None,
                                          ring=None,
                                          validation_environment=None,
                                          registration_info=None,
                                          vm_template=None,
                                          sso_context=None):
    return client.create_or_update(resource_group_name=resource_group_name,
                                   host_pool_name=host_pool_name,
                                   tags=tags,
                                   location=location,
                                   friendly_name=friendly_name,
                                   description=description,
                                   host_pool_type=host_pool_type,
                                   personal_desktop_assignment_type=personal_desktop_assignment_type,
                                   custom_rdp_property=custom_rdp_property,
                                   max_session_limit=max_session_limit,
                                   load_balancer_type=load_balancer_type,
                                   ring=ring,
                                   validation_environment=validation_environment,
                                   registration_info=registration_info,
                                   vm_template=vm_template,
                                   sso_context=sso_context)


def desktopvirtualization_hostpool_update(client,
                                          resource_group_name,
                                          host_pool_name,
                                          tags=None,
                                          friendly_name=None,
                                          description=None,
                                          custom_rdp_property=None,
                                          max_session_limit=None,
                                          personal_desktop_assignment_type=None,
                                          load_balancer_type=None,
                                          ring=None,
                                          validation_environment=None,
                                          registration_info=None,
                                          sso_context=None):
    return client.update(resource_group_name=resource_group_name,
                         host_pool_name=host_pool_name,
                         tags=tags,
                         friendly_name=friendly_name,
                         description=description,
                         custom_rdp_property=custom_rdp_property,
                         max_session_limit=max_session_limit,
                         personal_desktop_assignment_type=personal_desktop_assignment_type,
                         load_balancer_type=load_balancer_type,
                         ring=ring,
                         validation_environment=validation_environment,
                         registration_info=registration_info,
                         sso_context=sso_context)


def desktopvirtualization_hostpool_delete(client,
                                          resource_group_name,
                                          host_pool_name,
                                          force=None):
    return client.delete(resource_group_name=resource_group_name,
                         host_pool_name=host_pool_name,
                         force=force)
