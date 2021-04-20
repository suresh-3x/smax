from setuptools import setup, find_packages


setup_args = dict(
    name='smax',
    version='0.0.1',
    description='Useful tools to work with Elastic stack in Python',
    long_description_content_type="text/markdown",
    long_description="Nothing",
    license='MIT',
    packages=find_packages(),
    author='Suresh-3x',
    author_email='suresh.37x@gmail.com',
    keywords=['Elastic', 'ElasticSearch', 'ElasticStack'],
    url='https://github.com/suresh-3x/smax',
    download_url='https://github.com/suresh-3x/smax'
)

install_requires = [
   
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)