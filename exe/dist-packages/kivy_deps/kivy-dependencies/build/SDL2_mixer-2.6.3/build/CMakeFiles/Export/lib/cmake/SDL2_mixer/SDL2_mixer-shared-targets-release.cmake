#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SDL2_mixer::SDL2_mixer" for configuration "Release"
set_property(TARGET SDL2_mixer::SDL2_mixer APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SDL2_mixer::SDL2_mixer PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELEASE "SDL2::SDL2"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libSDL2_mixer-2.0.so.0.600.3"
  IMPORTED_SONAME_RELEASE "libSDL2_mixer-2.0.so.0"
  )

list(APPEND _IMPORT_CHECK_TARGETS SDL2_mixer::SDL2_mixer )
list(APPEND _IMPORT_CHECK_FILES_FOR_SDL2_mixer::SDL2_mixer "${_IMPORT_PREFIX}/lib/libSDL2_mixer-2.0.so.0.600.3" )

# Import target "SDL2_mixer::ogg" for configuration "Release"
set_property(TARGET SDL2_mixer::ogg APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SDL2_mixer::ogg PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libogg.so.0.8.5"
  IMPORTED_SONAME_RELEASE "libogg.so.0"
  )

list(APPEND _IMPORT_CHECK_TARGETS SDL2_mixer::ogg )
list(APPEND _IMPORT_CHECK_FILES_FOR_SDL2_mixer::ogg "${_IMPORT_PREFIX}/lib/libogg.so.0.8.5" )

# Import target "SDL2_mixer::opus" for configuration "Release"
set_property(TARGET SDL2_mixer::opus APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SDL2_mixer::opus PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopus.so.0.8.0"
  IMPORTED_SONAME_RELEASE "libopus.so.0"
  )

list(APPEND _IMPORT_CHECK_TARGETS SDL2_mixer::opus )
list(APPEND _IMPORT_CHECK_FILES_FOR_SDL2_mixer::opus "${_IMPORT_PREFIX}/lib/libopus.so.0.8.0" )

# Import target "SDL2_mixer::opusfile" for configuration "Release"
set_property(TARGET SDL2_mixer::opusfile APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SDL2_mixer::opusfile PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libopusfile.so.0.12"
  IMPORTED_SONAME_RELEASE "libopusfile.so.0"
  )

list(APPEND _IMPORT_CHECK_TARGETS SDL2_mixer::opusfile )
list(APPEND _IMPORT_CHECK_FILES_FOR_SDL2_mixer::opusfile "${_IMPORT_PREFIX}/lib/libopusfile.so.0.12" )

# Import target "SDL2_mixer::FLAC" for configuration "Release"
set_property(TARGET SDL2_mixer::FLAC APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SDL2_mixer::FLAC PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELEASE "SDL2_mixer::ogg"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libFLAC.so.8.3.0"
  IMPORTED_SONAME_RELEASE "libFLAC.so.8"
  )

list(APPEND _IMPORT_CHECK_TARGETS SDL2_mixer::FLAC )
list(APPEND _IMPORT_CHECK_FILES_FOR_SDL2_mixer::FLAC "${_IMPORT_PREFIX}/lib/libFLAC.so.8.3.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
