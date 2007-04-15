Summary:	Secure Shell (SSH) FingerPrint (FP) DNS RR Generator
Summary(pl.UTF-8):	Generator rekordów DNS typu Secure Shell (SSH) FingerPrint (FP)
Name:		sshfp
Version:	1.1.2
Release:	1
License:	GPL v2
Group:		Base
Source0:	ftp://ftp.xelerance.com/sshfp/%{name}-%{version}.tar.gz
# Source0-md5:	807626e651a0a7619f67eb088eb04ece
URL:		ftp://ftp.xelerance.com/sshfp/
BuildRequires:	rpm-pythonprov
Requires:	python-dns
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SSHFP is a small utility for generating RFC 4255 compliant Secure
Shell (SSH) FingerPrint (FP) Resource Records (RR) for the Domain Name
System (DNS) based on the SSH public keys stored in a "known_hosts"
file or SSH public keys which can be obtained by using ssh-keyscan(1).
If the DNS server of a DNS zone allows zone tranfers (AXFR), an entire
zone can be processed for all its A records.

%description -l pl.UTF-8
SSHFP to małe narzędzie do generowania zgodnych z RFC 4255 rekordów
(RR) typu Secure Shell (SSH) FingerPrint (FP) dla usługi DNS (Domain
Name System) w oparciu o klucze publiczne SSH przechowywane w pliku
"known_hosts" lub klucze publiczne SSH uzyskane poprzez
ssh-keyscan(1). Jeśli serwer DNS danej strefy pozwala na transfery
stref (AXFR), można przetworzyć całą strefę dla wszystkich rekordów A.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install sshfp $RPM_BUILD_ROOT%{_bindir}
install sshfp.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README
%attr(755,root,root) %{_bindir}/sshfp
%{_mandir}/man1/sshfp.1*
