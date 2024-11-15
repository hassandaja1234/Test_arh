[app]
title = Face Detection
package.name = facedetection
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,opencv-python,numpy,pillow
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 29
android.minapi = 21
# Removed android.sdk as it is deprecated
android.ndk = 27c
# Replaced android.arch with android.archs
android.archs = armeabi-v7a
