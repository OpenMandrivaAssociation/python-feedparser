%define pkgname feedparser
%define version 4.1

Summary: Parse RSS and Atom feeds in Python
Name: python-feedparser
Version: %{version}
Release: %mkrel 8
Source0: http://downloads.sourceforge.net/%{pkgname}/%{pkgname}-%{version}.tar.bz2
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
%setup -q -n %{pkgname}-%{version} -c  

perl -pi -e 's/\r\n$/\n/' $(find docs -type f)
%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc LICENSE README docs/


