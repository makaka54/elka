[app]
title = Ёлка с пожеланиями
package.name = elka
package.domain = org.mytest
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,pyjnius,certifi,urllib3,chardet,idna,requests
orientation = portrait
fullscreen = 1
android.api = 33
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
