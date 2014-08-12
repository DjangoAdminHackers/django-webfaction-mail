import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-webfaction-email',
    version='0.6',
    description="A Django app to provide a simple admin interface"
                "to Webfaction's email account API.",
    long_description=read('README.rst'),
    author='Andy Baker',
    author_email='andy@andybak.net',
    license='BSD',
    url='http://github.com/andybak/django-webfaction-mail/',
    packages=[
        'django_webfaction_mail',
    ],
    package_data={
        'django_webfaction_mail': [
            'templates/*.html',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
