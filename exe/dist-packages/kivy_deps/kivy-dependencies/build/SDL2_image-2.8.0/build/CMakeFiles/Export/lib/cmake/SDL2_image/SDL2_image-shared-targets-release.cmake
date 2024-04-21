#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SDL2_image::SDL2_image" for configuration "Release"
set_property(TARGET SDL2_image::SDL2_image APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SDL2_image::SDL2_image PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELEASE "SDL2::SDL2"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libSDL2_image-2.0.so.0.800.0"
  IMPORTED_SONAME_RELEASE "libSDL2_image-2.0.so.0"
  )

list(APPEND _IMPORT_CHECK_TARGETS SDL2_image::SDL2_image )
list(APPEND _IMPORT_CHECK_FILES_FOR_SDL2_image::SDL2_image "${_IMPORT_PREFIX}/lib/libSDL2_image-2.0.so.0.800.0" )

# Import target "SDL2_image::external_libtiff" for configuration "Release"
set_property(TARGET SDL2_image::external_libtiff APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SDL2_image::external_libtiff PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C"
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "m"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libtiff.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS SDL2_image::external_libtiff )
list(APPEND _IMPORT_CHECK_FILES_FOR_SDL2_image::external_libtiff "${_IMPORT_PREFIX}/lib/libtiff.a" )

# Import target "SDL2_image::external_libwebp" for configuration "Release"
set_property(TARGET SDL2_image::external_libwebp APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SDL2_image::external_libwebp PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libwebp.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS SDL2_image::external_libwebp )
list(APPEND _IMPORT_CHECK_FILES_FOR_SDL2_image::external_libwebp "${_IMPORT_PREFIX}/lib/libwebp.a" )

# Import target "SDL2_image::webpdemux" for configuration "Release"
set_property(TARGET SDL2_image::webpdemux APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SDL2_image::webpdemux PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "C"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libwebpdemux.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS SDL2_image::webpdemux )
list(APPEND _IMPORT_CHECK_FILES_FOR_SDL2_image::webpdemux "${_IMPORT_PREFIX}/lib/libwebpdemux.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
