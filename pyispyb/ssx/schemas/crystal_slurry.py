"""
Project: py-ispyb.

https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.
"""


__license__ = "LGPLv3+"



from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields
from marshmallow_jsonschema import JSONSchema

from pyispyb.app.extensions.api import api_v1 as api

dict_schema = {
        'crystalSlurryId': f_fields.Integer(required=True, description=''),
        'name': f_fields.String(required=False, description=''),
        'crystalSizeDistributionId': f_fields.Integer(required=False, description=''),
        'crystalDensity': f_fields.Float(required=False, description='1/mm3'),
        'bufferId': f_fields.Float(required=False, description='reference to Buffer.bufferId'),
        }

class CrystalSlurrySchema(Schema):
    """Marshmallows schema class representing CrystalSlurry table"""

    crystalSlurryId = ma_fields.Integer()
    name = ma_fields.String()
    crystalSizeDistributionId = ma_fields.Integer()
    crystalDensity = ma_fields.Float()
    bufferId = ma_fields.Float()

f_schema = api.model('CrystalSlurry', dict_schema)
ma_schema = CrystalSlurrySchema()
json_schema = JSONSchema().dump(ma_schema)
