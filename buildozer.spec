name: Build APK

on:
  push:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Setup older Gradle
        run: |
          sudo rm -rf /usr/share/gradle-*
          wget -q https://services.gradle.org/distributions/gradle-7.4.2-bin.zip
          sudo unzip -q gradle-7.4.2-bin.zip -d /opt/
          sudo ln -sf /opt/gradle-7.4.2/bin/gradle /usr/bin/gradle
          gradle --version

      - name: Install system deps
        run: |
          sudo apt-get update
          sudo apt-get install -y git zip unzip openjdk-17-jdk \
            autoconf libtool pkg-config zlib1g-dev libncurses5-dev \
            libncursesw5-dev cmake libffi-dev libssl-dev automake \
            autopoint gettext

      - name: Install Buildozer
        run: |
          pip install --upgrade pip
          pip install buildozer cython==0.29.36 virtualenv

      - name: Accept Android licenses
        run: |
          mkdir -p ~/.android
          echo "24333f8a63b6825ea9c5514f83c2829b004d1fee" > ~/.android/repositories.cfg

      - name: Clean previous build
        run: rm -rf .buildozer

      - name: Build APK
        run: buildozer -v android debug

      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: elka-apk
          path: bin/*.apk
