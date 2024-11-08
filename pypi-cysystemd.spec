#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v16
# autospec commit: b858a2a
#
Name     : pypi-cysystemd
Version  : 1.6.2
Release  : 2
URL      : https://files.pythonhosted.org/packages/b5/66/25fa2eda48dc9c634a2ae1b8c9879ed842359f2d8f3d2bf7bd88783e278c/cysystemd-1.6.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/b5/66/25fa2eda48dc9c634a2ae1b8c9879ed842359f2d8f3d2bf7bd88783e278c/cysystemd-1.6.2.tar.gz
Summary  : systemd wrapper in Cython
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-cysystemd-license = %{version}-%{release}
Requires: pypi-cysystemd-python = %{version}-%{release}
Requires: pypi-cysystemd-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
![pypi version](https://img.shields.io/pypi/v/cysystemd.svg) ![](https://img.shields.io/pypi/pyversions/cysystemd.svg)  ![License](https://img.shields.io/pypi/l/cysystemd.svg)

%package license
Summary: license components for the pypi-cysystemd package.
Group: Default

%description license
license components for the pypi-cysystemd package.


%package python
Summary: python components for the pypi-cysystemd package.
Group: Default
Requires: pypi-cysystemd-python3 = %{version}-%{release}

%description python
python components for the pypi-cysystemd package.


%package python3
Summary: python3 components for the pypi-cysystemd package.
Group: Default
Requires: python3-core
Provides: pypi(cysystemd)

%description python3
python3 components for the pypi-cysystemd package.


%prep
%setup -q -n cysystemd-1.6.2
cd %{_builddir}/cysystemd-1.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721352693
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cysystemd
cp %{_builddir}/cysystemd-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cysystemd/92170cdc034b2ff819323ff670d3b7266c8bffcd || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cysystemd/92170cdc034b2ff819323ff670d3b7266c8bffcd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
