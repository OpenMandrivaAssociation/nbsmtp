Summary:	: no-brainer SMTP
Name:		nbsmtp
Version:	1.00
Release:	%mkrel 7
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


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.00-7mdv2011.0
+ Revision: 613003
- the mass rebuild of 2010.1 packages

* Fri Apr 16 2010 Funda Wang <fwang@mandriva.org> 1.00-6mdv2010.1
+ Revision: 535334
- rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.00-5mdv2010.0
+ Revision: 430156
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 1.00-4mdv2009.0
+ Revision: 253646
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.00-2mdv2008.1
+ Revision: 136618
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.00-2mdv2008.0
+ Revision: 83819
- rebuild
- Import nbsmtp



* Thu Aug 03 2006 Oden Eriksson <oeriksson@mandriva.com> 1.00-1mdv2007.0
- initial Mandriva package
- added P0,P1 from opensuse
