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


from flask_restx._http import HTTPStatus

from pyispyb.flask_restx_patched import Resource

from pyispyb.app.extensions.api import api_v1, Namespace
from pyispyb.app.extensions.authentication import authentication_required
from pyispyb.app.extensions.authorization import authorization_required
from pyispyb.app.extensions.user_office import user_office


__license__ = "LGPLv3+"


api = Namespace(
    "User office", description="User office related namespace", path="/user_office"
)
api_v1.add_namespace(api)


@api.route("/sync_all", endpoint="user_office_sync_all")
@api.doc(security="apikey")
class SyncAll(Resource):

    """Sync with user office"""

    @authentication_required
    @authorization_required
    def post(self):
        """Sync with user office"""

        api.logger.info("Sync with uer office")
        user_office.sync_all()
        return HTTPStatus.OK, {"message": "Done!"}


@api.route(
    "/sync_proposal/<string:proposal_code><int:proposal_number>",
    endpoint="user_office_sync_proposal",
)
@api.param("proposal_code", "Proposal code (string)")
@api.param("proposal_number", "Proposal number (integer)")
@api.doc(security="apikey")
class UpdateProposal(Resource):
    """Sync with user office"""

    @authentication_required
    @authorization_required
    @api.doc(
        description="proposal_code should be a string, proposal_number should be an integer"
    )
    def post(self, proposal_code, proposal_number):
        """Sync with user office"""

        api.logger.info("Updates proposal %s%d" % (proposal_code, proposal_number))
        user_office.sync_proposal(proposal_code, proposal_number)
        return HTTPStatus.OK, {"message": "Done!"}
