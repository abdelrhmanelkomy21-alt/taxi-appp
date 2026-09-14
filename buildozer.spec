[app]

# (str) Title of your application
title = Taxi Meter

# (str) Package name
package.name = taximeter

# (str) Package domain (needed for android packaging)
package.domain = org.taxi

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Directory where the source files are located
source.dir = .

# (str) Application versioning (version number)
version = 0.1

# (list) Application requirements
requirements = python3,flet

# (str) Supported orientation (landscape, portrait, all)
orientation = portrait

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 33

# (bool) Automatically accept SDK license
android.accept_sdk_license = True
