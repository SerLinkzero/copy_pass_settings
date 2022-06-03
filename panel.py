import bpy
from . import data

class CPS_UL_copy_pass_settings(bpy.types.UIList):
    def draw_item(self, context, layout, data, item: data.CPSDataLayer, icon, active_data, active_propname, index):
        # Each item is a view layer
        if context.scene.name == item.scene_name and context.view_layer.name == item.layer_name:
            display_name = item.name + " [CURRENT]"
        else:
            display_name = item.name
        layout.label(text = display_name, icon_value = icon)
        layout.prop(data = item, property = "selected", text = "")

class CPS_PT_copy_pass_settings(bpy.types.Panel):
    bl_label = "Copy Render Pass Settings"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "view_layer"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        cps_data: data.CPSData = context.scene.copy_pass_settings
        
        layout.operator(operator = "scene.update_view_layer_list", text = "Update View Layer List")

        layout.operator(operator = "scene.copy_pass_settings", text = "Copy Pass Settings")
        layout.template_list("CPS_UL_copy_pass_settings", "layers", cps_data, "view_layers", cps_data, "view_layer_idx", rows = 6)

classes = (CPS_UL_copy_pass_settings, CPS_PT_copy_pass_settings, )