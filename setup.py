import io

from setuptools import find_packages, setup

setup(
    name='midaxupdate',
    version='1.8.12',
    url='http://www.midax.com',
    license='BSD',
    maintainer='Midax',
    maintainer_email='alex.r@midax.com',
    description='Midax Updater',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={        
    },
    install_requires=[
        'astroid',
        'cachetools',
        'certifi',
        'chardet',
        'colorama',        
        'futures',
        'google-api-core',
        'google-api-python-client',
        'google-auth',
        'google-auth-httplib2',
        'google-auth-oauthlib',
        'google-cloud-core',
        'google-cloud-logging',
        'googleapis-common-protos',
        'grpcio',
        'httplib2',
        'idna',
        'isort',
        'lazy-object-proxy',
        'mccabe',     
        'oauthlib',
        'protobuf',
        'pyasn1',
        'pyasn1-modules',
        'pylint',
        'pypiwin32',
        'pytz',
        'pywin32',    
        'requests',
        'requests-oauthlib',
        'rsa',
        'six',
        'typed-ast',
        'uritemplate',
        'urllib3',
        'wrapt',
    ]  
)