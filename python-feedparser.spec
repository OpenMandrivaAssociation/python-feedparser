%define pkgname feedparser

Summary: Parse RSS and Atom feeds in Python
Name: python-feedparser
Version: 5.1.1
Release: 1

Source0: http://pypi.python.org/packages/source/f/feedparser/%{pkgname}-%{version}.tar.bz2
License: BSD
URL: http://feedparser.org/
Group: Development/Python
Requires: python
BuildRequires: python-devel
BuildRequires: python-setuptools
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

PYTHONDONTWRITEBYTECODE= python setup.py install --root=%{buildroot}

%files
%doc LICENSE README
%py_puresitedir/*
