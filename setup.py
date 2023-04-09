from setuptools import setup, find_packages

setup(
  name = 'vit',
  packages = find_packages(exclude=['examples']),
  version = '0.0.1',
  license='MIT',
  description = 'Vision Transformer (ViT) - Pytorch',
  long_description_content_type = 'text/markdown',
  author = 'xrsrke',
  author_email = 'hello@xrs.wtf',
  url = 'https://github.com/xrsrke/vision-transformer',
  keywords = [
    'artificial intelligence',
    'attention mechanism',
    'vision-transformer'
  ],
  install_requires=[
    'einops',
    'torch',
  ],
  setup_requires=[
    'pytest-runner',
  ],
  tests_require=[
    'pytest',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)