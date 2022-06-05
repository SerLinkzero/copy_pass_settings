# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from . import (panel, operator, data)
from bpy.props import (
    PointerProperty,
)
import bpy
bl_info = {
    "name": "Copy Pass Settings",
    "author": "Linkzero Tsang <github.com/serlinkzero>",
    "description": "Copy view layer pass settings.",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "View Layer Properties",
    "warning": "",
    "category": "Render",
    "wiki_url": "https://github.com/SerLinkzero/copy_pass_settings"
}


classes = panel.classes + operator.classes + data.classes


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # Register the main property group
    bpy.types.Scene.copy_pass_settings = PointerProperty(type=data.CPSData)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
