%define		_class		Numbers
%define		_subclass	Roman
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.2
Release:	9
Summary:	Converting to and from Roman numerals
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Numbers_Roman/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-gd
BuildArch:	noarch
BuildRequires:	php-pear

%description
A class for converting to and from Roman numerals.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-7mdv2012.0
+ Revision: 742171
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-6
+ Revision: 679550
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-5mdv2011.0
+ Revision: 613743
- the mass rebuild of 2010.1 packages

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-4mdv2010.1
+ Revision: 468729
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2010.0
+ Revision: 441498
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2009.1
+ Revision: 322507
- rebuild

* Sun Oct 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-1mdv2009.1
+ Revision: 292886
- update to new version 1.0.2

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-9mdv2009.0
+ Revision: 237029
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-8mdv2007.0
+ Revision: 82469
- Import php-pear-Numbers_Roman

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-8mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-5mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-4mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-3mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdk
- fix spec file to conform with the others

* Sun May 29 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-1mdk
- initial Mandriva package

