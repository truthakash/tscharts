#(C) Copyright Syd Logan 2019
#(C) Copyright Thousand Smiles Foundation 2019
#
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#
#You may obtain a copy of the License at
#http://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

from __future__ import unicode_literals

from django.db import models

from patient.models import Patient
from clinic.models import Clinic

class XRay(models.Model):
    clinic = models.ForeignKey(Clinic)
    patient = models.ForeignKey(Patient)
    time = models.DateTimeField(auto_now=True)

    FULL = 'f'
    ANTERIORS_AND_BITEWINGS = 'a'
    TYPE_CHOICES = ((FULL, "full"), (ANTERIORS_AND_BITEWINGS, "anteriors_bitewings"))

    type = models.CharField(
        max_length = 1,
        choices = TYPE_CHOICES,
        default = FULL,
    )

    teeth = models.BigIntegerField(default = 0)
