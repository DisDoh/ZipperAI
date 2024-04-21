#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "SDL2_ttf::SDL2_ttf" for configuration "Release"
set_property(TARGET SDL2_ttf::SDL2_ttf APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(SDL2_ttf::SDL2_ttf PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELEASE "SDL2::SDL2"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libSDL2_ttf-2.0.so.0.2000.2"
  IMPORTED_SONAME_RELEASE "libSDL2_ttf-2.0.so.0"
  )

list(APPEND _IMPORT_CHECK_TARGETS SDL2_ttf::SDL2_ttf )
list(APPEND _IMPORT_CHECK_FILES_FOR_SDL2_ttf::SDL2_ttf "${_IMPORT_PREFIX}/lib/libSDL2_ttf-2.0.so.0.2000.2" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
