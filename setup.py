from distutils.core import setup
setup(
  name = 'pywav',
  packages = ['pywav'], 
  version = '0.1',
  license='GPL',
  description = 'Read and write wav files', 
  author = 'Saisyam Dampuri',                   
  author_email = 'saisyam@saisyam.com', 
  url = 'https://github.com/saisyam/pywav',  
  download_url = 'https://github.com/saisyam/pywav/archive/ver_01.tar.gz', 
  keywords = ['wave', 'wav read', 'wav write'],   
  install_requires=[],            
  classifiers=[
    'Development Status :: 4 - Beta', 
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Utilities',
    'License :: OSI Approved :: GPL License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)