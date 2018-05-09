Name:           ros-melodic-rqt-robot-dashboard
Version:        0.5.7
Release:        0%{?dist}
Summary:        ROS rqt_robot_dashboard package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/rqt_robot_dashboard
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-python-qt-binding >= 0.2.19
Requires:       ros-melodic-qt-gui
Requires:       ros-melodic-rospy
Requires:       ros-melodic-rqt-console >= 0.3.1
Requires:       ros-melodic-rqt-gui
Requires:       ros-melodic-rqt-gui-py
Requires:       ros-melodic-rqt-nav-view
Requires:       ros-melodic-rqt-robot-monitor
BuildRequires:  ros-melodic-catkin

%description
rqt_robot_dashboard provides an infrastructure for building robot dashboard
plugins in rqt.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed May 09 2018 Aaron Blasdel <ablasdel@gmail.com> - 0.5.7-0
- Autogenerated by Bloom

