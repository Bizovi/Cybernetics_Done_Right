"""Setup script for installing game of life."""

from setuptools import find_packages, setup


setup(
    name='game_of_life',
    version=0.1,
    description='Implementation of game of life with TDD'
                'run and visualize the game.',
    url='http://github.com/bizovi/cybernetics_done_right/game_of_life',
    author='Joseph Moukarzel',
    maintainer='Bizovi Mihai',
    license='MIT',

    classifiers=['Development Status :: 4 - Prototype',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Topic :: Scientific/Engineering',
                 'Topic :: Scientific/Engineering :: Cellular Automata',
                 'Intended Audience :: Science/Research',
                 'Operating System :: OS Independent'],
    keywords='cellular automata',
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
    install_requires=['matplotlib>=3.0.3', 'numpy>=1.16.2', 'Pillow>=5.4.1'],
    extras_require={
        'test': ['pytest>=4.3.1', 'pytest-runner', 'pytest-flake8']
    },
    zip_safe=True)
