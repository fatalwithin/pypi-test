import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='pypi-test',  

     version='0.2',

     scripts=['pypi-test'] ,

     author="Andre",

     author_email="fatalwithin@gmail.com",

     description="PyPi private repo test",

     long_description=long_description,

   long_description_content_type="text/markdown",

     url="https://github.com/fatalwithin/pypi-test",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )