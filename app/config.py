import os, shutil
import yaml


def merge_and_overwrite(base: dict, update: dict):
    """
    递归地合并两个字典，并用 update 字典中的值覆盖 base 字典中的对应值（如果 update 中的值不是 None）。
    """
    for key, value in update.items():
        if key in base:
            if isinstance(value, dict):
                merge_and_overwrite(base[key], value)
            elif isinstance(value, list):
                base[key] = value[:]
            else:
                if value is not None:
                    base[key] = value
    return base


with open("config_example/setting.yaml", "r") as file:
    setting_example = yaml.safe_load(file) or {}
if not os.path.exists("config/setting.yaml"):
    setting: dict = setting_example
else:
    with open("config/setting.yaml", "r") as file:
        setting = yaml.safe_load(file)
    setting: dict = merge_and_overwrite(setting_example, setting)

with open("config/setting.yaml", "w") as file:
    yaml.safe_dump(
        setting, file, default_flow_style=False, allow_unicode=True, sort_keys=False
    )
