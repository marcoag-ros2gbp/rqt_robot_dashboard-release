%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/rolling/.*$
%global __requires_exclude_from ^/opt/ros/rolling/.*$

Name:           ros-rolling-rqt-robot-dashboard
Version:        0.6.1
Release:        4%{?dist}%{?release_suffix}
Summary:        ROS rqt_robot_dashboard package

License:        BSD
URL:            http://wiki.ros.org/rqt_robot_dashboard
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-rolling-diagnostic-msgs
Requires:       ros-rolling-python-qt-binding >= 0.2.19
Requires:       ros-rolling-qt-gui
Requires:       ros-rolling-rclpy
Requires:       ros-rolling-rqt-console >= 0.3.1
Requires:       ros-rolling-rqt-gui
Requires:       ros-rolling-rqt-gui-py
Requires:       ros-rolling-rqt-robot-monitor
Requires:       ros-rolling-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  ros-rolling-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
rqt_robot_dashboard provides an infrastructure for building robot dashboard
plugins in rqt.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/rolling"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/rolling/setup.sh" ]; then . "/opt/ros/rolling/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/rolling

%changelog
* Tue Feb 20 2024 Aaron Blasdel <ablasdel@gmail.com> - 0.6.1-4
- Autogenerated by Bloom

