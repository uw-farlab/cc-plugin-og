# OG Compliance Checker Plugin

This is a checker for [OG](https://oceangliderscommunity.github.io/OG-format-user-manual/OG_Format.html) compliance

It works with the [IOOS Compliance Checker](https://github.com/ioos/compliance-checker)

**Note this code is in a pre-release state. Check back soon for the first release**

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Please see LICENSE for the full license text.

For a brief overview of the attributes the OG Checker runs through, check [here](/checks.md).

## Installation

#### Clone this project

```bash
$ git clone git@github.com:ioos/cc-plugin-og.git
$ cd cc-plugin-og
$ python setup.py install
```

#### Tests should now show up when you run compliance checker
```bash
$ compliance-checker -l

IOOS compliance checker available checker suites (code version):
 - OG (0.0.1-dev)
 - OG:1.0 (0.0.1-dev)
 - OG:latest (0.0.1-dev)
 - acdd (3.1.1)
 - acdd:1.1 (3.1.1)
 - acdd:1.3 (3.1.1)
 - acdd:latest (3.1.1)
 - cf (3.1.1)
 - cf:1.6 (3.1.1)
 - cf:latest (3.1.1)
 - ioos (3.1.1)
 - ioos:0.1 (3.1.1)
 - ioos:1.1 (3.1.1)
 - ioos:latest (3.1.1)
 - ioos_sos (3.1.1)
 - ioos_sos:0.1 (3.1.1)
 - ioos_sos:latest (3.1.1)
 ```
