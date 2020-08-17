# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration_async import FootprintMonitoringManagementClientConfiguration
from .operations_async import OperationOperations
from .operations_async import ProfileOperations
from .operations_async import MeasurementEndpointOperations
from .operations_async import MeasurementEndpointConditionOperations
from .operations_async import ExperimentOperations
from .. import models


class FootprintMonitoringManagementClient(object):
    """Microsoft Footprint active monitoring system REST API version 2020-02-01-preview.

    :ivar operation: OperationOperations operations
    :vartype operation: footprint_monitoring_management_client.aio.operations_async.OperationOperations
    :ivar profile: ProfileOperations operations
    :vartype profile: footprint_monitoring_management_client.aio.operations_async.ProfileOperations
    :ivar measurement_endpoint: MeasurementEndpointOperations operations
    :vartype measurement_endpoint: footprint_monitoring_management_client.aio.operations_async.MeasurementEndpointOperations
    :ivar measurement_endpoint_condition: MeasurementEndpointConditionOperations operations
    :vartype measurement_endpoint_condition: footprint_monitoring_management_client.aio.operations_async.MeasurementEndpointConditionOperations
    :ivar experiment: ExperimentOperations operations
    :vartype experiment: footprint_monitoring_management_client.aio.operations_async.ExperimentOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = FootprintMonitoringManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.profile = ProfileOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.measurement_endpoint = MeasurementEndpointOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.measurement_endpoint_condition = MeasurementEndpointConditionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.experiment = ExperimentOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "FootprintMonitoringManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
