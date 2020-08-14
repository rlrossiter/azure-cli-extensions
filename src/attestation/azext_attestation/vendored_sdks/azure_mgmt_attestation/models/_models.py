# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class Resource(msrest.serialization.Model):
    """Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.location = kwargs['location']


class AttestationProvider(TrackedResource):
    """Attestation service response message.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. Ex- Microsoft.Compute/virtualMachines or
     Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param location: Required. The geo-location where the resource lives.
    :type location: str
    :param trust_model: Trust model for the attestation service instance.
    :type trust_model: str
    :param status: Required. Status of attestation service. Possible values include: "Ready",
     "NotReady", "Error".
    :type status: str or ~azure.mgmt.attestation.models.AttestationServiceStatus
    :param attest_uri: Gets the uri of attestation service.
    :type attest_uri: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'status': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'trust_model': {'key': 'properties.trustModel', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'attest_uri': {'key': 'properties.attestUri', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AttestationProvider, self).__init__(**kwargs)
        self.trust_model = kwargs.get('trust_model', None)
        self.status = kwargs['status']
        self.attest_uri = kwargs.get('attest_uri', None)


class AttestationProviderListResult(msrest.serialization.Model):
    """Attestation Providers List.

    :param value: Attestation Provider array.
    :type value: list[~azure.mgmt.attestation.models.AttestationProvider]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[AttestationProvider]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AttestationProviderListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class AttestationServiceCreationParams(msrest.serialization.Model):
    """Parameters for creating an attestation service instance.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The supported Azure location where the attestation service instance
     should be created.
    :type location: str
    :param tags: A set of tags. The tags that will be assigned to the attestation service instance.
    :type tags: dict[str, str]
    :param attestation_policy: Name of attestation policy.
    :type attestation_policy: str
    :param keys: The value of the "keys" parameter is an array of JWK values.  By
     default, the order of the JWK values within the array does not imply
     an order of preference among them, although applications of JWK Sets
     can choose to assign a meaning to the order for their purposes, if
     desired.
    :type keys: list[~azure.mgmt.attestation.models.JsonWebKey]
    """

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'attestation_policy': {'key': 'properties.attestationPolicy', 'type': 'str'},
        'keys': {'key': 'properties.policySigningCertificates.keys', 'type': '[JsonWebKey]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AttestationServiceCreationParams, self).__init__(**kwargs)
        self.location = kwargs['location']
        self.tags = kwargs.get('tags', None)
        self.attestation_policy = kwargs.get('attestation_policy', None)
        self.keys = kwargs.get('keys', None)


class AttestationServicePatchParams(msrest.serialization.Model):
    """Parameters for patching an attestation service instance.

    :param tags: A set of tags. The tags that will be assigned to the attestation service instance.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AttestationServicePatchParams, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)


class CloudErrorBody(msrest.serialization.Model):
    """An error response from Attestation.

    :param code: An identifier for the error. Codes are invariant and are intended to be consumed
     programmatically.
    :type code: str
    :param message: A message describing the error, intended to be suitable for displaying in a
     user interface.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class JsonWebKey(msrest.serialization.Model):
    """JsonWebKey.

    All required parameters must be populated in order to send to Azure.

    :param alg: The "alg" (algorithm) parameter identifies the algorithm intended for
     use with the key.  The values used should either be registered in the
     IANA "JSON Web Signature and Encryption Algorithms" registry
     established by [JWA] or be a value that contains a Collision-
     Resistant Name.
    :type alg: str
    :param crv: The "crv" (curve) parameter identifies the curve type.
    :type crv: str
    :param d: RSA private exponent or ECC private key.
    :type d: str
    :param dp: RSA Private Key Parameter.
    :type dp: str
    :param dq: RSA Private Key Parameter.
    :type dq: str
    :param e: RSA public exponent, in Base64.
    :type e: str
    :param k: Symmetric key.
    :type k: str
    :param kid: The "kid" (key ID) parameter is used to match a specific key.  This
     is used, for instance, to choose among a set of keys within a JWK Set
     during key rollover.  The structure of the "kid" value is
     unspecified.  When "kid" values are used within a JWK Set, different
     keys within the JWK Set SHOULD use distinct "kid" values.  (One
     example in which different keys might use the same "kid" value is if
     they have different "kty" (key type) values but are considered to be
     equivalent alternatives by the application using them.)  The "kid"
     value is a case-sensitive string.
    :type kid: str
    :param kty: Required. The "kty" (key type) parameter identifies the cryptographic algorithm
     family used with the key, such as "RSA" or "EC". "kty" values should
     either be registered in the IANA "JSON Web Key Types" registry
     established by [JWA] or be a value that contains a Collision-
     Resistant Name.  The "kty" value is a case-sensitive string.
    :type kty: str
    :param n: RSA modulus, in Base64.
    :type n: str
    :param p: RSA secret prime.
    :type p: str
    :param q: RSA secret prime, with p < q.
    :type q: str
    :param qi: RSA Private Key Parameter.
    :type qi: str
    :param use: Use ("public key use") identifies the intended use of
     the public key. The "use" parameter is employed to indicate whether
     a public key is used for encrypting data or verifying the signature
     on data. Values are commonly "sig" (signature) or "enc" (encryption).
    :type use: str
    :param x: X coordinate for the Elliptic Curve point.
    :type x: str
    :param x5_c: The "x5c" (X.509 certificate chain) parameter contains a chain of one
     or more PKIX certificates [RFC5280].  The certificate chain is
     represented as a JSON array of certificate value strings.  Each
     string in the array is a base64-encoded (Section 4 of [RFC4648] --
     not base64url-encoded) DER [ITU.X690.1994] PKIX certificate value.
     The PKIX certificate containing the key value MUST be the first
     certificate.
    :type x5_c: list[str]
    :param y: Y coordinate for the Elliptic Curve point.
    :type y: str
    """

    _validation = {
        'kty': {'required': True},
    }

    _attribute_map = {
        'alg': {'key': 'alg', 'type': 'str'},
        'crv': {'key': 'crv', 'type': 'str'},
        'd': {'key': 'd', 'type': 'str'},
        'dp': {'key': 'dp', 'type': 'str'},
        'dq': {'key': 'dq', 'type': 'str'},
        'e': {'key': 'e', 'type': 'str'},
        'k': {'key': 'k', 'type': 'str'},
        'kid': {'key': 'kid', 'type': 'str'},
        'kty': {'key': 'kty', 'type': 'str'},
        'n': {'key': 'n', 'type': 'str'},
        'p': {'key': 'p', 'type': 'str'},
        'q': {'key': 'q', 'type': 'str'},
        'qi': {'key': 'qi', 'type': 'str'},
        'use': {'key': 'use', 'type': 'str'},
        'x': {'key': 'x', 'type': 'str'},
        'x5_c': {'key': 'x5c', 'type': '[str]'},
        'y': {'key': 'y', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(JsonWebKey, self).__init__(**kwargs)
        self.alg = kwargs.get('alg', None)
        self.crv = kwargs.get('crv', None)
        self.d = kwargs.get('d', None)
        self.dp = kwargs.get('dp', None)
        self.dq = kwargs.get('dq', None)
        self.e = kwargs.get('e', None)
        self.k = kwargs.get('k', None)
        self.kid = kwargs.get('kid', None)
        self.kty = kwargs['kty']
        self.n = kwargs.get('n', None)
        self.p = kwargs.get('p', None)
        self.q = kwargs.get('q', None)
        self.qi = kwargs.get('qi', None)
        self.use = kwargs.get('use', None)
        self.x = kwargs.get('x', None)
        self.x5_c = kwargs.get('x5_c', None)
        self.y = kwargs.get('y', None)


class OperationList(msrest.serialization.Model):
    """List of supported operations.

    :param value: List of supported operations.
    :type value: list[~azure.mgmt.attestation.models.OperationsDefinition]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OperationsDefinition]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class OperationsDefinition(msrest.serialization.Model):
    """Definition object with the name and properties of an operation.

    :param name: Name of the operation.
    :type name: str
    :param display: Display object with properties of the operation.
    :type display: ~azure.mgmt.attestation.models.OperationsDisplayDefinition
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationsDisplayDefinition'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationsDefinition, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)


class OperationsDisplayDefinition(msrest.serialization.Model):
    """Display object with properties of the operation.

    :param provider: Resource provider of the operation.
    :type provider: str
    :param resource: Resource for the operation.
    :type resource: str
    :param operation: Short description of the operation.
    :type operation: str
    :param description: Description of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationsDisplayDefinition, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)
