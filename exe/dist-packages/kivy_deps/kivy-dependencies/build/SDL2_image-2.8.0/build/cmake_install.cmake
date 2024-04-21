# Install script for directory: /home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/dist")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibraryx" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libSDL2_image-2.0.so.0.800.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libSDL2_image-2.0.so.0"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES
    "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/libSDL2_image-2.0.so.0.800.0"
    "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/libSDL2_image-2.0.so.0"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libSDL2_image-2.0.so.0.800.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libSDL2_image-2.0.so.0"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHANGE
           FILE "${file}"
           OLD_RPATH "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/dist/lib:"
           NEW_RPATH "")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibraryx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libSDL2_image-2.0.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libSDL2_image-2.0.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libSDL2_image-2.0.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/libSDL2_image-2.0.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libSDL2_image-2.0.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libSDL2_image-2.0.so")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libSDL2_image-2.0.so"
         OLD_RPATH "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/dist/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libSDL2_image-2.0.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xDEVELx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/SDL2" TYPE FILE FILES "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/include/SDL_image.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevelx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/external/libtiff/libtiff/libtiff.a")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevelx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/external/libwebp/libwebp.a")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevelx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES
    "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/external/libwebp/src/webp/decode.h"
    "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/external/libwebp/src/webp/encode.h"
    "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/external/libwebp/src/webp/types.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevelx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/external/libwebp/libwebpdemux.a")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevelx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE FILE FILES
    "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/external/libwebp/src/webp/decode.h"
    "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/external/libwebp/src/webp/demux.h"
    "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/external/libwebp/src/webp/mux_types.h"
    "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/external/libwebp/src/webp/types.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevelx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/SDL2_image" TYPE FILE FILES
    "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/SDL2_imageConfig.cmake"
    "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/SDL2_imageConfigVersion.cmake"
    "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/cmake/Findlibjxl.cmake"
    "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/cmake/Findwebp.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevelx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/SDL2_image/SDL2_image-shared-targets.cmake")
    file(DIFFERENT EXPORT_FILE_CHANGED FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/SDL2_image/SDL2_image-shared-targets.cmake"
         "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/CMakeFiles/Export/lib/cmake/SDL2_image/SDL2_image-shared-targets.cmake")
    if(EXPORT_FILE_CHANGED)
      file(GLOB OLD_CONFIG_FILES "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/SDL2_image/SDL2_image-shared-targets-*.cmake")
      if(OLD_CONFIG_FILES)
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/SDL2_image/SDL2_image-shared-targets.cmake\" will be replaced.  Removing files [${OLD_CONFIG_FILES}].")
        file(REMOVE ${OLD_CONFIG_FILES})
      endif()
    endif()
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/SDL2_image" TYPE FILE FILES "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/CMakeFiles/Export/lib/cmake/SDL2_image/SDL2_image-shared-targets.cmake")
  if("${CMAKE_INSTALL_CONFIG_NAME}" MATCHES "^([Rr][Ee][Ll][Ee][Aa][Ss][Ee])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/SDL2_image" TYPE FILE FILES "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/CMakeFiles/Export/lib/cmake/SDL2_image/SDL2_image-shared-targets-release.cmake")
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevelx" OR NOT CMAKE_INSTALL_COMPONENT)
  
            # FIXME: use file(COPY_FILE) if minimum CMake version >= 3.21
            execute_process(COMMAND "${CMAKE_COMMAND}" -E copy_if_different
                "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/SDL2_image-Release.pc"
                "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/SDL2_image.pc")
            file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig"
                TYPE FILE
                FILES "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/SDL2_image.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xdevelx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE FILES "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/libSDL2_image.so")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xlibraryx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/licenses/SDL2_image" TYPE FILE FILES "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/LICENSE.txt")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/disd/Documents/Git/ZipperAI/exe/kivy-deps-build/kivy-dependencies/build/SDL2_image-2.8.0/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
