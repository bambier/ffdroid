#! /usr/bin/env python3
import subprocess
from pathlib import Path

import yaml

# Codes

BASE_DIR = Path().parent


with open("android.yaml", "r") as file:
    data: dict = yaml.load(file.read(), yaml.Loader)


commands = ["p4a", "create", "apk"]

name = data.get("name", None)
package = data.get("package", None)
version = data.get("version", None)
icon = data.get("icon", None)
release = data.get("release", None)
private = data.get("private", None)
sdk_dir = data.get("sdk-dir", None)
ndk_dir = data.get("ndk-dir", None)
android_api = data.get("android-api", None)
ndk_api = data.get("ndk-api", None)
storage_dir = data.get("storage-dir", None)
bootstrap = data.get("bootstrap", None)
orientation = data.get("orientation", None)
manifest_orientation = data.get("manifest-orientation", None)
permission = data.get("permission", None)
meta_data = data.get("meta-data", None)
presplash = data.get("presplash", None)
presplash_color = data.get("presplash-color", None)
presplash_lottie = data.get("presplash-lottie", None)
wakelock = data.get("wakelock", None)
window = data.get("window", None)
blacklist = data.get("blacklist", None)
whitelist = data.get("whitelist", None)
add_jar = data.get("add-jar", None)
intent_filters = data.get("intent-filters", None)
service = data.get("service", None)
add_source = data.get("add-source", None)
no_byte_compile_python = data.get("no-byte-compile-python", None)
enable_androidx = data.get("enable-androidx", None)
add_resource = data.get("add-resource", None)
arch = data.get("arch", None)
dist_name = data.get("dist-name", None)
blacklist_requirements = data.get("blacklist-requirements", None)
requirements = data.get("requirements", None)
recipe_blacklist = data.get("recipe-blacklist", None)
local_recipes = data.get("local-recipes", None)
activity_class_name = data.get("activity-class-name", None)
service_class_name = data.get("service-class-name", None)
java_build_tool = data.get("java-build-tool", None)
add_asset = data.get("add-asset", None)
with_debug_symbols = data.get("with-debug-symbols", None)
keystore = data.get("keystore", None)
signkey = data.get("signkey", None)
keystorepw = data.get("keystorepw", None)
signkeypw = data.get("signkeypw", None)
force_build = data.get("force-build", None)
require_perfect_match = data.get("require-perfect-match", None)
copy_libs = data.get("copy-libs", None)
debug = data.get("debug", None)
color = data.get("color", None)


if name not in (False, None):
    commands.append("--name")
    commands.append(str(name))

if package not in (False, None):
    commands.append("--package")
    commands.append(str(package))

if version not in (False, None):
    commands.append("--version")
    commands.append(str(version))

if icon not in (False, None):
    commands.append("--icon")
    commands.append(str(icon))

if private not in (False, None):
    commands.append("--private")
    commands.append(str(private))

if sdk_dir not in (False, None):
    commands.append("--sdk-dir")
    commands.append(str(sdk_dir))

if ndk_dir not in (False, None):
    commands.append("--ndk-dir")
    commands.append(str(ndk_dir))

if android_api not in (False, None):
    commands.append("--android-api")
    commands.append(str(android_api))

if ndk_api not in (False, None):
    commands.append("--ndk-api")
    commands.append(str(ndk_api))

if storage_dir not in (False, None):
    commands.append("--storage-dir")
    commands.append(str(storage_dir))

if bootstrap not in (False, None):
    commands.append("--bootstrap")
    commands.append(str(bootstrap))

if orientation not in (False, None):
    commands.append("--orientation")
    commands.append(str(orientation))

if manifest_orientation not in (False, None):
    commands.append("--manifest-orientation")
    commands.append(str(manifest_orientation))

if permission not in (False, None):
    for i in permission:
        commands.append("--permission")
        commands.append(str(i))

if meta_data not in (False, None):
    for key, value in meta_data:
        commands.append("--meta-data")
        commands.append(f"{key}={value}")

if presplash not in (False, None):
    commands.append("--presplash")
    commands.append(str(presplash))

if presplash_color not in (False, None):
    commands.append("--presplash-color")
    commands.append(str(presplash_color))

if presplash_lottie not in (False, None):
    commands.append("--presplash-lottie")
    commands.append(str(presplash_lottie))

if wakelock not in (False, None):
    commands.append("--wakelock")

if window not in (False, None):
    commands.append("--window")

if blacklist not in (False, None):
    commands.append("--blacklist")
    commands.append(str(blacklist))

if whitelist not in (False, None):
    commands.append("--whitelist")
    commands.append(str(whitelist))

if add_jar not in (False, None):
    commands.append("--add-jar")
    commands.append(str(add_jar))

if intent_filters not in (False, None):
    commands.append("--intent-filters")
    commands.append(str(intent_filters))

if service not in (False, None):
    commands.append("--service")
    commands.append(str(service))

if add_source not in (False, None):
    commands.append("--add-source")
    commands.append(str(add_source))

if no_byte_compile_python not in (False, None):
    commands.append("--no-byte-compile-python")

if enable_androidx not in (False, None):
    commands.append("--enable-androidx")

if add_resource not in (False, None):
    commands.append("--add-resource")
    commands.append(str(add_resource))

if arch not in (False, None):
    for i in arch:
        commands.append("--arch")
        commands.append(str(i))

if dist_name not in (False, None):
    commands.append("--dist-name")
    commands.append(str(dist_name))

if blacklist_requirements not in (False, None):
    commands.append("--blacklist-requirements")
    commands.append(",".join(blacklist_requirements))

if requirements not in (False, None):
    commands.append("--requirements")
    commands.append(",".join(requirements))

if recipe_blacklist not in (False, None):
    commands.append("--recipe-blacklist")
    commands.append(",".join(recipe_blacklist))

if local_recipes not in (False, None):
    commands.append("--local-recipes")
    commands.append(",".join(local_recipes))

if activity_class_name not in (False, None):
    commands.append("--activity-class-name")
    commands.append(str(activity_class_name))

if service_class_name not in (False, None):
    commands.append("--service-class-name")
    commands.append(str(service_class_name))

if java_build_tool not in (False, None):
    commands.append("--java-build-tool")
    commands.append(str(java_build_tool))

if add_asset not in (False, None):
    commands.append("--add-asset")
    commands.append(str(add_asset))

if with_debug_symbols not in (False, None):
    commands.append("--with-debug-symbols")

if keystore not in (False, None):
    commands.append("--keystore")
    commands.append(str(keystore))

if signkey not in (False, None):
    commands.append("--signkey")
    commands.append(str(signkey))

if keystorepw not in (False, None):
    commands.append("--keystorepw")
    commands.append(str(keystorepw))

if signkeypw not in (False, None):
    commands.append("--signkeypw")
    commands.append(str(signkeypw))

if force_build not in (False, None):
    commands.append("--force-build")

if require_perfect_match not in (False, None):
    commands.append("--require-perfect-match")
    commands.append(str(require_perfect_match))

if copy_libs not in (False, None):
    commands.append("--copy-libs")

if debug not in (False, None):
    commands.append("--debug")

if color not in (False, None):
    commands.append("--color")
    commands.append(str(color))

if release not in (False, None):
    commands.append("--release")


print("\nRunning Command:", commands, "\n")

subprocess.run(commands)
