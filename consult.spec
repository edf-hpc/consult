%define debug_package %{nil}

Summary: Utility to monitor state of a Consul cluster
Name: consult
Version: 0.2
Release: 1%{?dist}.edf
License: CeCILL
Group: Applications/System
URL: https://github.com/edf-hpc/consult
Source: %{name}-%{version}.tar.gz
Requires: python3 python3-requests

%description
This package contains the consult utility which discovers the nodes and
services of a consul cluster and monitor their state. It provides a CLI
with shiny ANSI colors to give a quick overview of the cluster state to
the sysadmins.


%prep
%setup -q

%build
sed -i s#usr/bin/env\ python#usr/bin/env\ python3# consult
%install
install -d %{buildroot}/usr/bin
install -m 755 consult %{buildroot}/usr/bin

%files
%defattr(-, root, root)
/usr/bin/consult

%changelog
* Wed Mar 24 2021 Kwame Amedodji <kwame-externe.amedodji@edf.fr> 0.2-1el8.edf
- first python3 working release
* Fri Sep 18 2020 Pierre Trespeuch <pierre-externe.trespeuch@edf.fr> 0.1-1el8.edf
- Initial RPM release
