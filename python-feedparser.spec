%define	modname	feedparser

Summary:	Parse RSS and Atom feeds in Python
Name:		python-%{modname}
Version:	5.1.3
Release:	2

Source0:	http://feedparser.googlecode.com/files/feedparser-%{version}.tar.gz
License:	BSD
URL:		http://code.google.com/p/feedparser/
Group:		Development/Python
BuildRequires:	pkgconfig(python2)
BuildRequires:  python3-devel
BuildRequires:	python-setuptools
BuildRequires:  python3-distribute
BuildArch:	noarch

%description
Feedparser is the "Universal Feed Parser" library for python, which
handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds

%package -n python3-feedparser
Summary:        Python decorator utilities
Group:          Development/Python
Requires:       python3
 
%description -n python3-feedparser
Feedparser is the "Universal Feed Parser" library for python, which
handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds

%prep
%setup -q -c

mv %{modname}-%{version} python2
cp -r python2 python3

%check
#pushd feedparser
#    python feedparsertest.py
#popd

%install
pushd python2
python setup.py install --root=%{buildroot}
popd

pushd python3
python3 setup.py install --root=%{buildroot}
popd

%files
%defattr(644,root,root,755)
%doc python2/LICENSE python2/
%{py_puresitedir}/%{modname}*

%files -n python3-feedparser
%defattr(644,root,root,755)
%doc python3/LICENSE python3/README
%{python3_sitelib}/%{modname}*

