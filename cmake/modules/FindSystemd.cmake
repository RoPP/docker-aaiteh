# Finds systemd and its libraries
# Not a huge module but sufficient for now
# Uses the same semantics as pkg_check_modules, i.e. ${LIB}{_FOUND,_INCLUDE_DIR,_LIBRARIES}
# where ${LIB} can be one of the following:
#     LIBSYSTEMD_JOURNAL, SYSTEMD, LIBSYSTEMD_DAEMON, LIBSYSTEMD_LOGIN, LIBSYSTEMD_ID128
#
# Copyright: Red Hat, Inc. 2013
# Author: Martin Briza <mbriza@redhat.com>
#
# Distributed under the BSD license. See COPYING-CMAKE-SCRIPTS for details.

#defining any of these disables systemd support
if (NOT LIBSYSTEMD_JOURNAL_FOUND AND
    NOT SYSTEMD_FOUND AND
    NOT LIBSYSTEMD_DAEMON_FOUND AND
    NOT LIBSYSTEMD_LOGIN_FOUND AND
    NOT LIBSYSTEMD_ID128_FOUND)
find_package(PkgConfig)
if (PKG_CONFIG_FOUND)
    pkg_check_modules(LIBSYSTEMD_JOURNAL QUIET "libsystemd-journal")
    pkg_check_modules(SYSTEMD QUIET "systemd")
    pkg_check_modules(LIBSYSTEMD_DAEMON QUIET "libsystemd-daemon")
    pkg_check_modules(LIBSYSTEMD_LOGIN QUIET "libsystemd-login")
    pkg_check_modules(LIBSYSTEMD_ID128 QUIET "libsystemd-id128")
endif (PKG_CONFIG_FOUND)

if (SYSTEMD_FOUND)
    message(STATUS "Found systemd")
endif(SYSTEMD_FOUND)

mark_as_advanced(LIBSYSTEMD_JOURNAL_FOUND       SYSTEMD_FOUND       LIBSYSTEMD_DAEMON_FOUND       LIBSYSTEMD_LOGIN_FOUND       LIBSYSTEMD_ID128_FOUND)
mark_as_advanced(LIBSYSTEMD_JOURNAL_INCLUDE_DIR SYSTEMD_INCLUDE_DIR LIBSYSTEMD_DAEMON_INCLUDE_DIR LIBSYSTEMD_LOGIN_INCLUDE_DIR LIBSYSTEMD_ID128_INCLUDE_DIR)
mark_as_advanced(LIBSYSTEMD_JOURNAL_LIBRARIES   SYSTEMD_LIBRARIES   LIBSYSTEMD_DAEMON_LIBRARIES   LIBSYSTEMD_LOGIN_LIBRARIES   LIBSYSTEMD_ID128_LIBRARIES)

endif (NOT LIBSYSTEMD_JOURNAL_FOUND AND
       NOT SYSTEMD_FOUND AND
       NOT LIBSYSTEMD_DAEMON_FOUND AND
       NOT LIBSYSTEMD_LOGIN_FOUND AND
       NOT LIBSYSTEMD_ID128_FOUND)