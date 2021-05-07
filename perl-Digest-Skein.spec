#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Digest
%define	pnam	Skein
Summary:	Digest::Skein - Perl interface to the Skein digest algorithm
#Summary(pl.UTF-8):
Name:		perl-Digest-Skein
Version:	0.05
Release:	12
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Digest/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cb7ff5208a078e5e504715e6486a06d5
URL:		http://search.cpan.org/dist/Digest-Skein/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl(Digest)
BuildRequires:	perl(MIME::Base64)
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digest::Skein implements the Skein digest algorithm, submitted to NIST
for the SHA-3 competition.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorarch}/Digest/*.pm
%dir %{perl_vendorarch}/auto/Digest/Skein
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/Skein/*.so
%{_mandir}/man3/*
#it should go to static subpackage, shouldn't it?
#%{perl_vendorarch}/auto/libskein/libskein.a
