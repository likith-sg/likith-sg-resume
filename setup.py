from setuptools import setup, find_packages

setup(
    name='likith-sg-resume',
    version='0.1',
    packages=find_packages(),
    description='Likith SG Resume Package',
    author='Likith SG',
    author_email='likithsg1@gmail.com',
    url='https://github.com/likith-sg/likith-sg-resume',  
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_data={
        'likith_sg_resume': ['likith-sg-resume.pdf'],  
    },
)

