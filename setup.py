from setuptools import setup
with open('README.md', encoding='utf-8') as f: # README 내용 읽어오기
    long_description = f.read()
setup(
    name='juu',
    version='0.2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='test',
    author='Huiju Kim',
    author_email='ayanaloey1127@gmail.com',
    url='',#깃허브 주소
    install_requires=[],
    packages=['juu'],
    keywords=['torch'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifires=[
        'Programing Language :: python :: 3',
        'Programing Language :: python :: 3.6',
        'Programing Language :: Python :: 3.7',
    ],
)
