Summary:	GNU Line Editor
Name:		ed
Version:	1.8
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	ftp://ftp.gnu.org/pub/gnu/ed/%{name}-%{version}.tar.gz
# Source0-md5:	2268d2344b3c52d23730acb2e3c942fe
URL:		http://www.gnu.org/software/ed/
BuildRequires:	autoconf
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the GNU line editor. It is an implementation of one of the
first editors under *nix. Some programs rely on it, but in general you
probably don't *need* it.

%prep
%setup  -q

rm -f doc/ed.info

%build
%configure
%{__make} all doc

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*info*
%{_mandir}/man1/*

