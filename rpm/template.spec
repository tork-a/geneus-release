Name:           ros-indigo-geneus
Version:        2.1.2
Release:        0%{?dist}
Summary:        ROS geneus package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       python-rospkg
Requires:       ros-indigo-genmsg
BuildRequires:  ros-indigo-catkin >= 0.5.78
BuildRequires:  ros-indigo-genmsg

%description
EusLisp ROS message and service generators.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Feb 25 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.2-0
- Autogenerated by Bloom

* Sat Feb 21 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.1-0
- Autogenerated by Bloom

* Thu Feb 12 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.1.0-0
- Autogenerated by Bloom

* Tue Feb 10 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.1-1
- Autogenerated by Bloom

* Tue Feb 10 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Tue Jan 06 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.0-0
- Autogenerated by Bloom

* Mon Dec 22 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.0-0
- Autogenerated by Bloom

