[app]

title = Golden Studio

package.name = goldenstudio
package.domain = com.goldenstudio

source.dir = .
source.include_exts = py,png,jpg,kv,json,db,txt

version = 1.0

requirements = python3==3.11,kivy==2.3.0,kivymd==1.2.0

orientation = portrait
fullscreen = 0

# Android Configuration
android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a
android.build_tools_version = 33.0.2

android.permissions = INTERNET
android.accept_sdk_license = True

icon.filename = assets/icon.png
presplash.filename = assets/splash.png

# Logging
log_level = 2
warn_on_root = 1

p4a.branch = 2024.01.21


[buildozer]

log_level = 2
warn_on_root = 1