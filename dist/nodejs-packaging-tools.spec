#
# spec file for package nodejs-packaging-tools
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           nodejs-packaging-tools
Version:        0.1.0
Release:        0
Summary:        Tools for packaging NodeJS applications and libraries
License:        GPL-2.0
URL:            https://github.com/expeehaa/nodejs-packaging-tools
Source0:        https://github.com/expeehaa/nodejs-packaging-tools/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Tools for packaging NodeJS applications and libraries.

%package -n obs-service-nodejs_pack
Summary:        OBS Service for packaging NodeJS applications and libraries
Requires:       jq
Requires:       npm
Requires:       tar
Requires:       gzip

%description -n obs-service-nodejs_pack
The OBS Source service for packaging NodeJS applications and libraries.

%package -n nodejs-packaging-rpm-macros
Summary:        Macros for packaging NodeJS applications and libraries
Requires:       jq
Requires:       npm

%description -n nodejs-packaging-rpm-macros
RPM Macros for %{name}.

%prep
%autosetup

%build

%install
install -d %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 nodejs_pack %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 nodejs_pack.service %{buildroot}%{_prefix}/lib/obs/service

install -d %{buildroot}%{_rpmconfigdir}/macros.d/
install -m 0644 macros.nodejs %{buildroot}%{_rpmconfigdir}/macros.d/

%files -n obs-service-nodejs_pack
%doc README.adoc
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%files -n nodejs-packaging-rpm-macros
%{_rpmconfigdir}/macros.d/macros.nodejs

%changelog
