from setuptools import find_packages
from setuptools import setup

package_name = 'vector_ros_driver'

setup(
    name=package_name,
    version='2.0.0',
    packages=['vector_ros_driver'],
    install_requires=[
        'setuptools',
        'anki_vector',
    ],
    zip_safe=True,
    author='beta_b0t',
    author_email='beta_b0t@yahoo.com',
    keywords=['ROS2', 'Anki Vector'],
    description=(
"""
    Unofficial ROS 2 port of the anki vector robot driver
"""
    ),
    license='MIT',
    entry_points={
        'console_scripts': [
            'vector_node = nodes.vector_node:main',
        ],
    },
)
