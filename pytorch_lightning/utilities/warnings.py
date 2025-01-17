# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pytorch_lightning.utilities.distributed import rank_zero_deprecation, rank_zero_warn


class WarningCache(set):

    def warn(self, m, *args, **kwargs):
        if m not in self:
            self.add(m)
            rank_zero_warn(m, *args, **kwargs)

    def deprecation(self, m, *args, **kwargs):
        if m not in self:
            self.add(m)
            rank_zero_deprecation(m, *args, **kwargs)
