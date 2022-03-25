from tecton import Entity


user = Entity(
    name='fraud_user',
    default_join_keys=['USER_ID'],
    description='A user of the platform',
    family='fraud',
    owner='matt@tecton.ai',
    tags={'release': 'production'}
)

merchant = Entity(
    name='merchant',
    default_join_keys=['MERCHANT'],
    description='A  merchant',
    family='fraud',
    owner='david@tecton.ai',
    tags={'release': 'production'}
)


category = Entity(
    name='category',
    default_join_keys=['CATEGORY'],
    description='A purchase category',
    family='fraud',
    owner='david@tecton.ai',
    tags={'release': 'production'}
)
