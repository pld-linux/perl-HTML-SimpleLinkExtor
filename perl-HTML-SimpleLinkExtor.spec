#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	SimpleLinkExtor
Summary:	HTML::SimpleLinkExtor - extract links from HTML
Summary(pl):	HTML::SimpleLinkExtor - wyodr�bnianie odno�nik�w z HTML-a
Name:		perl-HTML-SimpleLinkExtor
Version:	1.06
Release:	1
License:	?
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b86290d5f29049d198c02ad76f80ee5d
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

%description -l pl
To jest prosty modu� do wyodr�bniania odno�nik�w z HTML-a stworzony dla
os�b, kt�re nie chc� si� wdawa� w skomplikowanie modu�u HTML::Parser ani
dereferencje potrzebne do uzyskania odno�nik�w z modu�u HTML::LinkExtor.

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
