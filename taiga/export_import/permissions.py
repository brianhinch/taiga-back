# coding: utf-8
# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from taiga.base.api.permissions import (TaigaResourcePermission,
                                        IsProjectOwner, IsAuthenticated)


class ImportExportPermission(TaigaResourcePermission):
    import_project_perms = IsAuthenticated()
    import_item_perms = IsProjectOwner()
    export_project_perms = IsProjectOwner()
    load_dump_perms = IsAuthenticated()
