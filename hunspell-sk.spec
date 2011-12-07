Name: hunspell-sk
Summary: Slovak hunspell dictionaries
Epoch: 1
%define upstreamid 20090330
Version: 0.%{upstreamid}
Release: 2.1%{?dist}
Source: http://www.sk-spell.sk.cx/file_download/51/%{name}-%{upstreamid}.zip
Group: Applications/Text
URL: http://www.sk-spell.sk.cx/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2 or GPLv2 or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Slovak hunspell dictionaries.

%prep
%setup -q -n hunspell-sk-20090106

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1:0.20090330-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20090330-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Caolan McNamara <caolanm@redhat.com> - 1:0.20090330-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20090106-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 11 2009 Caolan McNamara <caolanm@redhat.com> - 1:0.20090106-1
- latest version

* Thu Dec 03 2008 Caolan McNamara <caolanm@redhat.com> - 1:0.20080525-1
- latest version

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 1:0.5.6-2
- clarify that tri-licensed

* Wed Jul 11 2007 Caolan McNamara <caolanm@redhat.com> - 1:0.5.6-1
- canonical upstream version

* Wed Feb 14 2007 Caolan McNamara <caolanm@redhat.com> - 0.20050911-1
- upstream id

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20050228-1
- initial version
