[app]
title = Golden Studio
package.name = goldenstudio
package.domain = com.goldenstudio

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,db,txt,ttf

version = 1.0

requirements = python3,kivy==2.3.0,kivymd==1.2.0

orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 24
android.sdk = 34
android.ndk = 28c
android.archs = arm64-v8a

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

icon.filename = assets/icon.png
presplash.filename = assets/splash.png

log_level = 2
warn_on_root = 1

p4a.branch = develop
p4a.source_dir = /home/user/.buildozer/android/platform/python-for-android

[buildozer]
log_level = 2
warn_on_root = 1