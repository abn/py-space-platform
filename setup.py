"""
DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER

Copyright (c) 2015 Juniper Networks, Inc.
All rights reserved.

Use is subject to license terms.

Licensed under the Apache License, Version 2.0 (the ?License?); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at http://www.apache.org/licenses/LICENSE-2.0.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations
under the License.
"""
from setuptools import setup, find_packages

setup(name='space-ez',
      version='0.0.2',
      author='Roshan Joyce',
      author_email='rjoyce@juniper.net',
      packages=find_packages(),
      package_data={'jnpr.space': ['descriptions/*.*',
                                   'descriptions/apps/servicenow/*.*',
                                   'descriptions/apps/serviceinsight/*.*',
                                   'templates/*.*']},
      install_requires=['requests>=2.5.1',
                        'lxml>=3.3.5',
                        'PyYAML>=3.11',
                        'pytest>=2.5.2',
                        'jinja2>=2.7.3']
      )
