%global cartridgedir %{_libexecdir}/openshift/cartridges/redis

Summary:       Provides embedded Redis support
Name:          openshift-cartridge-redis
Version:       0.1.0
Release:       0%{?dist}
Group:         Network/Daemons
License:       ASL 2.0
URL:           http://redis.io
Source0:       %{name}-%{version}.tar.gz
Requires:      php-pecl-redis
Requires:      php54-php-pecl-redis
Requires:      php55-php-pecl-redis
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Provides:      openshift-cartridge-redis = 0.1
BuildArch:     noarch

%description
Provides Redis cartridge support to OpenShift.

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}
%__rm -rf %{buildroot}%{cartridgedir}/rel-eng

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/conf/
%attr(0755,-,-) %{cartridgedir}/hooks/
%attr(0755,-,-) %{cartridgedir}/tests/
%attr(0755,-,-) %{cartridgedir}/versions/
%{cartridgedir}/metadata
%doc %{cartridgedir}/README.md

%changelog
* Mon Mar 16 2015 Builder <getup@getupcloud.com> 0.1.0-0
- new package built with tito

