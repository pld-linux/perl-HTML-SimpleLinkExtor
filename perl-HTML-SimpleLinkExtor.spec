#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	SimpleLinkExtor
Summary:	HTML::SimpleLinkExtor - Extract links from HTML
#Summary(pl):	
Name:		perl-HTML-SimpleLinkExtor
Version:	0.72
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7d9dcb0229d3dcd54e5c254b15fbe4be
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(HTML::LinkExtor) >= 1.28
BuildRequires:	perl-URI >= 1.09
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a simple HTML link extractor designed for the person who does not
want to deal with the intricacies of C<HTML::Parser> or the de-referencing
needed to get links out of C<HTML::LinkExtor>.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
