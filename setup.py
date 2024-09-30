from setuptools import setup, find_packages

setup(
    name='stats_for_me',  # パッケージ名
    version='0.1',  # バージョン
    description='A package for statistical analysis',
    author='soramiya',
    author_email='your.email@example.com',
    url='https://github.com/soramiya/stats_for_me',
    packages=find_packages(),  # パッケージを自動検出
    install_requires=[  # 依存パッケージ
        'numpy',
        'scipy',
    ],
)