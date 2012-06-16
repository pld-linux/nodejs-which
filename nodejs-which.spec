%define		pkg	which
Summary:	A JavaScript implementation of the 'which' command
Name:		nodejs-%{pkg}
Version:    1.0.5
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/node-which
Source0:    http://registry.npmjs.org/which/-/which-%{version}.tgz
# Source0-md5:	de8504eba9afa3e8a4e7feb9d3b52b38
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A JavaScript implementation of the '%{pkg}' command.

%prep
%setup -qc
mv package/* .

%{__sed} -i -e '1s,^#!.*node,#!/usr/bin/node,' bin/*
chmod a+rx bin/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{nodejs_libdir}/%{pkg}}
cp -a %{pkg}.js bin package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
ln -s %{nodejs_libdir}/%{pkg}/bin/%{pkg} $RPM_BUILD_ROOT%{_bindir}/%{pkg}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/which.js
%dir %{nodejs_libdir}/%{pkg}
%{nodejs_libdir}/%{pkg}/package.json
%{nodejs_libdir}/%{pkg}/%{pkg}.js
%dir %{nodejs_libdir}/%{pkg}/bin
%attr(755,root,root) %{nodejs_libdir}/%{pkg}/bin/which
