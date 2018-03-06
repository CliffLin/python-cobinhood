from setuptools import setup
setup(name='cobinhood',
      version='0.1.0',
      description='Cobinhood API',
      url='https://github.com/CliffLin/python-cobinhood',
      author='zylin',
      packages=['cobinhood', 'cobinhood/ws', 'cobinhood/http'],
      install_requires=['requests', 'websocket-client', 'coloredlogs'],
      zip_safe=False)
