from distutils.core import setup

setup(
    name='PayZippySDK',
    version='0.1.0',
    author='PayZippy',
    author_email='merchant.care@payzippy.com',
    packages=['payzippysdk'],
    url='https://www.payzippy.com/developers',
    license='LICENSE.txt',
    description='PayZippy SDK for Python.',
    long_description=open('README.md').read(),
    install_requires=[
        "Python >= 2.5.6",
    ],
)
