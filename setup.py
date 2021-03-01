from distutils.core import setup

setup(
    name="simpletokenizer",
    author="Ali Safaya",
    packages = ['simpletokenizer'],
    version='0.1',
    author_email="alisafaya@gmail.com",
    long_description=open("README.md", "r", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    download_url='https://github.com/tdd-ai/simple-tokenizer/archive/v_01.tar.gz',
    install_requires=[],
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)