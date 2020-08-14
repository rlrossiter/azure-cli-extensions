# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class ExperimentOperations(object):
    """ExperimentOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~footprint_monitoring_management_client.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_by_profile(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.ExperimentList"]
        """Retrieves the information about all experiments under a Footprint profile.

        Get all experiments under a Footprint profile.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param profile_name: Name of the Footprint profile resource.
        :type profile_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ExperimentList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~footprint_monitoring_management_client.models.ExperimentList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.ExperimentList"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-02-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_profile.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
                    'profileName': self._serialize.url("profile_name", profile_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('ExperimentList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.DefaultErrorResponse, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_profile.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FootprintMonitoring/profiles/{profileName}/experiments'}  # type: ignore

    def get(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        experiment_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Experiment"
        """Retrieves the information about a single Footprint experiment.

        Get a Footprint experiment resource.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param profile_name: Name of the Footprint profile resource.
        :type profile_name: str
        :param experiment_name: Name of the Footprint experiment resource.
        :type experiment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Experiment, or the result of cls(response)
        :rtype: ~footprint_monitoring_management_client.models.Experiment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Experiment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-02-01-preview"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'profileName': self._serialize.url("profile_name", profile_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]'),
            'experimentName': self._serialize.url("experiment_name", experiment_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DefaultErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Experiment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FootprintMonitoring/profiles/{profileName}/experiments/{experimentName}'}  # type: ignore

    def create_or_update(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        experiment_name,  # type: str
        description=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Experiment"
        """Creates or updates a Footprint experiment with the specified properties.

        Creates or updates a Footprint experiment resource.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param profile_name: Name of the Footprint profile resource.
        :type profile_name: str
        :param experiment_name: Name of the Footprint experiment resource.
        :type experiment_name: str
        :param description: The description of a Footprint experiment.
        :type description: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Experiment, or the result of cls(response)
        :rtype: ~footprint_monitoring_management_client.models.Experiment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Experiment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _parameters = models.Experiment(description=description)
        api_version = "2020-02-01-preview"
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'profileName': self._serialize.url("profile_name", profile_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]'),
            'experimentName': self._serialize.url("experiment_name", experiment_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_parameters, 'Experiment')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DefaultErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Experiment', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Experiment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FootprintMonitoring/profiles/{profileName}/experiments/{experimentName}'}  # type: ignore

    def delete(
        self,
        resource_group_name,  # type: str
        profile_name,  # type: str
        experiment_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes an existing Footprint experiment.

        Deletes a Footprint experiment resource.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param profile_name: Name of the Footprint profile resource.
        :type profile_name: str
        :param experiment_name: Name of the Footprint experiment resource.
        :type experiment_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-02-01-preview"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
            'profileName': self._serialize.url("profile_name", profile_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]'),
            'experimentName': self._serialize.url("experiment_name", experiment_name, 'str', max_length=64, min_length=5, pattern=r'^[a-zA-Z0-9]'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.DefaultErrorResponse, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.FootprintMonitoring/profiles/{profileName}/experiments/{experimentName}'}  # type: ignore
