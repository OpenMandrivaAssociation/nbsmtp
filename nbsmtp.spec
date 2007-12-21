Summary:	nbSMTP: no-brainer SMTP
Name:		nbsmtp
Version:	1.00
Release:	%mkrel 2
License:	GPL
Group:		System/Servers
URL:		http://nbsmtp.ferdyx.org/
Source0:	http://www.gentoo-es.org/~ferdy/%{name}-%{version}.tar.bz2
Patch0:		nbsmtp-1.00_DESTDIR.patch
Patch1:		nbsmtp-1.00_gcc41.patch
Provides:	sendmail-command
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
nbSMTP is a simple SMTP client suitable to run in chroot jails, in embeded
systems, laptops, workstations, ... It's written in C and it compiles and runs
under lot of Unix flavors such as Linux, MacOSX, FreeBSD, ... (it practically
runs on any Unix flavor). Here you can read more AboutNbsmtp.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build

%configure2_5x \
    --bindir=%{_sbindir} \
    --enable-ssl \
    --enable-ipv6

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%post
update-alternatives --install %{_sbindir}/sendmail sendmail-command %{_sbindir}/nbsmtp 5

%preun
if [ $1 = 0 ]; then
    update-alternatives --remove sendmail-command %{_sbindir}/nbsmtp
fi


%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog DOCS INSTALL
%attr(0755,root,root) %{_sbindir}/nbsmtp
%attr(0644,root,root) %{_mandir}/man5/*
%attr(0644,root,root) %{_mandir}/man8/*
