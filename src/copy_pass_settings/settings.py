passes_common = (
    "use_pass_ambient_occlusion",
    "use_pass_combined",
    "use_pass_cryptomatte_accurate",
    "use_pass_cryptomatte_asset",
    "use_pass_cryptomatte_material",
    "use_pass_cryptomatte_object",
    "use_pass_diffuse_color",
    "use_pass_diffuse_direct",
    "use_pass_diffuse_indirect",
    "use_pass_emit",
    "use_pass_environment",
    "use_pass_glossy_color",
    "use_pass_glossy_direct",
    "use_pass_glossy_indirect",
    "use_pass_material_index",
    "use_pass_mist",
    "use_pass_normal",
    "use_pass_object_index",
    "use_pass_position",
    "use_pass_shadow",
    "use_pass_subsurface_color",
    "use_pass_subsurface_direct",
    "use_pass_subsurface_indirect",
    "use_pass_transmission_color",
    "use_pass_transmission_direct",
    "use_pass_transmission_indirect",
    "use_pass_uv",
    "use_pass_vector",
    "use_pass_z",
)

passes_eevee = (
    "use_pass_bloom",
    "use_pass_volume_direct",
)


def apply_settings(source, target, props):
    for prop in props:
        setattr(target, prop, getattr(source, prop))
