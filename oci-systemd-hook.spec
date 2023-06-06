%global provider        github
%global provider_tld    com
%global project         projectatomic
%global repo            oci-systemd-hook
# https://github.com/projectatomic/oci-systemd-hook
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

Name:           %{repo}
Version:        v0.2.0
Release:        0%{shortcommit}%{?dist}
Summary:        OCI systemd hook for docker
Group:          Applications/Text
License:        GPLv3+
URL:            https://%{import_path}
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(yajl)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pcre-devel
BuildRequires:  go-md2man
Obsoletes:      %{name} <= 1.10.3-46
# golang / go-md2man not available on ppc64
ExcludeArch:    ppc64

%description
OCI systemd hooks enable running systemd in a OCI runc/docker container.

%prep

%autosetup

%build
aclocal
autoreconf -i
%configure --libexecdir=%{_libexecdir}/oci/hooks.d/
make %{?_smp_mflags}

%install
%make_install

#define license tag if not already defined
%{!?_licensedir:%global license %doc}
%files
%doc README.md
%license LICENSE
%{_mandir}/man1/%{name}.1*
%dir %{_libexecdir}/oci
%dir %{_libexecdir}/oci/hooks.d
%{_libexecdir}/oci/hooks.d/%{name}
%if 0%{?suse_version}
%dir %{_usr}/share/containers/
%dir %{_usr}/share/containers/oci/
%endif
%dir %{_usr}/share/containers/oci/hooks.d
%{_usr}/share/containers/oci/hooks.d/oci-systemd-hook.json

%changelog
