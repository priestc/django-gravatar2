from distutils.core import setup
 
setup(
    name='django-gravatar2',
    version='0.2.0',
    description='Gravatar Support in a Django Reusable Application',
    author='Chris Priest',
    author_email='nbvfour@gmail.com',
    url='http://github.com/nbv4/django-gravatar2',
    packages=[
        'gravatar',
        'gravatar.templatetags',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)

