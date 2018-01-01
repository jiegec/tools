#!/bin/bash
xcodebuild -workspace $1.xcworkspace -scheme $1 -archivePath temp_archive/$1.xcarchive archive
xcodebuild -exportArchive -exportOptionsPlist /Volumes/Data/tools/make_app/export.plist -archivePath temp_archive/$1.xcarchive -exportPath App
rm -r temp_archive
