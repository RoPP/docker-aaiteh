cmake_minimum_required(VERSION 2.6)

project(docker-aaiteh)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_SOURCE_DIR}/cmake/modules)

# Default to release build type
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Release")
endif()

install(
    PROGRAMS ${CMAKE_SOURCE_DIR}/docker-aaiteh.py
    DESTINATION bin
    )

# Systemd
find_package(Systemd)
if(SYSTEMD_FOUND)
    execute_process(
        COMMAND ${PKG_CONFIG_EXECUTABLE} --variable=systemdsystemunitdir systemd
        OUTPUT_VARIABLE SYSTEMD_SYSTEM_UNIT_DIR
        )
    string(STRIP ${SYSTEMD_SYSTEM_UNIT_DIR} SYSTEMD_SYSTEM_UNIT_DIR)

    configure_file(
        ${CMAKE_SOURCE_DIR}/docker-aaiteh.service.in
        ${CMAKE_BINARY_DIR}/docker-aaiteh.service
        )
    message("SYSTEMD_SYSTEM_UNIT_DIR: " ${SYSTEMD_SYSTEM_UNIT_DIR})
    install(
        FILES ${CMAKE_BINARY_DIR}/docker-aaiteh.service
        DESTINATION ${SYSTEMD_SYSTEM_UNIT_DIR}
        )
endif()
