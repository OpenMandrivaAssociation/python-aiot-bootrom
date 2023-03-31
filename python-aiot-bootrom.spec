%undefine _debugsource_packages

Name:		python-aiot-bootrom
Version:	1.1.4
Release:	2
Source0:	https://gitlab.com/mediatek/aiot/bsp/aiot-bootrom/-/archive/main/aiot-bootrom-main.tar.bz2
Summary:	Python library for handling the boot ROM on Mediatek AIoT SoCs
URL:		https://gitlab.com/mediatek/aiot/bsp/aiot-bootrom
License:	GPL
Group:		Development/Python
BuildRequires:	python%{pyver}dist(setuptools)

%description
Python library for handling the boot ROM on Mediatek AIoT SoCs

%prep
%autosetup -p1 -n aiot-bootrom-main

%build
%py_build

%install
%py_install

%files
%{_bindir}/*
%{py_sitedir}/aiot_bootrom
%{py_sitedir}/aiot_bootrom-*.*-info
