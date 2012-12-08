%define pkgname feedparser

Summary: Parse RSS and Atom feeds in Python
Name: python-feedparser
Version: 5.0.1
Release: %mkrel 2
Source0: http://downloads.sourceforge.net/%{pkgname}/%{pkgname}-%{version}.tar.gz
License: BSD
URL: http://feedparser.org/
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: python
BuildRequires: python-devel
BuildArch: noarch

%description
Feedparser is the "Universal Feed Parser" library for python, which
handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds

%prep
%setup -q -n %{pkgname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%check
pushd feedparser
    python feedparsertest.py
popd

%install
rm -rf $RPM_BUILD_ROOT

PYTHONDONTWRITEBYTECODE= python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc LICENSE README


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 5.0.1-1mdv2011.0
+ Revision: 662183
- 5.0.1 (fixes CVE-2009-5065, CVE-2011-1156, CVE-2011-1157, CVE-2011-1158)

* Mon Nov 01 2010 Ahmad Samir <ahmadsamir@mandriva.org> 4.1-9mdv2011.0
+ Revision: 591517
- fix build (python byte code is compiled by feedparser by default)

  + Michael Scherer <misc@mandriva.org>
    - rebuild for python 2.7

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1-8mdv2010.1
+ Revision: 523786
- rebuilt for 2010.1

* Thu Dec 25 2008 Adam Williamson <awilliamson@mandriva.org> 4.1-7mdv2009.1
+ Revision: 319129
- rebuild with python 2.6
- better source location

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 4.1-6mdv2009.0
+ Revision: 259603
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 4.1-5mdv2009.0
+ Revision: 247412
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 4.1-3mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Dec 13 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 4.1-3mdv2007.0
+ Revision: 96541
- Rebuild against new python

  + Michael Scherer <misc@mandriva.org>
    - Import python-feedparser

* Fri Jul 14 2006 Michael Scherer <misc@mandriva.org> 4.1-2mdv2007.0
- Rebuild for new extension

* Thu Jan 12 2006 Michael Scherer <misc@mandriva.org> 4.1-1mdk
- update to last release
- make it rpmbuildupdatable
- from Benoît Guédas <benoit@guedas.com>
  - First Mandriva release

