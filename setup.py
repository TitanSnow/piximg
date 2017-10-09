from setuptools import setup


setup(
    name='piximg',
    version='0.1.dev1',
    packages=('piximg',),
    install_requires=('docutils',),

    author="TitanSnow",
    author_email="tttnns1024@gmail.com",
    url='https://github.com/TitanSnow/piximg',
    description='A sphinx extension to insert images from pixiv.net to doc',
    long_description=open('README.rst').read(),
    license="MIT License",
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
    ),
)
