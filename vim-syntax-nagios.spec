Summary:	Vim syntax: Nagios configuration files syntax
Summary(pl.UTF-8):	Opis składni dla Vima: podświetlanie składni dla plików konfiguracyjnych Nagiosa
Name:		vim-syntax-nagios
Version:	1.17
Release:	1
Epoch:		1
License:	as-is
Group:		Applications/Editors/Vim
Source0:	nagios.vim
URL:		http://bugs.gentoo.org/show_bug.cgi?id=76712
Requires:	vim-rt >= 4:7.2.239-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles
%define		syntax nagios

%description
This plugin provides syntax highlighting for Nagios configuration
files. Detection is by filename (/etc/nagios).

%description -l pl.UTF-8
Ta wtyczka dostarcza podświetlanie składni dla plików konfiguracyjnych
Nagiosa. Pliki są rozpoznawane po nazwie (/etc/nagios).

%prep
rev=$(awk '/^".*Revision:/{print $5}' %{SOURCE0})
if [ "$rev" != "%{version}" ]; then
	: Update version $rev, and retry
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
install %{SOURCE0} $RPM_BUILD_ROOT%{_vimdatadir}/syntax

cat > $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{syntax}.vim <<-EOF
au BufNewFile,BufRead /*etc/nagios/*.cfg,*sample-config/template-object/*.cfg{,.in},/var/lib/nagios/objects.cache set filetype=%{syntax}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*
%{_vimdatadir}/ftdetect/*
