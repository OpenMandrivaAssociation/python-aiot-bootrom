%undefine _debugsource_packages

Name:		python-aiot-bootrom
Version:	1.1.5
Release:	4
Source0:	https://gitlab.baylibre.com/baylibre/mediatek/bsp/aiot-bootrom/-/archive/main/aiot-bootrom-main.tar.bz2
Summary:	Python library for handling the boot ROM on Mediatek AIoT SoCs
URL:		https://gitlab.baylibre.com/baylibre/mediatek/bsp/aiot-bootrom
# See also https://gitlab.com/mediatek/aiot/bsp/aiot-bootrom
License:	GPL
Group:		Development/Python
BuildRequires:	python%{pyver}dist(setuptools)

%description
Python library for handling the boot ROM on Mediatek AIoT SoCs

%prep
%autosetup -p1 -n aiot-bootrom-main
# setuptools 84 no longer ships pkg_resources.
python - << 'PY'
from pathlib import Path
path = Path("aiot_bootrom/bootrom.py")
text = path.read_text()
old_import = "import pkg_resources\n"
new_import = "import importlib.resources\n"
old_call = "pkg_resources.resource_filename('aiot_bootrom', bin_name)"
new_call = "str(importlib.resources.files('aiot_bootrom').joinpath(bin_name))"
if old_import not in text or old_call not in text:
    raise SystemExit("bootrom.py no longer uses pkg_resources")
path.write_text(text.replace(old_import, new_import, 1).replace(old_call, new_call, 1))
PY

%build
%py_build

%install
%py_install
# Upstream ships prebuilt bootrom-tool binaries for several architectures.
# find-requires turns every one of them into a dependency.
case "%{_arch}" in
aarch64) keep=bootrom-tool.aarch64 ;;
armv7hl|armv7l|arm*) keep=bootrom-tool.armv7l ;;
*) keep= ;;
esac
bindir="%{buildroot}%{py_sitedir}/aiot_bootrom/bin"
if [ -n "$keep" ]; then
	find "$bindir" -type f ! -name "$keep" -delete
else
	rm -rf "$bindir"
fi

%files
%{_bindir}/*
%{py_sitedir}/aiot_bootrom
%{py_sitedir}/aiot_bootrom-*.*-info
