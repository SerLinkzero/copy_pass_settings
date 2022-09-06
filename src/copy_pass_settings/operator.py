import bpy
from copy_pass_settings.data import (CPSData, )


def update_layers():

    context = bpy.context
    current_scene = getattr(context, "scene", None)

    if current_scene is None:
        return

    # See register()
    cps_data: CPSData = current_scene.copy_pass_settings

    # A record of the currently existing layers in the collection prop
    existing_layer_ids = []
    for layer in cps_data.view_layers:
        existing_layer_ids.append(
            {"scene_name": layer.scene_name, "layer_name": layer.layer_name})

    # Add all currently existing view layers to a list
    # Should be the latest state everytime this function executes
    current_layer_ids = []
    for scene in bpy.data.scenes:
        for layer in scene.view_layers:
            current_layer_ids.append(
                {"scene_name": scene.name, "layer_name": layer.name})

    # Add new layers to data
    for layer in current_layer_ids:
        if layer not in existing_layer_ids:
            new_layer = cps_data.view_layers.add()
            new_layer.scene_name = layer["scene_name"]
            new_layer.layer_name = layer["layer_name"]
            new_layer.name = layer["scene_name"] + " / " + layer["layer_name"]

    # Remove the non-existing layers
    idx_offset = 0
    for i, layer in enumerate(existing_layer_ids):
        if layer not in current_layer_ids:
            cps_data.view_layers.remove(i - idx_offset)
            # The index should be offset as one item is removed in the target collection props
            idx_offset += 1


def copy_pass_settings(context, selected_layers, source_layer):
    # Local import
    from .settings import (passes_common, passes_eevee, apply_settings, copy_aovs, copy_lightgroups)

    for target_layer in selected_layers:
        apply_settings(source=source_layer,
                       target=target_layer, props=passes_common)
        apply_settings(source=source_layer.eevee,
                       target=target_layer.eevee, props=passes_eevee)
        copy_aovs(source=source_layer, target=target_layer)
        copy_lightgroups(source=source_layer, target=target_layer)

class CPS_OT_CopyPassSettings(bpy.types.Operator):
    bl_idname = "scene.copy_pass_settings"
    bl_label = "Render: Copy Pass Settings"
    bl_option = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        cps_data: CPSData = context.scene.copy_pass_settings
        current_layer = context.view_layer
        selected_layers = []

        for layer in cps_data.view_layers:
            if layer.selected:
                view_layer = bpy.data.scenes[layer.scene_name].view_layers[layer.layer_name]
                selected_layers.append(view_layer)

        copy_pass_settings(
            context, selected_layers=selected_layers, source_layer=current_layer)

        return {'FINISHED'}


class CPS_OT_UpdateViewLayerList(bpy.types.Operator):
    bl_idname = "scene.update_view_layer_list"
    bl_label = "Render: Update View Layer List"

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        update_layers()
        return {'FINISHED'}


classes = (
    CPS_OT_CopyPassSettings,
    CPS_OT_UpdateViewLayerList
)
