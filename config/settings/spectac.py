from .base import INSTALLED_APPS

INSTALLED_APPS += [
    'drf_spectacular',
]
SPECTACULAR_SETTINGS = {
    'TITLE': 'Project API',
    'DESCRIPTION': 'API for project',
    'VERSION': '1.0.0',

    'SERVE_PERMISSIONS': ['rest_framework.permissions.AllowAny'],

    'SERVE_AUTHENTICATION': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    # 'SERVE_INCLUDE_SCHEMA': False,

    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'displayOperationId': True,
    },

    'COMPONENT_SPLIT_REQUEST': True,
    'SORT_OPERATION': False,
    # 'COMPONENT_SPLIT_RESPONSE': True,
    # 'COMPONENT_SPLIT_ENDPOINTS': True,
    # 'TAGS': [
    #     {'name': 'users', 'description': 'Users endpoints'},
    #     {'name': 'groups', 'description': 'Groups endpoints'},
    #     {'name': 'common', 'description': 'Common endpoints'},
    # ],
    # 'DEFAULT_GENERATOR_CLASS': 'drf_spectacular.generators.SchemaGenerator',
    # 'SECURITY': [
    #     {
    #         'Basic': [],
    #     },
    # ],
    # 'SCHEMA_PATH_PREFIX': r'/api/v[0-9]',
    # 'SCHEMA_PATH_PREFIX_TRIM': r'/api/v[0-9]',
    # 'SCHEMA_PATH_PREFIX_TRIM': r'/api/v[0-9]',
    # 'SCHEMA_PATH_PREFIX_TRIM': r'/api/v[0-9]',
    # 'SCHEMA_PATH_PREFIX_TRIM': r'/api/v[0-9]',
    # 'SCHEMA_PATH_PREFIX_TRIM': r'/api/v[0-9]',
    # 'SCHEMA_PATH_PREFIX_TRIM': r'/api/v[0-9]',


}
