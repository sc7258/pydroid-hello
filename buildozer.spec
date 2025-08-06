[app]

title = Pydroid Hello
package.name = pydroidhello
package.domain = com.sc7258
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1.0
# Explicitly require a Python 3-compatible version of pyjnius to fix build errors.
requirements = python3,kivy,pyjnius==1.6.1
orientation = portrait

# Android specific settings
android.permissions = INTERNET

[buildozer]

log_level = 2
warn_on_root = 1
