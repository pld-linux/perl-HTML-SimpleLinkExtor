#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	SimpleLinkExtor
Summary:	HTML::SimpleLinkExtor - extract links from HTML
Summary(pl.UTF-8):   HTML::SimpleLinkExtor - wyodrębnianie odnośników z HTML-a
Name:		perl-HTML-SimpleLinkExtor
Version:	1.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5fbc0759423a9365a68b26be2d2eb233
URL:		http://search.cpan.org/dist/HTML-SimpleLinkExtor/
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
want to deal with the intricacies of HTML::Parser or the de-referencing
needed to get links out of HTML::LinkExtor.

%description -l pl.UTF-8
To jest prosty moduł do wyodrębniania odnośników z HTML-a stworzony dla
osób, które nie chcą się wdawać w skomplikowanie modułu HTML::Parser ani
dereferencje potrzebne do uzyskania odnośników z modułu HTML::LinkExtor.

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
%{perl_vendorlib}/HTML/*.pm
%{_mandir}/man3/*
