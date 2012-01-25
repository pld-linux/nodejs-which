%define		git_hash 5266ec6
%define		pkg	which
Summary:	A JavaScript implementation of the 'which' command
Name:		nodejs-%{pkg}
Version:	1.0.2
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/node-which
# download from https://github.com/isaacs/node-which/tarball/%%{version}
Source0:	isaacs-node-%{pkg}-%{version}-0-g%{git_hash}.tar.gz
# Source0-md5:	d0eae673d48dc782d437b522594cf4bd
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A JavaScript implementation of the '%{pkg}' command.

%prep
%setup -qc
mv isaacs-node-%{pkg}-*/* .

#%nodejs_fixshebang bin/%{pkg}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}
cp -p %{pkg}.js $RPM_BUILD_ROOT%{nodejs_libdir}

install -d $RPM_BUILD_ROOT%{_bindir}
install -p bin/%{pkg} $RPM_BUILD_ROOT%{_bindir}/%{pkg}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/%{pkg}.js
%{nodejs_libdir}/%{pkg}.js
