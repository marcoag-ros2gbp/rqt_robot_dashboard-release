Name:           ros-jade-rqt-robot-dashboard
Version:        0.5.7
Release:        0%{?dist}
Summary:        ROS rqt_robot_dashboard package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rqt_robot_dashboard
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-diagnostic-msgs
Requires:       ros-jade-python-qt-binding >= 0.2.19
Requires:       ros-jade-qt-gui
Requires:       ros-jade-rospy
Requires:       ros-jade-rqt-console >= 0.3.1
Requires:       ros-jade-rqt-gui
Requires:       ros-jade-rqt-gui-py
Requires:       ros-jade-rqt-nav-view
Requires:       ros-jade-rqt-robot-monitor
BuildRequires:  ros-jade-catkin

%description
rqt_robot_dashboard provides an infrastructure for building robot dashboard
plugins in rqt.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Apr 28 2017 Aaron Blasdel <ablasdel@gmail.com> - 0.5.7-0
- Autogenerated by Bloom

