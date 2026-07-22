[app]

# (str) Title of your application
title = Golden Studio

# (str) Package name
package.name = goldenstudio

# (str) Package domain
package.domain = com.goldenstudio

# (str) Source code directory
source.dir = .

# (list) Included file extensions
source.include_exts = py,png,jpg,jpeg,kv,json,txt,db

# (list) Excluded directories
source.exclude_dirs = .git,.github,bin,build,__pycache__

# (str) Application version
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy==2.3.0,kivymd==1.2.0

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (str) Icon
icon.filename = assets/icon.png

# (str) Splash screen
presplash.filename = assets/splash.png

# -------------------------
# Android Configuration
# -------------------------

android.api = 33

android.minapi = 24

android.ndk = 25b

android.build_tools_version = 33.0.2

android.archs = arm64-v8a

android.permissions = INTERNET

android.accept_sdk_license = True

# -------------------------
# Logging
# -------------------------

log_level = 2

warn_on_root = 1


[buildozer]

log_level = 2

warn_on_root = 1