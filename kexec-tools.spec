#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : kexec-tools
Version  : 2.0.25
Release  : 20
URL      : https://www.kernel.org/pub/linux/utils/kernel/kexec/kexec-tools-2.0.25.tar.xz
Source0  : https://www.kernel.org/pub/linux/utils/kernel/kexec/kexec-tools-2.0.25.tar.xz
Summary  : Load one kernel from another
Group    : Development/Tools
License  : GPL-2.0
Requires: kexec-tools-bin = %{version}-%{release}
Requires: kexec-tools-license = %{version}-%{release}
Requires: kexec-tools-man = %{version}-%{release}
BuildRequires : pkgconfig(zlib)
BuildRequires : xz-dev

%description
/sbin/kexec is a user space utility for loading another kernel
and asking the currently running kernel to do something with it.
A currently running kernel may be asked to start the loaded
kernel on reboot, or to start the loaded kernel after it panics.

The panic case is useful for having an intact kernel for writing
crash dumps.  But other uses may be imagined.

%package bin
Summary: bin components for the kexec-tools package.
Group: Binaries
Requires: kexec-tools-license = %{version}-%{release}

%description bin
bin components for the kexec-tools package.


%package license
Summary: license components for the kexec-tools package.
Group: Default

%description license
license components for the kexec-tools package.


%package man
Summary: man components for the kexec-tools package.
Group: Default

%description man
man components for the kexec-tools package.


%prep
%setup -q -n kexec-tools-2.0.25
cd %{_builddir}/kexec-tools-2.0.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659366387
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1659366387
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kexec-tools
cp %{_builddir}/kexec-tools-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kexec-tools/c1f673dec6037696f751588854283118d7c38db3
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/kexec-tools/kexec_test

%files bin
%defattr(-,root,root,-)
/usr/bin/kexec
/usr/bin/vmcore-dmesg

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kexec-tools/c1f673dec6037696f751588854283118d7c38db3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/kexec.8
/usr/share/man/man8/vmcore-dmesg.8
