# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from pysa import _test_source


class C:
    def foo():  # pyrefly: ignore[bad-function-definition]
        return _test_source()


class C:
    def also_tainted_but_missing_from_analysis():  # pyrefly: ignore[bad-function-definition]
        return _test_source()
