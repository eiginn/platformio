# Copyright 2014-2016 Ivan Kravets <me@ikravets.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
import requests

from platformio.util import get_api_result


def pytest_generate_tests(metafunc):
    if "package_data" not in metafunc.fixturenames:
        return
    pkgs_manifest = get_api_result("/packages/manifest")
    assert isinstance(pkgs_manifest, dict)
    packages = []
    for _, variants in pkgs_manifest.iteritems():
        for item in variants:
            packages.append(item)
    metafunc.parametrize("package_data", packages)


def validate_response(req):
    assert req.status_code == 200
    assert int(req.headers['Content-Length']) > 0
    assert req.headers['Content-Type'] in ("application/gzip",
                                           "application/octet-stream")


def test_package(package_data):
    assert package_data['url'].endswith("%d.tar.gz" % package_data['version'])

    r = requests.head(package_data['url'], allow_redirects=True)
    validate_response(r)

    if "X-Checksum-Sha1" not in r.headers:
        return pytest.skip("X-Checksum-Sha1 is not provided")

    assert package_data['sha1'] == r.headers.get("X-Checksum-Sha1")
