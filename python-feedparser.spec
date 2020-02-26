%define	modname	feedparser

Summary:	Parse RSS and Atom feeds in Python
Name:		python-%{modname}
Version:	5.2.1
Release:	3

Source0:	https://files.pythonhosted.org/packages/ca/f4/91a056f11751701c24f86c692d92fee290b0ba3f99f657cdeb85ad3da402/feedparser-5.2.1.tar.gz
License:	BSD
URL:		https://pypi.org/project/feedparser/
Group:		Development/Python
BuildRequires:	pkgconfig(python2)
BuildRequires:  python-devel
BuildRequires:	python2-distribute
BuildRequires:  python-distribute
BuildArch:	noarch
%rename		python3-%{modname}

%description
Feedparser is the "Universal Feed Parser" library for python, which
handles RSS 0.9x, RSS 1.0, RSS 2.0, CDF, Atom 0.3, and Atom 1.0 feeds

%package -n python2-feedparser
Summary:        Python decorator utilities
Group:          Development/Python
Requires:       python2
 
%description -n python2-feedparser
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
%__python2 setup.py install --root=%{buildroot}
popd

pushd python3
%__python3 setup.py install --root=%{buildroot}
popd

rm -Rf %{buildroot}%{py3_puresitedir}/__pycache__

%files
%defattr(644,root,root,755)
%doc python3/LICENSE python3/
%{py3_puresitedir}/%{modname}*
%{py3_puresitedir}/__pycache__/feedparser.cpython*

%files -n python2-feedparser
%defattr(644,root,root,755)
%doc python2/LICENSE python2/README.rst
%{py2_puresitedir}/%{modname}*

