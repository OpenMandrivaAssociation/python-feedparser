%define pkgname feedparser

Summary: Parse RSS and Atom feeds in Python
Name: python-feedparser
Version: 5.0.1
Release: %mkrel 1
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
rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc LICENSE README
