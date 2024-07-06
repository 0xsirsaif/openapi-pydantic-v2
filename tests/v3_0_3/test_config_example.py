from openapi_pydantic_v2.v3.v3_0_3 import (
    XML,
    Callback,
    Components,
    Contact,
    Discriminator,
    Encoding,
    Example,
    ExternalDocumentation,
    Header,
    Info,
    License,
    Link,
    MediaType,
    OAuthFlow,
    OAuthFlows,
    OpenAPI,
    Operation,
    Parameter,
    PathItem,
    Paths,
    Reference,
    RequestBody,
    Response,
    Responses,
    Schema,
    SecurityRequirement,
    SecurityScheme,
    Server,
    ServerVariable,
    Tag,
)


def test_config_example():
    all_types = [
        OpenAPI,
        Info,
        Contact,
        License,
        Server,
        ServerVariable,
        Components,
        Paths,
        PathItem,
        Operation,
        ExternalDocumentation,
        Parameter,
        RequestBody,
        MediaType,
        Encoding,
        Responses,
        Response,
        Callback,
        Example,
        Link,
        Header,
        Tag,
        Reference,
        Schema,
        Discriminator,
        XML,
        SecurityScheme,
        OAuthFlows,
        OAuthFlow,
        SecurityRequirement,
    ]
    for schema_type in all_types:
        _assert_config_examples(schema_type)


def _assert_config_examples(schema_type):
    if getattr(schema_type, "Config", None) and getattr(
        schema_type.Config, "schema_extra", None
    ):
        examples = schema_type.Config.schema_extra.get("examples")
        for example_dict in examples:
            obj = schema_type(**example_dict)
            assert obj.model_fields_set
