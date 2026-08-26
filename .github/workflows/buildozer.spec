cat > buildozer.spec << 'EOF'
[app]
title = WiFiTool
package.name = wifitool
package.domain = org.rocket
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.2.0
fullscreen = 0
android.minapi = 21
android.maxapi = 33
android.api = 30
android.ndk = 26c
android.sdk = 30
android.accept_sdk_license = True
android.permissions = INTERNET,ACCESS_WIFI_STATE,ACCESS_COARSE_LOCATION,ACCESS_FINE_LOCATION
EOF
