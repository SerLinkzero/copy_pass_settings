import bpy
from bpy.props import (
    StringProperty,
    BoolProperty,
    IntProperty,
    CollectionProperty,
)

# View Layers
class CPSDataLayer(bpy.types.PropertyGroup):
    selected: BoolProperty(default = True)
    scene_name: StringProperty()
    layer_name: StringProperty()
    
    # For list filtering
    name: StringProperty()

class CPSData(bpy.types.PropertyGroup):
    view_layers: CollectionProperty(
        type=CPSDataLayer,
        name="View Layers",
        description="View layers that will be affected")

    view_layer_idx: IntProperty()

classes = (
    CPSDataLayer,
    CPSData
    )