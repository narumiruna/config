from setuptools import find_packages, setup


def main():
    setup(
        name='mlconfig',
        version='0.1.6',
        author='Narumi',
        author_email='weaper@gamil.com',
        packages=find_packages(),
        install_requires=['pyyaml'],
    )


if __name__ == "__main__":
    main()
